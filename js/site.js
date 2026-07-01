(function () {
  'use strict';

  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

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

  /* Scroll reveal */
  if ('IntersectionObserver' in window) {
    var revealEls = document.querySelectorAll(
      '.card, .section-header, .quote-card, .founder-bio, .step, .testimonial, .case-study, .gmb-widget, .dominance-feature, .blog-card, .blog-hero-carousel'
    );
    revealEls.forEach(function (el) { el.classList.add('agency-reveal'); });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -30px 0px' });

    revealEls.forEach(function (el) { observer.observe(el); });
  }

  /* Blog hero carousel + progress bar */
  var carousel = document.getElementById('blog-hero-carousel');
  var progressBar = document.getElementById('blog-hero-progress');
  var slideInterval = 6000;
  var progressTimer = null;

  function resetProgress() {
    if (!progressBar) return;
    progressBar.style.transition = 'none';
    progressBar.style.width = '0%';
    void progressBar.offsetWidth;
    if (reducedMotion) return;
    progressBar.style.transition = 'width ' + slideInterval + 'ms linear';
    progressBar.style.width = '100%';
  }

  if (carousel) {
    var slides = carousel.querySelectorAll('.blog-hero-slide');
    var dots = document.querySelectorAll('.blog-hero-dot');
    var current = 0;

    function showSlide(index) {
      slides.forEach(function (slide, i) {
        slide.classList.toggle('is-active', i === index);
      });
      dots.forEach(function (dot, i) {
        dot.classList.toggle('is-active', i === index);
      });
      current = index;
      resetProgress();
    }

    dots.forEach(function (dot) {
      dot.addEventListener('click', function () {
        showSlide(parseInt(dot.getAttribute('data-slide'), 10));
        if (progressTimer) clearInterval(progressTimer);
        if (slides.length > 1 && !reducedMotion) {
          progressTimer = setInterval(function () {
            showSlide((current + 1) % slides.length);
          }, slideInterval);
        }
      });
    });

    showSlide(0);

    if (slides.length > 1 && !reducedMotion) {
      progressTimer = setInterval(function () {
        showSlide((current + 1) % slides.length);
      }, slideInterval);
    }
  }

  /* Blog sidebar: search, open, close */
  var sidebar = document.getElementById('blog-sidebar');
  var sidebarOpen = document.getElementById('blog-sidebar-open');
  var sidebarClose = document.getElementById('blog-sidebar-close');
  var blogSearch = document.querySelector('[data-blog-search]');

  function setSidebarOpen(open) {
    if (!sidebar) return;
    sidebar.classList.toggle('is-open', open);
    if (sidebarOpen) sidebarOpen.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open && window.innerWidth < 1100 ? 'hidden' : '';
  }

  if (sidebarOpen) {
    sidebarOpen.addEventListener('click', function () {
      setSidebarOpen(true);
    });
  }
  if (sidebarClose) {
    sidebarClose.addEventListener('click', function () {
      setSidebarOpen(false);
    });
  }
  if (sidebar) {
    sidebar.addEventListener('click', function (e) {
      if (e.target === sidebar) setSidebarOpen(false);
    });
  }

  if (blogSearch) {
    blogSearch.addEventListener('input', function () {
      var q = blogSearch.value.toLowerCase().trim();
      document.querySelectorAll('.blog-sidebar-post[data-search-title]').forEach(function (el) {
        var title = el.getAttribute('data-search-title') || '';
        var show = !q || title.indexOf(q) !== -1;
        el.style.display = show ? '' : 'none';
      });
      document.querySelectorAll('.blog-sidebar-list a[data-search-title]').forEach(function (el) {
        var title = el.getAttribute('data-search-title') || '';
        var li = el.closest('li');
        if (li) li.style.display = !q || title.indexOf(q) !== -1 ? '' : 'none';
      });
    });
  }

  /* Form fallback when Formspree is not configured */
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