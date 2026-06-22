/* ================================================================
   GRAND HOLIDAYS — GLOBAL UX SCRIPT
   Dark Mode · Back Button · Scroll To Top · Mobile Menu
   ================================================================ */
(function () {
  'use strict';

  /* ── HELPERS ──────────────────────────────────────────────── */
  const $ = (sel, ctx) => (ctx || document).querySelector(sel);
  const $$ = (sel, ctx) => [...(ctx || document).querySelectorAll(sel)];
  const isHome = () => {
    const p = window.location.pathname;
    return p === '/' || p.endsWith('index.html') || p === '';
  };

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     DARK MODE TOGGLE
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function initTheme() {
    const saved = localStorage.getItem('gh-theme');
    const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    const isDark = saved ? saved === 'dark' : prefersDark;
    if (isDark) document.body.classList.add('dark-mode');

    // Inject toggle button into nav-actions
    const navActions = $('.nav-actions');
    if (!navActions || $('#gh-theme-btn')) return;

    const btn = document.createElement('button');
    btn.id = 'gh-theme-btn';
    btn.className = 'gh-theme-toggle';
    btn.setAttribute('aria-label', 'Toggle dark mode');
    btn.setAttribute('title', 'Toggle light / dark mode');
    btn.innerHTML = isDark ? '☀️' : '🌙';

    // Insert before the first child (WhatsApp btn or hamburger)
    const firstChild = navActions.firstChild;
    navActions.insertBefore(btn, firstChild);

    btn.addEventListener('click', () => {
      const dark = document.body.classList.toggle('dark-mode');
      localStorage.setItem('gh-theme', dark ? 'dark' : 'light');
      btn.innerHTML = dark ? '☀️' : '🌙';
    });

    // Sync when system preference changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
      if (!localStorage.getItem('gh-theme')) {
        document.body.classList.toggle('dark-mode', e.matches);
        btn.innerHTML = e.matches ? '☀️' : '🌙';
      }
    });
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     BACK BUTTON
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function initBackButton() {
    if (isHome()) return; // No back btn on homepage
    if ($('#gh-back-btn')) return;

    const btn = document.createElement('button');
    btn.id = 'gh-back-btn';
    btn.className = 'gh-back-btn';
    btn.setAttribute('aria-label', 'Go back');
    btn.setAttribute('title', 'Go back to previous page');
    btn.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="15 18 9 12 15 6"/>
      </svg>
      Back`;
    document.body.appendChild(btn);

    btn.addEventListener('click', () => {
      if (window.history.length > 1) {
        window.history.back();
      } else {
        window.location.href = 'index.html';
      }
    });
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     SCROLL TO TOP
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function initScrollTop() {
    if ($('#gh-scroll-top')) return;

    const btn = document.createElement('button');
    btn.id = 'gh-scroll-top';
    btn.className = 'gh-scroll-top';
    btn.setAttribute('aria-label', 'Scroll to top');
    btn.setAttribute('title', 'Back to top');
    btn.innerHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <polyline points="18 15 12 9 6 15"/>
      </svg>`;
    document.body.appendChild(btn);

    window.addEventListener('scroll', () => {
      btn.classList.toggle('visible', window.scrollY > 350);
    }, { passive: true });

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     MOBILE MENU — Enhanced
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function initMobileMenu() {
    const toggle = $('.mobile-nav-toggle');
    const navMenu = $('.nav-menu');
    if (!toggle || !navMenu) return;

    // Inject overlay
    let overlay = $('#nav-overlay');
    if (!overlay) {
      overlay = document.createElement('div');
      overlay.id = 'nav-overlay';
      overlay.className = 'nav-overlay';
      document.body.appendChild(overlay);
    }

    // Inject close button inside nav
    if (!$('.nav-close-btn', navMenu)) {
      const closeBtn = document.createElement('button');
      closeBtn.className = 'nav-close-btn';
      closeBtn.setAttribute('aria-label', 'Close menu');
      closeBtn.innerHTML = '✕';
      navMenu.insertBefore(closeBtn, navMenu.firstChild);

      closeBtn.addEventListener('click', closeMenu);
    }

    function openMenu() {
      navMenu.classList.add('active');
      overlay.classList.add('active');
      toggle.classList.add('open');
      document.body.classList.add('menu-open');
      toggle.setAttribute('aria-expanded', 'true');
    }

    function closeMenu() {
      navMenu.classList.remove('active');
      overlay.classList.remove('active');
      toggle.classList.remove('open');
      document.body.classList.remove('menu-open');
      toggle.setAttribute('aria-expanded', 'false');
    }

    toggle.addEventListener('click', () => {
      const isOpen = navMenu.classList.contains('active');
      isOpen ? closeMenu() : openMenu();
    });

    overlay.addEventListener('click', closeMenu);

    // Close on nav link click
    $$('.nav-link', navMenu).forEach(link => {
      link.addEventListener('click', () => {
        closeMenu();
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeMenu();
    });

    // Handle nav items with dropdowns on mobile
    $$('.nav-dropdown', navMenu).forEach(item => {
      const toggle = item.querySelector('.dropdown-toggle');
      if (!toggle) return;
      toggle.addEventListener('click', e => {
        if (window.innerWidth <= 768) {
          e.preventDefault();
          item.classList.toggle('active');
        }
      });
    });
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     SMOOTH SCROLL — Internal Anchors
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function initSmoothScroll() {
    $$('a[href^="#"]').forEach(link => {
      link.addEventListener('click', e => {
        const target = document.getElementById(link.getAttribute('href').slice(1));
        if (!target) return;
        e.preventDefault();
        const offset = 80;
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      });
    });
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
     INIT
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initBackButton();
    initScrollTop();
    initMobileMenu();
    initSmoothScroll();
  });

})();
