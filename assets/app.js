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
      const href=norm((a.getAttribute('href')||'').split('/').pop().split('#')[0]);
      if(href===path) a.classList.add('active');
    });
  }
  document.addEventListener('DOMContentLoaded',()=>{initTheme();initNav();initActiveLinks();});
})();