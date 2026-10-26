const menuButton = document.querySelector('.menu-toggle');
const nav = document.querySelector('#main-nav');

if (menuButton && nav) {
  menuButton.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    menuButton.setAttribute('aria-expanded', String(open));
    menuButton.textContent = open ? 'Fechar' : 'Menu';
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      menuButton.setAttribute('aria-expanded', 'false');
      menuButton.textContent = 'Menu';
    });
  });
}

const revealItems = document.querySelectorAll('.reveal');
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (reducedMotion || !('IntersectionObserver' in window)) {
  revealItems.forEach((item) => item.classList.add('is-visible'));
} else {
  const observer = new IntersectionObserver((entries, currentObserver) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        currentObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealItems.forEach((item) => observer.observe(item));
}

const header = document.querySelector('[data-header]');
let lastScroll = 0;
window.addEventListener('scroll', () => {
  if (!header || reducedMotion) return;
  const currentScroll = window.scrollY;
  header.style.boxShadow = currentScroll > 12 ? '0 8px 28px rgba(8,35,55,.06)' : 'none';
  lastScroll = currentScroll;
}, { passive: true });
