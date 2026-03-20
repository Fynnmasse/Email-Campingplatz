import re
import os

file_path = r'email.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure we don't accidentally link twice
if 'href="https://www.hamburgpapier-shop.de/search?search=' in html:
    print("Links already exist!")

def wrap_p2(match):
    td_open = match.group(1)
    inner = match.group(2)
    td_close = match.group(3)
    shop_match = re.search(r'Shopsuche:\s*<strong>([^<]+)</strong>', inner)
    if shop_match:
        sid = shop_match.group(1).strip()
        if '<a href=' not in td_open + inner:
            new_inner = f'\n                  <a href="https://www.hamburgpapier-shop.de/search?search={sid}" target="_blank" style="text-decoration:none; color:inherit; display:block;">{inner}\n                  </a>\n                '
            return td_open + new_inner + td_close
    return match.group(0)

html = re.sub(r'(<td width="49%" valign="top" style="background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:10px;">)(.*?)(</td>)', wrap_p2, html, flags=re.DOTALL)

def wrap_p1(match):
    td_open = match.group(1)
    inner = match.group(2)
    td_close = match.group(3)
    
    shop_match = re.search(r'Shopsuche:\s*<strong>([^<]+)</strong>', inner)
    if shop_match:
        sid = shop_match.group(1).strip()
        if '<a href=' not in inner:
            new_inner = f'\n                  <a href="https://www.hamburgpapier-shop.de/search?search={sid}" target="_blank" style="text-decoration:none; color:inherit; display:block;">{inner}\n                  </a>\n                '
            return td_open + new_inner + td_close

    return match.group(0)

html = re.sub(r'(<td width="49%" valign="top" style="background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:12px; vertical-align:top;">)(.*?)(</td>)', wrap_p1, html, flags=re.DOTALL)

# For Nitril and Müllsäcke
html = html.replace('<!-- Nitril-Handschuhe -->\n                  <table', '<!-- Nitril-Handschuhe -->\n                  <a href="https://www.hamburgpapier-shop.de/search?search=Nitril-Handschuhe+Blau+Schwarz" target="_blank" style="text-decoration:none; color:inherit; display:block;">\n                  <table')
# Close Nitril (look for Müllsäcke)
html = html.replace('</table>\n\n                  <!-- Müllsäcke -->', '</table>\n                  </a>\n\n                  <!-- Müllsäcke -->')

html = html.replace('<!-- Müllsäcke -->\n                  <table', '<!-- Müllsäcke -->\n                  <a href="https://www.hamburgpapier-shop.de/search?search=Deiss+Müllsäcke" target="_blank" style="text-decoration:none; color:inherit; display:block;">\n                  <table')
# Close Müllsäcke
html = html.replace('</table>\n                </td>\n\n                <!-- Abstand zwischen Spalten -->', '</table>\n                  </a>\n                </td>\n\n                <!-- Abstand zwischen Spalten -->')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Successfully processed links.")
