(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var isMobile = window.innerWidth < 768;

  var toggle = document.getElementById('nav-toggle');
  var mobileNav = document.getElementById('nav-mobile');

  if (toggle && mobileNav) {
    toggle.addEventListener('click', function () {
      var isOpen = mobileNav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    });

    mobileNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        mobileNav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener('click', function (e) {
      var target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  /* ── Live starfield canvas (skipped when reduced-motion or low-power mobile) ── */
  if (!reducedMotion) {
  var canvas = document.createElement('canvas');
  canvas.id = 'cosmic-starfield';
  canvas.setAttribute('aria-hidden', 'true');
  document.body.prepend(canvas);

  var aurora = document.createElement('div');
  aurora.className = 'cosmic-aurora';
  aurora.setAttribute('aria-hidden', 'true');
  document.body.prepend(aurora);

  var ctx = canvas.getContext('2d');
  var stars = [];
  var mouse = { x: 0.5, y: 0.5 };
  var smoothMouse = { x: 0.5, y: 0.5 };
  var w = 0;
  var h = 0;
  var dpr = 1;
  var shooting = null;
  var nextShoot = Date.now() + 8000;

  function rand(min, max) {
    return min + Math.random() * (max - min);
  }

  function buildStars(count) {
    stars = [];
    for (var i = 0; i < count; i++) {
      stars.push({
        x: Math.random(),
        y: Math.random(),
        z: rand(0.2, 1),
        r: rand(0.4, 1.8),
        tw: rand(0, Math.PI * 2),
        spd: rand(0.008, 0.03),
        hue: Math.random() > 0.85 ? 45 : Math.random() > 0.7 ? 190 : 0
      });
    }
  }

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    w = window.innerWidth;
    h = window.innerHeight;
    canvas.width = w * dpr;
    canvas.height = h * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = h + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    var density = isMobile ? 6500 : 4200;
    buildStars(Math.floor((w * h) / density));
  }

  function maybeShoot() {
    var now = Date.now();
    if (!shooting && now > nextShoot) {
      shooting = {
        x: rand(0, w * 0.6),
        y: rand(0, h * 0.35),
        vx: rand(6, 11),
        vy: rand(1.5, 3.5),
        life: 1
      };
      nextShoot = now + rand(12000, 28000);
    }
  }

  function draw() {
    ctx.clearRect(0, 0, w, h);
    smoothMouse.x += (mouse.x - smoothMouse.x) * 0.04;
    smoothMouse.y += (mouse.y - smoothMouse.y) * 0.04;
    var parX = (smoothMouse.x - 0.5) * 28;
    var parY = (smoothMouse.y - 0.5) * 18;

    for (var i = 0; i < stars.length; i++) {
      var s = stars[i];
      s.tw += s.spd;
      var flicker = 0.55 + Math.sin(s.tw) * 0.45;
      var sx = s.x * w + parX * s.z;
      var sy = s.y * h + parY * s.z;
      var alpha = flicker * (0.25 + s.z * 0.75);
      var radius = s.r * (0.6 + s.z * 0.6);

      if (s.hue === 45) {
        ctx.fillStyle = 'rgba(232, 201, 106, ' + alpha + ')';
      } else if (s.hue === 190) {
        ctx.fillStyle = 'rgba(56, 189, 248, ' + alpha * 0.9 + ')';
      } else {
        ctx.fillStyle = 'rgba(255, 255, 255, ' + alpha + ')';
      }

      ctx.beginPath();
      ctx.arc(sx, sy, radius, 0, Math.PI * 2);
      ctx.fill();

      if (s.z > 0.75 && flicker > 0.9) {
        ctx.strokeStyle = 'rgba(255,255,255,' + (alpha * 0.25) + ')';
        ctx.lineWidth = 0.5;
        ctx.beginPath();
        ctx.moveTo(sx - radius * 3, sy);
        ctx.lineTo(sx + radius * 3, sy);
        ctx.moveTo(sx, sy - radius * 3);
        ctx.lineTo(sx, sy + radius * 3);
        ctx.stroke();
      }
    }

    maybeShoot();
    if (shooting) {
      var g = ctx.createLinearGradient(
        shooting.x, shooting.y,
        shooting.x - shooting.vx * 12, shooting.y - shooting.vy * 12
      );
      g.addColorStop(0, 'rgba(255,255,255,' + shooting.life + ')');
      g.addColorStop(0.4, 'rgba(56,189,248,' + (shooting.life * 0.6) + ')');
      g.addColorStop(1, 'transparent');
      ctx.strokeStyle = g;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(shooting.x, shooting.y);
      ctx.lineTo(shooting.x - shooting.vx * 12, shooting.y - shooting.vy * 12);
      ctx.stroke();
      shooting.x += shooting.vx;
      shooting.y += shooting.vy;
      shooting.life -= 0.028;
      if (shooting.life <= 0 || shooting.x > w + 50) shooting = null;
    }

    requestAnimationFrame(draw);
  }

  window.addEventListener('resize', resize);
  window.addEventListener('mousemove', function (e) {
    mouse.x = e.clientX / (window.innerWidth || 1);
    mouse.y = e.clientY / (window.innerHeight || 1);
  });

  resize();
  requestAnimationFrame(draw);
  }

  /* ── Scroll reveal ── */
  if ('IntersectionObserver' in window) {
    var revealEls = document.querySelectorAll(
      '.card, .section-header, .quote-card, .founder-bio, .step, .testimonial, .case-study, .gmb-widget'
    );
    revealEls.forEach(function (el) { el.classList.add('cosmic-reveal'); });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

    revealEls.forEach(function (el) { observer.observe(el); });
  }

  /* ── Form fallback when Formspree is not configured ── */
  document.querySelectorAll('form[data-tsbr-form="fallback"]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = form.getAttribute('data-tsbr-email') || 'hello@tsbrenterprises.com';
      var data = new FormData(form);
      var lines = [];
      var subject = 'TSBR Website Inquiry';
      data.forEach(function (value, key) {
        if (key === '_subject') {
          subject = value;
        } else if (value) {
          lines.push(key + ': ' + value);
        }
      });
      window.location.href =
        'mailto:' + email +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(lines.join('\n'));
    });
  });
})();