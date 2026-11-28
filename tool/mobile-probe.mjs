#!/usr/bin/env node
/**
 * Đo bề rộng trang bằng Chrome headless (CDP, không cần dependency).
 * Dùng cho tool/check-mobile.py — không gọi trực tiếp trừ khi cần debug.
 *
 * Cách dùng:
 *   node tool/mobile-probe.mjs --width 375 --height 900 <file.html> [file.html ...]
 *   node tool/mobile-probe.mjs --width 375 --chrome "C:\\...\\chrome.exe" <file>
 *   node tool/mobile-probe.mjs --width 375 --shot DIR --full <file>   # chụp ảnh để tự review
 *
 * In ra một dòng JSON: [{"file":..., "width":375, "scrollWidth":375, "shot": "..."}]
 * Thiếu Chrome -> in {"error": "..."} và thoát mã 3.
 */
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawn } from "node:child_process";

const CANDIDATES = [
  "C:/Program Files/Google/Chrome/Application/chrome.exe",
  "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
  path.join(process.env.LOCALAPPDATA || "", "Google/Chrome/Application/chrome.exe"),
  "C:/Program Files/Microsoft/Edge/Application/msedge.exe",
  "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe",
  "/usr/bin/google-chrome",
  "/usr/bin/google-chrome-stable",
  "/usr/bin/chromium",
  "/usr/bin/chromium-browser",
];

function parseArgs(argv) {
  const out = { width: 375, height: 900, chrome: null, files: [], shot: null, full: false, eager: false, anchor: null };
  for (let i = 0; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--width") out.width = parseInt(argv[++i], 10);
    else if (a === "--height") out.height = parseInt(argv[++i], 10);
    else if (a === "--chrome") out.chrome = argv[++i];
    else if (a === "--shot") out.shot = argv[++i];
    else if (a === "--full") out.full = true;
    else if (a === "--eager") out.eager = true;
    else if (a === "--anchor") out.anchor = argv[++i];
    else out.files.push(a);
  }
  return out;
}

// Ảnh lazy không được tải khi chụp ngoài khung nhìn -> gallery ra trắng.
// Đặt eager rồi đợi decode xong mới chụp, nếu không ảnh trong ảnh chụp sẽ trống.
async function warmImages(cdp) {
  await cdp.send("Runtime.evaluate", {
    expression: "document.querySelectorAll('img[loading=lazy]').forEach(i=>{i.loading='eager';}); 1",
    returnByValue: true,
  });
  await cdp.send("Runtime.evaluate", {
    expression:
      "Promise.all([...document.images].map(i=>i.complete?0:new Promise(r=>{i.onload=i.onerror=r;}))).then(()=>document.images.length)",
    awaitPromise: true,
    returnByValue: true,
  });
  await sleep(300);
}

async function scrollToAnchor(cdp, anchor) {
  if (!anchor) return;
  await cdp.send("Runtime.evaluate", {
    expression:
      "(()=>{const el=document.querySelector(location.hash||" + JSON.stringify(anchor) + ");" +
      "if(el){document.documentElement.style.scrollBehavior='auto'; el.scrollIntoView({block:'start'});} return window.scrollY;})()",
    returnByValue: true,
  });
  await sleep(400);
}

function shotPath(shot, file, width, full) {
  const base = path.basename(file).replace(/\.html?$/i, "") + "-" + width + (full ? "-full" : "") + ".png";
  if (/\.png$/i.test(shot)) return shot;
  fs.mkdirSync(shot, { recursive: true });
  return path.join(shot, base);
}

async function capture(cdp, opts, file) {
  const out = shotPath(opts.shot, file, opts.width, opts.full);
  let clip = null;
  if (opts.full) {
    const metrics = await cdp.send("Page.getLayoutMetrics");
    const size = metrics.cssContentSize || metrics.contentSize;
    clip = {
      x: 0,
      y: 0,
      width: Math.min(size.width, opts.width),
      height: Math.min(size.height, Number(process.env.SHOT_MAX_HEIGHT || 16000)),
      scale: 1,
    };
  }
  const shot = await cdp.send("Page.captureScreenshot", {
    format: "png",
    captureBeyondViewport: !!opts.full,
    ...(clip ? { clip } : {}),
  });
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, Buffer.from(shot.data, "base64"));
  return out;
}

function findChrome(explicit) {
  for (const c of [explicit, ...CANDIDATES]) {
    if (c && fs.existsSync(c)) return c;
  }
  return null;
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

async function waitFor(predicate, timeoutMs, label) {
  const start = Date.now();
  while (Date.now() - start < timeoutMs) {
    const value = predicate();
    if (value) return value;
    await sleep(100);
  }
  throw new Error("hết thời gian chờ " + label);
}

class Cdp {
  constructor(url) {
    this.ws = new WebSocket(url);
    this.id = 0;
    this.pending = new Map();
    this.events = [];
    this.ready = new Promise((resolve, reject) => {
      this.ws.addEventListener("open", () => resolve());
      this.ws.addEventListener("error", (e) => reject(new Error("WebSocket lỗi: " + e.message)));
    });
    this.ws.addEventListener("message", (ev) => {
      const msg = JSON.parse(ev.data);
      if (msg.id && this.pending.has(msg.id)) {
        const { resolve, reject } = this.pending.get(msg.id);
        this.pending.delete(msg.id);
        msg.error ? reject(new Error(msg.method + ": " + msg.error.message)) : resolve(msg.result);
      } else if (msg.method) {
        this.events.push(msg.method);
      }
    });
  }

  async send(method, params = {}) {
    await this.ready;
    const id = ++this.id;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.ws.send(JSON.stringify({ id, method, params }));
      setTimeout(() => {
        if (this.pending.has(id)) {
          this.pending.delete(id);
          reject(new Error("hết thời gian chờ " + method));
        }
      }, 30000);
    });
  }

  close() {
    try { this.ws.close(); } catch {}
  }
}

async function measure(port, file, opts, width, height) {
  const url = "file:///" + file.replace(/\\/g, "/");
  const res = await fetch(`http://127.0.0.1:${port}/json/new?${encodeURIComponent(url)}`, { method: "PUT" });
  if (!res.ok) throw new Error("không mở được tab (" + res.status + ")");
  const target = await res.json();
  const cdp = new Cdp(target.webSocketDebuggerUrl);
  try {
    await cdp.send("Page.enable");
    await cdp.send("Runtime.enable");
    await cdp.send("Emulation.setDeviceMetricsOverride", {
      width, height, deviceScaleFactor: 1, mobile: false,
    });
    await waitFor(() => cdp.events.includes("Page.loadEventFired"), 20000, "tải trang " + path.basename(file));
    if (opts.shot && (opts.eager || opts.full)) await warmImages(cdp);
    if (opts.shot) await scrollToAnchor(cdp, opts.anchor);
    const { result } = await cdp.send("Runtime.evaluate", {
      expression: `(() => {
        const d = document.documentElement;
        const wide = [];
        document.querySelectorAll("body *").forEach((el) => {
          const r = el.getBoundingClientRect();
          if (r.right > d.clientWidth + 1 && r.width > 0) wide.push(el.tagName.toLowerCase());
        });
        return JSON.stringify({
          clientWidth: d.clientWidth,
          scrollWidth: d.scrollWidth,
          wide: [...new Set(wide)].slice(0, 5),
        });
      })()`,
      returnByValue: true,
    });
    const data = JSON.parse(result.value);
    const out = { file, width, clientWidth: data.clientWidth, scrollWidth: data.scrollWidth, wide: data.wide };
    if (opts.shot) out.shot = await capture(cdp, opts, file);
    return out;
  } finally {
    cdp.close();
    await fetch(`http://127.0.0.1:${port}/json/close/${target.id}`).catch(() => {});
  }
}

async function main() {
  if (typeof WebSocket === "undefined") {
    console.log(JSON.stringify({ error: "cần Node >= 22 (có WebSocket toàn cục)" }));
    process.exit(3);
  }
  const args = parseArgs(process.argv.slice(2));
  if (!args.files.length) {
    console.log(JSON.stringify({ error: "không có file nào để đo" }));
    process.exit(2);
  }
  const chromePath = findChrome(args.chrome);
  if (!chromePath) {
    console.log(JSON.stringify({ error: "không tìm thấy Chrome/Edge trên máy" }));
    process.exit(3);
  }
  const userDir = fs.mkdtempSync(path.join(os.tmpdir(), "totk-mobile-"));
  const proc = spawn(chromePath, [
    "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
    "--disable-extensions", "--disable-background-networking", "--mute-audio",
    "--remote-debugging-port=0", "--user-data-dir=" + userDir, "about:blank",
  ], { stdio: "ignore" });

  try {
    const portFile = path.join(userDir, "DevToolsActivePort");
    const port = await waitFor(() => {
      if (!fs.existsSync(portFile)) return null;
      const text = fs.readFileSync(portFile, "utf8").split(/\r?\n/)[0].trim();
      return text ? parseInt(text, 10) : null;
    }, 30000, "Chrome khởi động");

    // đợi endpoint HTTP sẵn sàng
    await waitFor(() => null, 0, "").catch(() => {});
    for (let i = 0; i < 60; i++) {
      try { const r = await fetch(`http://127.0.0.1:${port}/json/version`); if (r.ok) break; } catch {}
      await sleep(200);
    }

    const results = [];
    for (const file of args.files) {
      try {
        results.push(await measure(port, file, args, args.width, args.height));
      } catch (err) {
        results.push({ file, width: args.width, error: String(err.message || err) });
      }
    }
    console.log(JSON.stringify(results));
  } finally {
    try { proc.kill(); } catch {}
    await sleep(300);
    try { fs.rmSync(userDir, { recursive: true, force: true }); } catch {}
  }
}

main().catch((err) => {
  console.log(JSON.stringify({ error: String(err.message || err) }));
  process.exit(4);
});
