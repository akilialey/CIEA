(function () {
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

  // Postmark city cycle: real direct-flight cities to and from Bridgetown
  var cities = ['LONDON', 'TORONTO', 'LAGOS', 'NEW YORK', 'ACCRA', 'MIAMI', 'MONTREAL'];
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var cycling = document.querySelectorAll('.pm-city[data-cycle]');
  if (cycling.length && !reduce) {
    var i = 0;
    setInterval(function () {
      i = (i + 1) % cities.length;
      cycling.forEach(function (el) {
        el.classList.add('swap');
        setTimeout(function () { el.textContent = cities[i]; el.classList.remove('swap'); }, 350);
      });
    }, 2600);
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

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
