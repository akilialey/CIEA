(function () {
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Hero water: looking down into Carlisle Bay. WebGL caustics, CSS gradient underneath as fallback.
  document.querySelectorAll('canvas.water').forEach(function (canvas) {
    var gl = canvas.getContext('webgl', { antialias: false, alpha: true, premultipliedAlpha: false });
    if (!gl) { canvas.remove(); return; }
    var vs = 'attribute vec2 p;void main(){gl_Position=vec4(p,0.,1.);}';
    var fs = [
      'precision mediump float;uniform vec2 r;uniform float t;',
      'void main(){',
      ' vec2 uv=gl_FragCoord.xy/r.y*1.15;',
      ' float time=t*.32+23.;',
      ' vec2 p=mod(uv*6.28318,6.28318)-250.;',
      ' vec2 i=p;float c=1.;float inten=.005;',
      ' for(int n=0;n<5;n++){float tt=time*(1.-(3.5/float(n+1)));',
      '  i=p+vec2(cos(tt-i.x)+sin(tt+i.y),sin(tt-i.y)+cos(tt+i.x));',
      '  c+=1./length(vec2(p.x/(sin(i.x+tt)/inten),p.y/(cos(i.y+tt)/inten)));}',
      ' c/=5.;c=1.17-pow(c,1.4);float light=pow(abs(c),8.);',
      ' vec2 q=gl_FragCoord.xy/r;',
      ' vec3 sand=vec3(.99,.96,.89);vec3 shallow=vec3(.80,.94,.93);vec3 lagoon=vec3(.56,.86,.88);',
      ' vec3 base=mix(sand,shallow,smoothstep(.15,.85,q.x*.85+q.y*.35));',
      ' base=mix(base,lagoon,smoothstep(.6,1.25,q.x+q.y*.3)*.7);',
      ' vec3 col=base*(1.-light*.10)+light*vec3(1.,1.,.97)*.55;',
      ' gl_FragColor=vec4(col,1.);}'
    ].join('\n');
    function sh(type, src) { var o = gl.createShader(type); gl.shaderSource(o, src); gl.compileShader(o); return o; }
    var prog = gl.createProgram();
    gl.attachShader(prog, sh(gl.VERTEX_SHADER, vs)); gl.attachShader(prog, sh(gl.FRAGMENT_SHADER, fs)); gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) { canvas.remove(); return; }
    gl.useProgram(prog);
    var buf = gl.createBuffer(); gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    var loc = gl.getAttribLocation(prog, 'p'); gl.enableVertexAttribArray(loc); gl.vertexAttribPointer(loc, 2, gl.FLOAT, false, 0, 0);
    var uR = gl.getUniformLocation(prog, 'r'), uT = gl.getUniformLocation(prog, 't');
    var scale = 0.5 * Math.min(window.devicePixelRatio || 1, 2);
    function resize() {
      var w = Math.max(1, Math.round(canvas.clientWidth * scale)), h = Math.max(1, Math.round(canvas.clientHeight * scale));
      if (canvas.width !== w || canvas.height !== h) { canvas.width = w; canvas.height = h; gl.viewport(0, 0, w, h); }
      gl.uniform2f(uR, w, h);
    }
    var visible = true, start = performance.now();
    function frame(now) {
      resize();
      gl.uniform1f(uT, (now - start) / 1000);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      if (!reduceMotion && visible) requestAnimationFrame(frame);
    }
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) {
        var was = visible; visible = e[0].isIntersecting;
        if (visible && !was && !reduceMotion) requestAnimationFrame(frame);
      }).observe(canvas);
    }
    window.addEventListener('resize', function () { if (reduceMotion) frame(start + 8000); });
    requestAnimationFrame(function (n) { frame(reduceMotion ? start + 8000 : n); });
  });
  // Mobile navigation
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
      toggle.querySelector('.i-menu').hidden = open;
      toggle.querySelector('.i-close').hidden = !open;
    });
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a') && nav.classList.contains('open')) toggle.click();
    });
  }

  // Contact form: client-side validation and success state
  var form = document.getElementById('consult-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var ok = true;
      form.querySelectorAll('[required]').forEach(function (input) {
        var field = input.closest('.field');
        var valid = input.value.trim() !== '' && (input.type !== 'email' || /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value.trim()));
        field.classList.toggle('invalid', !valid);
        input.setAttribute('aria-invalid', valid ? 'false' : 'true');
        if (!valid && ok) { input.focus(); ok = false; }
      });
      if (!ok) return;
      var btn = form.querySelector('button[type="submit"]');
      btn.disabled = true;
      btn.textContent = 'Sending...';
      // Connect a form service (Formspree, Netlify Forms, etc.) here before launch.
      setTimeout(function () {
        form.hidden = true;
        var done = document.getElementById('form-success');
        done.hidden = false;
        done.focus();
      }, 600);
    });
    form.querySelectorAll('input, select, textarea').forEach(function (input) {
      input.addEventListener('input', function () { input.closest('.field').classList.remove('invalid'); });
    });
  }

  /* Landing on a section link from another page: fonts and photos can shift the
     layout after the browser's first jump, so settle on the target once they load. */
  function settleOnHash() {
    var id = decodeURIComponent(location.hash.slice(1));
    var el = id && document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'instant', block: 'start' });
  }
  /* Smooth scrolling only switches on after load, so it never animates the
     first jump past a target that is still moving. */
  var root = document.documentElement;
  function ready() { settleOnHash(); root.classList.add('smooth'); }
  if (location.hash.length > 1) {
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(settleOnHash);
  } else {
    /* A fresh visit starts at the top. Embedded previews can keep the outer page
       scrolled down at the old footer, so a new page looked like nothing happened. */
    var navEntry = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];
    if (!navEntry || navEntry.type === 'navigate') toTop();
  }
  if (document.readyState === 'complete') ready(); else window.addEventListener('load', ready);

  function toTop() {
    window.scrollTo({ top: 0, left: 0, behavior: 'instant' });
    root.scrollIntoView({ behavior: 'instant', block: 'start' });
  }
  /* Going to another page jumps to the top the moment the link is clicked, so
     the next page never opens down at the footer, whatever frame it is shown in. */
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href]');
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    if (a.target && a.target !== '_self') return;
    var url = new URL(a.href, location.href);
    if (url.origin !== location.origin) return;
    if (url.hash && url.pathname === location.pathname) return;
    toTop();
  });

})();
