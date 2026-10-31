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
      toggle.addEventListener('click',()=>nav.classList.toggle('open'));
    }
  }
  function initActiveLinks(){
    const path=location.pathname.split('/').pop()||'index.html';
    document.querySelectorAll('.navbar nav a, .toc a').forEach(a=>{
      const href=(a.getAttribute('href')||'').split('/').pop().split('#')[0];
      if(href===path) a.classList.add('active');
    });
  }
  document.addEventListener('DOMContentLoaded',()=>{initTheme();initNav();initActiveLinks();});
})();