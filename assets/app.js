(function(){
  const root=document.documentElement;
  function applyTheme(t){
    root.setAttribute('data-theme',t);
    localStorage.setItem('totk-theme',t);
    const btn=document.querySelector('.theme-toggle');
    if(btn) btn.textContent = t==='dark' ? '☀️ Sáng' : '🌙 Tối';
  }
  function initTheme(){
    const saved=localStorage.getItem('totk-theme');
    const prefersDark=window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(saved || (prefersDark?'dark':'light'));
    const btn=document.querySelector('.theme-toggle');
    if(btn) btn.addEventListener('click',()=>applyTheme(root.getAttribute('data-theme')==='dark'?'light':'dark'));
  }
  function initNav(){
    const toggle=document.querySelector('.nav-toggle');
    const nav=document.querySelector('.navbar nav');
    if(toggle&&nav){
      toggle.setAttribute('aria-expanded','false');
      toggle.addEventListener('click',()=>{
        const open=nav.classList.toggle('open');
        toggle.setAttribute('aria-expanded',open?'true':'false');
      });
    }
  }
  function norm(v){return (v||'').replace(/\.html$/,'').replace(/\/$/,'')||'index';}
  function initActiveLinks(){
    const path=norm(location.pathname.split('/').pop());
    document.querySelectorAll('.navbar nav a, .toc a').forEach(a=>{
      const raw=a.getAttribute('href')||'';
      if(raw.startsWith('#')) return;           // mục lục trong trang do scrollspy lo
      const href=norm(raw.split('/').pop().split('#')[0]);
      if(href===path) a.classList.add('active');
    });
  }
  // Index bước: tự gập trên mobile để nội dung walkthrough không bị đẩy xuống quá xa
  function syncIndexBox(){
    const mobile=window.matchMedia('(max-width:900px)').matches;
    document.querySelectorAll('.index-box').forEach(d=>{d.open=!mobile;});
    // mục lục vùng cũng gập trên mobile; trên desktop mở nhưng không ép đóng nếu người dùng tự mở
    document.querySelectorAll('.rail-toc-box').forEach(d=>{ if(mobile) d.open=false; else if(d.dataset.userClosed!=='1') d.open=true; });
  }
  function initIndexBox(){
    syncIndexBox();
    window.addEventListener('resize',syncIndexBox);
    document.querySelectorAll('.rail-toc-box').forEach(d=>{
      d.addEventListener('toggle',()=>{ d.dataset.userClosed = d.open ? '0' : '1'; });
    });
  }
  // Thanh tiến độ đọc + nút lên đầu trang
  function initReadingChrome(){
    const bar=document.createElement('div');
    bar.id='read-progress';
    document.body.appendChild(bar);
    const btn=document.createElement('button');
    btn.className='back-to-top';
    btn.type='button';
    btn.setAttribute('aria-label','Lên đầu trang');
    btn.textContent='↑';
    document.body.appendChild(btn);
    btn.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
    const update=()=>{
      const h=document.documentElement;
      const max=h.scrollHeight-h.clientHeight;
      const pct=max>0?(h.scrollTop||document.body.scrollTop)/max:0;
      bar.style.width=(pct*100)+'%';
      btn.classList.toggle('show',(h.scrollTop||document.body.scrollTop)>600);
    };
    document.addEventListener('scroll',update,{passive:true});
    window.addEventListener('resize',update);
    update();
  }
  // Menu con "Lộ trình": bấm nút mũi tên để mở/đóng, đóng khi bấm ra ngoài hoặc Esc
  function initRouteMenu(){
    const item=document.querySelector('.nav-item');
    const btn=document.querySelector('.nav-sub-toggle');
    if(!item||!btn) return;
    const set=(open)=>{
      item.classList.toggle('open',open);
      btn.setAttribute('aria-expanded',open?'true':'false');
    };
    btn.addEventListener('click',(e)=>{
      e.preventDefault();e.stopPropagation();
      set(!item.classList.contains('open'));
    });
    document.addEventListener('click',(e)=>{
      if(!item.contains(e.target)) set(false);
    });
    document.addEventListener('keydown',(e)=>{if(e.key==='Escape') set(false);});
  }
  // Đánh dấu mục đang đọc trong rail trái khi cuộn walkthrough
  function initScrollSpy(){
    const links=[...document.querySelectorAll('.rail-toc a[href^="#"]')];
    if(!links.length||!('IntersectionObserver' in window)) return;
    const map=new Map();
    links.forEach(a=>{
      const el=document.getElementById(a.getAttribute('href').slice(1));
      if(el) map.set(el,a);
    });
    if(!map.size) return;
    const current=new Set();
    const io=new IntersectionObserver((entries)=>{
      entries.forEach(en=>{
        if(en.isIntersecting) current.add(en.target); else current.delete(en.target);
      });
      let active=null;
      for(const el of map.keys()){ if(current.has(el)){ active=el; break; } }
      if(!active){
        // mục gần mép trên nhất
        let best=null,bestTop=-Infinity;
        map.forEach((a,el)=>{
          const t=el.getBoundingClientRect().top;
          if(t<160&&t>bestTop){bestTop=t;best=el;}
        });
        active=best;
      }
      links.forEach(a=>a.classList.remove('active'));
      if(active&&map.has(active)) map.get(active).classList.add('active');
    },{rootMargin:'-96px 0px -65% 0px',threshold:0});
    map.forEach((_,el)=>io.observe(el));
  }
  document.addEventListener('DOMContentLoaded',()=>{initTheme();initNav();initActiveLinks();initIndexBox();initReadingChrome();initRouteMenu();initScrollSpy();});
})();