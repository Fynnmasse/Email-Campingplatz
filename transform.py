import re

file_path = r'\\sage\Ablage\WEB SHOP\AAA_SHOPWARE 6\E-Mails\Git Hub\Camping-Email\Email-Campingplatz\email.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Backgrounds
html = html.replace('background-color:#f4f4f4;', 'background-color:#E9EFF4;')

# 2. Product boxes
html = html.replace('border:1px solid #e0e0e0; padding:12px; vertical-align:top;', 'background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:12px; vertical-align:top;')
html = html.replace('border:1px solid #e0e0e0; padding:10px;', 'background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:10px;')
html = html.replace('border:1px solid #e0e0e0; border-top:none; padding:10px;', 'background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:10px;')

# 3. Product Titles to Dark Blue
html = re.sub(r'(font-size:\d+px; font-weight:bold;) color:#333(333)?(;">)', r'\1 color:#1d4e74\3', html)

# 4. Price Bubbles
html = re.sub(
    r'<p style="margin:0; font-size:(9|10)px; color:#999(999)?;">(Preis pro [^<]+)</p>\s*<p style="margin:[0-2]px 0 0 0; font-size:(24|26)px; font-weight:bold; color:#c0392b;">([^<]+<span[^>]*>\*</span>)</p>',
    r'<div style="background-color:#e64254; color:#ffffff; border-radius:6px; padding:6px 10px; display:inline-block; text-align:center;"><p style="margin:0; font-size:\1px; color:#ffffff;">\3</p><p style="margin:2px 0 0 0; font-size:20px; font-weight:bold; color:#ffffff;">\4</p></div>',
    html
)

# 5. Shopsuche Pill
html = re.sub(
    r'<p style="margin:[68]px 0 0 0; font-size:1[01]px; color:#666(666)?; (text-align:center; )?border-top:1px solid #eee; padding-top:[46]px;">\s*&#128269; Shopsuche: <strong>([^<]+)</strong>\s*</p>',
    r'<div style="text-align:center; margin-top:8px;"><p style="margin:0; font-size:11px; color:#1d4e74; border:1px solid #1d4e74; border-radius:12px; padding:3px 12px; display:inline-block;">&#128269; Shopsuche: <strong>\2</strong></p></div>',
    html
)

# 6. Saisonpreise header
html = html.replace('color:#3a7ca5; font-style:italic;">Saisonpreise 2026', 'color:#4a8c3f;">Saisonpreise 2026')

# 7. PREMIUM header and text color
html = html.replace('background-color:#3a7ca5; padding:8px;', 'background-color:#0f592a; padding:8px;')
html = html.replace('color:#3a7ca5; font-weight:bold;">100&thinsp;% Zellstoff', 'color:#0f592a; font-weight:bold;">100&thinsp;% Zellstoff')

# 8. Shipping Info boxes
html = re.sub(
    r'style="border:1px solid #eee; padding:4px; font-size:9px; color:#666; text-align:center;"',
    r'style="border:1px solid #dcdcdc; background-color:#f0f4f7; border-radius:4px; padding:4px; font-size:9px; color:#333; text-align:center;"',
    html
)

# 9. Vorteile-Box & Rabatt Badge
html = html.replace('background-color:#fdf2f2;', 'background-color:#ffffff;') # reset Cremeseife
html = html.replace(
    '<td width="49%" valign="top" style="background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:10px;">\n                  <p style="margin:0 0 8px 0; font-size:14px; font-weight:bold; color:#1d4e74;">Ihre Vorteile auf einen Blick:',
    '<td width="49%" valign="top" style="background-color:#a8cde5; border:none; border-radius:8px; padding:10px;">\n                  <p style="margin:0 0 8px 0; font-size:14px; font-weight:bold; color:#1d4e74;">Ihre Vorteile auf einen Blick:'
)
html = html.replace('background-color:#e63946; border-radius:50%; width:90px; height:90px;', 'background-color:#4a8c3f; border-radius:50%; width:90px; height:90px;')

# 10. Bestell-Banner 
html = html.replace('background-color:#4a8c3f; padding:12px 16px; border-radius:4px;', 'background-color:#e64254; padding:12px 16px; border-radius:4px;')

# 11. Footer
html = html.replace('background-color:#f0f0f0; border-top:1px solid #ddd;', 'background-color:#1d4e74;')
html = re.sub(r'color:#666(666)?;">\s*hamburgpapier', r'color:#ffffff;">\n                    hamburgpapier', html)
html = re.sub(r'color:#666(666)?;">\s*Lokstedter', r'color:#ffffff;">\n                    Lokstedter', html)
html = re.sub(r'color:#666(666)?;">\s*Telefon', r'color:#ffffff;">\n                    Telefon', html)
html = re.sub(r'color:#666(666)?;">\s*E-Mail', r'color:#ffffff;">\n                    E-Mail', html)

# 12. Neu-Bereich
html = html.replace('background-color:#f8d7da; border-radius:6px; padding:0; vertical-align:top;', 'background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:0; vertical-align:top; overflow:hidden;')
html = html.replace('<td style="padding:10px 12px 6px 12px;">', '<td style="background-color:#e64254; padding:10px 12px;">')
html = html.replace('color:#c0392b;">Wir erweitern', 'color:#ffffff;">Wir erweitern')
html = html.replace('background-color:#c0392b; color:#ffffff;', 'background-color:#ffffff; color:#e64254;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("Transformation complete.")
