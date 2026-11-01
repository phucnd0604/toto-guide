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
  // Index bước: tự gập trên mobile để nội dung walkthrough không bị đẩy xuống quá xa
  function syncIndexBox(){
    const mobile=window.matchMedia('(max-width:900px)').matches;
    document.querySelectorAll('.index-box').forEach(d=>{d.open=!mobile;});
  }
  function initIndexBox(){
    syncIndexBox();
    window.addEventListener('resize',syncIndexBox);
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
  document.addEventListener('DOMContentLoaded',()=>{initTheme();initNav();initActiveLinks();initIndexBox();initReadingChrome();});
})();