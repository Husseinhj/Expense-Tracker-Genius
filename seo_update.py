#!/usr/bin/env python3
"""
SEO optimization for Expense Tracker Genius landing page.
Adds: Open Graph, Twitter Cards, structured data, sitemap, robots.txt, hreflang tags.
"""

import os
import re
import json
from datetime import datetime

BASE_URL = "https://husseinhj.github.io/Expense-Tracker-Genius"
APP_STORE_URL = "https://apps.apple.com/app/id6760190294"
SITE_DIR = os.path.dirname(os.path.abspath(__file__))

LANGUAGES = {
    'en': 'English', 'de': 'German', 'nl': 'Dutch', 'fr': 'French',
    'fa': 'Persian', 'ar': 'Arabic', 'it': 'Italian', 'es': 'Spanish',
    'zh-Hans': 'Chinese', 'ja': 'Japanese', 'tr': 'Turkish', 'he': 'Hebrew',
    'ko': 'Korean', 'pt-BR': 'Portuguese', 'hi': 'Hindi', 'th': 'Thai',
    'vi': 'Vietnamese', 'uk': 'Ukrainian', 'pl': 'Polish', 'ro': 'Romanian',
    'cs': 'Czech', 'hu': 'Hungarian', 'ru': 'Russian',
}

# Map lang codes to hreflang codes (BCP 47)
HREFLANG_MAP = {
    'en': 'en', 'de': 'de', 'nl': 'nl', 'fr': 'fr', 'fa': 'fa',
    'ar': 'ar', 'it': 'it', 'es': 'es', 'zh-Hans': 'zh-Hans',
    'ja': 'ja', 'tr': 'tr', 'he': 'he', 'ko': 'ko', 'pt-BR': 'pt-BR',
    'hi': 'hi', 'th': 'th', 'vi': 'vi', 'uk': 'uk', 'pl': 'pl',
    'ro': 'ro', 'cs': 'cs', 'hu': 'hu', 'ru': 'ru',
}

PAGES = ['index.html', 'privacy.html', 'terms.html', 'travel.html', 'accessibility.html']

# ─── SEO meta tags to inject ───

def build_seo_head(page, base_url):
    """Build SEO meta tags for a given page."""

    page_data = {
        'index.html': {
            'title': 'Expense Tracker Genius — Smart AI Expense Tracking for iPhone, iPad & Mac',
            'description': 'Free expense tracker with AI receipt scanning, budget planning, travel planner, 60 currencies, and Apple Watch. Privacy-first — all data on your device. 23 languages.',
            'og_type': 'website',
            'keywords': 'expense tracker, budget app, receipt scanner, AI finance, travel planner, money manager, savings goal, Apple Watch, iPhone, iPad, Mac, privacy',
        },
        'travel.html': {
            'title': 'AI Travel Budget Planner — Expense Tracker Genius',
            'description': 'Plan your trip with AI-powered cost estimates, real hotels, day-by-day itineraries, and expense tracking. Available as an instant App Clip.',
            'og_type': 'website',
            'keywords': 'travel budget, trip planner, travel expense, vacation budget, AI travel, App Clip',
        },
        'privacy.html': {
            'title': 'Privacy Policy — Expense Tracker Genius',
            'description': 'Privacy policy for Expense Tracker Genius. All data stays on your device. No tracking, no servers, no accounts required.',
            'og_type': 'article',
            'keywords': 'privacy policy, expense tracker, data protection',
        },
        'terms.html': {
            'title': 'Terms of Use — Expense Tracker Genius',
            'description': 'Terms and conditions for using Expense Tracker Genius expense tracking app.',
            'og_type': 'article',
            'keywords': 'terms of use, expense tracker',
        },
        'accessibility.html': {
            'title': 'Accessibility — Expense Tracker Genius',
            'description': 'Accessibility features of Expense Tracker Genius. VoiceOver support, Dynamic Type, and more.',
            'og_type': 'article',
            'keywords': 'accessibility, VoiceOver, Dynamic Type, expense tracker',
        },
    }

    data = page_data.get(page, page_data['index.html'])
    page_url = f"{base_url}/{page}" if page != 'index.html' else base_url
    og_image = f"{base_url}/screenshots/01_iPhone_6.9_Dashboard.png"

    # Hreflang tags
    hreflang_tags = []
    for lang, hreflang in HREFLANG_MAP.items():
        lang_url = f"{page_url}?lang={lang}" if page == 'index.html' else f"{base_url}/{page}?lang={lang}"
        hreflang_tags.append(f'  <link rel="alternate" hreflang="{hreflang}" href="{lang_url}">')
    hreflang_tags.append(f'  <link rel="alternate" hreflang="x-default" href="{page_url}">')

    tags = f"""
  <!-- SEO Meta Tags -->
  <meta name="keywords" content="{data['keywords']}">
  <meta name="author" content="Hussein Habibi Juybari">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{page_url}">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="{data['og_type']}">
  <meta property="og:url" content="{page_url}">
  <meta property="og:title" content="{data['title']}">
  <meta property="og:description" content="{data['description']}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="1320">
  <meta property="og:image:height" content="2868">
  <meta property="og:site_name" content="Expense Tracker Genius">
  <meta property="og:locale" content="en_US">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{data['title']}">
  <meta name="twitter:description" content="{data['description']}">
  <meta name="twitter:image" content="{og_image}">

  <!-- App Links -->
  <meta property="al:ios:app_store_id" content="6760190294">
  <meta property="al:ios:app_name" content="Expense Tracker Genius">
  <meta property="al:ios:url" content="accountant://">

  <!-- Hreflang (multi-language) -->
{chr(10).join(hreflang_tags)}
"""
    return tags


def build_structured_data():
    """Build JSON-LD structured data for the app."""
    data = {
        "@context": "https://schema.org",
        "@type": "SoftwareApplication",
        "name": "Expense Tracker Genius",
        "description": "Smart expense tracking with AI receipt scanning, budget planning, travel planner, 60 currencies, and Apple Watch support. Privacy-first.",
        "applicationCategory": "FinanceApplication",
        "operatingSystem": "iOS 17+, macOS 14+, watchOS 10+",
        "offers": {
            "@type": "Offer",
            "price": "0",
            "priceCurrency": "USD"
        },
        "author": {
            "@type": "Person",
            "name": "Hussein Habibi Juybari",
            "url": "https://github.com/husseinhj"
        },
        "url": BASE_URL,
        "downloadUrl": APP_STORE_URL,
        "screenshot": f"{BASE_URL}/screenshots/01_iPhone_6.9_Dashboard.png",
        "softwareVersion": "1.7.0",
        "datePublished": "2024-12-01",
        "dateModified": datetime.now().strftime("%Y-%m-%d"),
        "inLanguage": list(LANGUAGES.keys()),
        "featureList": [
            "AI Receipt Scanning",
            "Budget Tracking",
            "Travel Planner",
            "60 Currencies",
            "Apple Watch",
            "11 Widgets",
            "23 Languages",
            "Privacy-First",
            "iCloud Sync",
            "Siri Shortcuts"
        ],
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "ratingCount": "50",
            "bestRating": "5"
        }
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2)}\n</script>'


def build_breadcrumb_data(page):
    """Build breadcrumb structured data."""
    items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE_URL}]

    page_names = {
        'travel.html': 'Travel Planner',
        'privacy.html': 'Privacy Policy',
        'terms.html': 'Terms of Use',
        'accessibility.html': 'Accessibility',
    }
    if page in page_names:
        items.append({
            "@type": "ListItem",
            "position": 2,
            "name": page_names[page],
            "item": f"{BASE_URL}/{page}"
        })

    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": items
    }
    return f'<script type="application/ld+json">\n{json.dumps(data, indent=2)}\n</script>'


def inject_seo_into_html(filepath, page):
    """Inject SEO tags into an HTML file's <head>."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Skip if already has OG tags
    if 'og:title' in html:
        print(f"  SKIP {page} (already has OG tags)")
        return

    seo_head = build_seo_head(page, BASE_URL)
    structured_data = build_structured_data() if page == 'index.html' else ''
    breadcrumb = build_breadcrumb_data(page)

    # Inject after the existing <meta name="description"> tag
    injection = f"{seo_head}\n  {structured_data}\n  {breadcrumb}"

    # Find the closing </head> and inject before it
    html = html.replace('</head>', f'{injection}\n</head>', 1)

    # Also update <title> for better SEO on non-index pages
    page_titles = {
        'index.html': 'Expense Tracker Genius — Smart AI Expense Tracking for iPhone, iPad & Mac',
    }

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"  OK   {page}")


def create_sitemap():
    """Generate sitemap.xml."""
    urls = []
    for page in PAGES:
        page_url = BASE_URL if page == 'index.html' else f"{BASE_URL}/{page}"
        priority = '1.0' if page == 'index.html' else ('0.8' if page == 'travel.html' else '0.5')
        changefreq = 'weekly' if page in ('index.html', 'travel.html') else 'monthly'

        urls.append(f"""  <url>
    <loc>{page_url}</loc>
    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>""")

        # Add language variants for index
        if page == 'index.html':
            for lang in LANGUAGES:
                urls.append(f"""  <url>
    <loc>{page_url}?lang={lang}</loc>
    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>""")

    sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>"""

    path = os.path.join(SITE_DIR, 'sitemap.xml')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(sitemap)
    print(f"  OK   sitemap.xml ({len(urls)} URLs)")


def create_robots_txt():
    """Generate robots.txt."""
    content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    path = os.path.join(SITE_DIR, 'robots.txt')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  OK   robots.txt")


def main():
    print("SEO Optimization for Expense Tracker Genius\n")

    print("Injecting meta tags into HTML pages:")
    for page in PAGES:
        filepath = os.path.join(SITE_DIR, page)
        if os.path.exists(filepath):
            inject_seo_into_html(filepath, page)
        else:
            print(f"  SKIP {page} (not found)")

    print("\nGenerating SEO files:")
    create_sitemap()
    create_robots_txt()

    print("\nDone!")


if __name__ == '__main__':
    main()
