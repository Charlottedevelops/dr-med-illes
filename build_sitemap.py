import os

BASE = os.path.dirname(os.path.abspath(__file__))
DOMAIN = "https://peterilles.info"
LANG_ORDER = ["de", "en", "fr", "it", "es", "pt", "hu"]
PATHS = {"de": "/", "en": "/en/", "fr": "/fr/", "it": "/it/", "es": "/es/", "pt": "/pt/", "hu": "/hu/"}

alt_block = "\n".join(
    f'    <xhtml:link rel="alternate" hreflang="{c}" href="{DOMAIN}{PATHS[c]}"/>' for c in LANG_ORDER
) + f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/"/>'

urls = []
for c in LANG_ORDER:
    urls.append(f'''  <url>
    <loc>{DOMAIN}{PATHS[c]}</loc>
{alt_block}
  </url>''')

sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(urls)}
</urlset>
'''

with open(os.path.join(BASE, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap)

robots = f'''User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
'''
with open(os.path.join(BASE, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots)

print("sitemap.xml and robots.txt written")
