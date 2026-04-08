(() => {
  const languageMeta = (window.SiteComponents && window.SiteComponents.languages) || {};
  const rtlLanguages = new Set(['ar', 'fa', 'he']);
  const cache = new Map();

  let currentLanguage = 'en';
  let currentTranslations = {};

  function supportedLanguages() {
    return Object.keys(languageMeta);
  }

  function normalizeLanguage(language) {
    if (!language) return null;
    if (languageMeta[language]) return language;

    const lower = language.toLowerCase();
    const exact = supportedLanguages().find((code) => code.toLowerCase() === lower);
    if (exact) return exact;
    if (lower.startsWith('zh')) return 'zh-Hans';
    if (lower === 'pt' || lower.startsWith('pt-')) return 'pt-BR';

    const base = lower.split('-')[0];
    return supportedLanguages().find((code) => code.toLowerCase() === base) || null;
  }

  function resolveLanguage(preferredLanguage) {
    return (
      normalizeLanguage(preferredLanguage) ||
      normalizeLanguage(new URLSearchParams(window.location.search).get('lang')) ||
      normalizeLanguage(navigator.language) ||
      normalizeLanguage((navigator.languages || [])[0]) ||
      'en'
    );
  }

  async function loadLocale(language) {
    const normalized = normalizeLanguage(language) || 'en';
    if (cache.has(normalized)) {
      return cache.get(normalized);
    }

    const promise = fetch(`locales/${encodeURIComponent(normalized)}.json`, { cache: 'no-cache' })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to load locale: ${normalized}`);
        }
        return response.json();
      })
      .catch(() => (normalized === 'en' ? {} : loadLocale('en')));

    cache.set(normalized, promise);
    return promise;
  }

  function translatedValue(key) {
    return currentTranslations[key] ?? key;
  }

  function setDocumentDirection(language) {
    document.documentElement.lang = language;
    document.documentElement.dir = rtlLanguages.has(language) ? 'rtl' : 'ltr';
  }

  function applyTextTranslations() {
    document.querySelectorAll('[data-i18n]').forEach((element) => {
      const key = element.dataset.i18n;
      if (!key) return;

      const value = translatedValue(key);
      const attrs = element.dataset.i18nAttr;
      if (attrs) {
        attrs
          .split(',')
          .map((item) => item.trim())
          .filter(Boolean)
          .forEach((attr) => element.setAttribute(attr, value));
      } else {
        element.textContent = value;
      }
    });

    document.querySelectorAll('[data-i18n-content]').forEach((element) => {
      const key = element.dataset.i18nContent;
      if (!key) return;
      element.textContent = String(translatedValue(key)).replace(/\\n/g, '\n');
    });

    document.querySelectorAll('[data-i18n-html]').forEach((element) => {
      const key = element.dataset.i18nHtml;
      if (!key) return;
      element.innerHTML = translatedValue(key);
    });

    const titleElement = document.querySelector('title[data-i18n]');
    if (titleElement) {
      document.title = titleElement.textContent;
    }
  }

  function isInternalLink(href) {
    return href && !href.startsWith('#') && !/^(mailto:|tel:|https?:)/i.test(href);
  }

  function preserveLanguageInLinks(language) {
    document.querySelectorAll('a[href]').forEach((link) => {
      if (link.dataset.noPreserveLang === 'true') return;
      if (!link.dataset.baseHref) {
        link.dataset.baseHref = link.getAttribute('href');
      }

      const baseHref = link.dataset.baseHref;
      if (!isInternalLink(baseHref)) return;

      try {
        const url = new URL(baseHref, window.location.href);
        if (url.origin !== window.location.origin) return;
        url.searchParams.set('lang', language);
        link.setAttribute('href', `${url.pathname.split('/').pop() || ''}${url.search}${url.hash}`);
      } catch (error) {
        link.setAttribute('href', baseHref);
      }
    });
  }

  function syncLanguageSelector(language) {
    const selector = document.getElementById('site-language-selector');
    if (!selector) return;
    selector.value = language;

    if (!selector.dataset.boundChange) {
      selector.addEventListener('change', (event) => {
        changeLanguage(event.target.value, { updateHistory: true });
      });
      selector.dataset.boundChange = 'true';
    }
  }

  function updateHistory(language) {
    const url = new URL(window.location.href);
    url.searchParams.set('lang', language);
    history.replaceState({}, '', `${url.pathname}${url.search}${url.hash}`);
  }

  function dispatchUpdateEvent() {
    document.dispatchEvent(
      new CustomEvent('i18n:updated', {
        detail: {
          lang: currentLanguage,
          translations: currentTranslations,
          t: translatedValue,
        },
      })
    );
  }

  async function changeLanguage(language, options = {}) {
    const targetLanguage = resolveLanguage(language);
    const [englishLocale, targetLocale] = await Promise.all([
      loadLocale('en'),
      targetLanguage === 'en' ? Promise.resolve({}) : loadLocale(targetLanguage),
    ]);

    currentLanguage = targetLanguage;
    currentTranslations = { ...englishLocale, ...targetLocale };

    setDocumentDirection(targetLanguage);
    syncLanguageSelector(targetLanguage);
    applyTextTranslations();
    preserveLanguageInLinks(targetLanguage);

    if (options.updateHistory !== false) {
      updateHistory(targetLanguage);
    }

    dispatchUpdateEvent();
    return currentTranslations;
  }

  async function initialize() {
    await changeLanguage(resolveLanguage(), { updateHistory: true });
  }

  document.addEventListener('DOMContentLoaded', initialize);

  window.SiteI18n = {
    changeLanguage,
    getLanguage: () => currentLanguage,
    getTranslations: () => ({ ...currentTranslations }),
    isRTL: (language) => rtlLanguages.has(language || currentLanguage),
    resolveLanguage,
    t: translatedValue,
  };
})();

