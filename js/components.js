(() => {
  const languages = {
    en: { native: 'English', dir: 'ltr' },
    de: { native: 'Deutsch', dir: 'ltr' },
    nl: { native: 'Nederlands', dir: 'ltr' },
    fr: { native: 'Français', dir: 'ltr' },
    fa: { native: 'فارسی', dir: 'rtl' },
    ar: { native: 'العربية', dir: 'rtl' },
    he: { native: 'עברית', dir: 'rtl' },
    it: { native: 'Italiano', dir: 'ltr' },
    es: { native: 'Español', dir: 'ltr' },
    'pt-BR': { native: 'Português', dir: 'ltr' },
    'zh-Hans': { native: '简体中文', dir: 'ltr' },
    ja: { native: '日本語', dir: 'ltr' },
    ko: { native: '한국어', dir: 'ltr' },
    hi: { native: 'हिन्दी', dir: 'ltr' },
    th: { native: 'ไทย', dir: 'ltr' },
    vi: { native: 'Tiếng Việt', dir: 'ltr' },
    tr: { native: 'Türkçe', dir: 'ltr' },
    ru: { native: 'Русский', dir: 'ltr' },
    uk: { native: 'Українська', dir: 'ltr' },
    pl: { native: 'Polski', dir: 'ltr' },
    ro: { native: 'Română', dir: 'ltr' },
    cs: { native: 'Čeština', dir: 'ltr' },
    hu: { native: 'Magyar', dir: 'ltr' },
  };

  const navItems = [
    { key: 'nav_home', href: 'index.html', page: 'index' },
    { key: 'nav_travel', href: 'travel.html', page: 'travel' },
    { key: 'nav_privacy', href: 'privacy.html', page: 'privacy' },
    { key: 'nav_terms', href: 'terms.html', page: 'terms' },
    { key: 'nav_accessibility', href: 'accessibility.html', page: 'accessibility' },
  ];

  const APP_STORE_URL = 'https://apps.apple.com/app/id6760190294';
  const APP_CLIP_URL = 'https://appclip.apple.com/id?p=com.accountant.app.Clip';
  const CONTACT_URL = 'mailto:hussein.juybari@gmail.com';

  function currentPage() {
    return document.body.dataset.page || 'index';
  }

  function currentLangFromUrl() {
    return new URLSearchParams(window.location.search).get('lang') || 'en';
  }

  function withLang(path, lang) {
    try {
      const url = new URL(path, window.location.href);
      if (url.origin !== window.location.origin) {
        return path;
      }
      url.searchParams.set('lang', lang);
      return `${url.pathname.split('/').pop() || ''}${url.search}${url.hash}`;
    } catch (error) {
      return path;
    }
  }

  function renderHeader() {
    const host = document.getElementById('site-header');
    if (!host) return;

    const lang = currentLangFromUrl();
    const page = currentPage();
    const navMarkup = navItems
      .map((item) => {
        const href = withLang(item.href, lang);
        const isCurrent = item.page === page;
        return `
          <a href="${href}" ${isCurrent ? 'aria-current="page"' : ''} data-i18n="${item.key}">${item.key}</a>
        `;
      })
      .join('');

    const languageOptions = Object.entries(languages)
      .map(([code, meta]) => `<option value="${code}">${meta.native}</option>`)
      .join('');

    host.innerHTML = `
      <header class="site-header glass">
        <div class="container header-inner">
          <a class="brand" href="${withLang('index.html', lang)}" aria-label="Expense Tracker Genius home">
            <img class="brand-logo" src="screenshots/AppIcon.png" alt="Expense Tracker Genius app icon" width="42" height="42">
            <span class="brand-name" data-i18n="app_name">Expense Tracker Genius</span>
          </a>

          <nav class="site-nav" id="site-nav" aria-label="Primary navigation">
            ${navMarkup}
            <div class="nav-mobile-actions">
              <label class="visually-hidden" for="site-language-selector-mobile" data-i18n="Language">Language</label>
              <select id="site-language-selector-mobile" class="language-select nav-mobile-lang" data-i18n="Language" data-i18n-attr="aria-label">
                ${languageOptions}
              </select>
              <a class="header-button secondary" href="${APP_CLIP_URL}" target="_blank" rel="noreferrer" data-i18n="header_try_app_clip">Try App Clip</a>
              <a class="header-button primary" href="${APP_STORE_URL}" target="_blank" rel="noreferrer" data-i18n="header_download">Download</a>
            </div>
          </nav>

          <div class="header-actions header-actions-desktop">
            <label class="visually-hidden" for="site-language-selector" data-i18n="Language">Language</label>
            <select id="site-language-selector" class="language-select" data-i18n="Language" data-i18n-attr="aria-label">
              ${languageOptions}
            </select>
            <a class="header-button secondary" href="${APP_CLIP_URL}" target="_blank" rel="noreferrer" data-i18n="header_try_app_clip">Try App Clip</a>
            <a class="header-button primary" href="${APP_STORE_URL}" target="_blank" rel="noreferrer" data-i18n="header_download">Download</a>
          </div>

          <button class="hamburger" id="hamburger-btn" aria-label="Toggle menu" aria-expanded="false">
            <span></span><span></span><span></span>
          </button>
        </div>
      </header>
    `;

    // Set language on both desktop and mobile selectors
    host.querySelectorAll('.language-select').forEach(sel => {
      sel.value = languages[lang] ? lang : 'en';
    });

    // Hamburger menu toggle
    const hamburger = host.querySelector('#hamburger-btn');
    const nav = host.querySelector('#site-nav');
    if (hamburger && nav) {
      hamburger.addEventListener('click', () => {
        const isOpen = nav.classList.toggle('is-open');
        hamburger.classList.toggle('is-open', isOpen);
        hamburger.setAttribute('aria-expanded', isOpen);
      });
      // Close menu when a nav link is clicked
      nav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
          nav.classList.remove('is-open');
          hamburger.classList.remove('is-open');
          hamburger.setAttribute('aria-expanded', 'false');
        });
      });
    }

    // Mobile language selector change handler
    const mobileLangSel = host.querySelector('#site-language-selector-mobile');
    if (mobileLangSel) {
      mobileLangSel.addEventListener('change', (e) => {
        const newLang = e.target.value;
        const page = window.location.pathname.split('/').pop() || 'index.html';
        window.location.href = withLang(page, newLang);
      });
    }
  }

  function renderFooter() {
    const host = document.getElementById('site-footer');
    if (!host) return;

    const lang = currentLangFromUrl();
    host.innerHTML = `
      <footer class="site-footer">
        <div class="container footer-inner">
          <p class="footer-copy" data-i18n="footer_copyright">© 2026 Expense Tracker Genius</p>
          <nav class="footer-links" aria-label="Footer navigation">
            <a href="${APP_STORE_URL}" target="_blank" rel="noreferrer" data-i18n="footer_app_store">App Store</a>
            <a href="${withLang('privacy.html', lang)}" data-i18n="nav_privacy">Privacy</a>
            <a href="${withLang('terms.html', lang)}" data-i18n="nav_terms">Terms</a>
            <a href="${CONTACT_URL}" data-i18n="footer_contact">Contact</a>
          </nav>
        </div>
      </footer>
    `;
  }

  document.addEventListener('DOMContentLoaded', () => {
    renderHeader();
    renderFooter();
  });

  window.SiteComponents = {
    languages,
    APP_STORE_URL,
    APP_CLIP_URL,
    CONTACT_URL,
    withLang,
    renderHeader,
    renderFooter,
  };
})();

