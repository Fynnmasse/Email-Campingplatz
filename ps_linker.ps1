$path = "email.html"
$content = Get-Content -LiteralPath $path -Raw -Encoding UTF8

# Page 2 regex
$pattern2 = '(?s)(<td width="49%" valign="top" style="background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:10px;">)(.*?)(</td>)'
$content = [regex]::Replace($content, $pattern2, {
    param($m)
    $inner = $m.Groups[2].Value
    if ($inner -match 'Shopsuche:\s*<strong>([^<]+)</strong>') {
        $sid = $matches[1].Trim()
        if ($inner -notmatch '<a href=') {
            return $m.Groups[1].Value + "`n                  <a href=`"https://www.hamburgpapier-shop.de/search?search=$sid`" target=`"_blank`" style=`"text-decoration:none; color:inherit; display:block;`">" + $inner + "`n                  </a>`n                " + $m.Groups[3].Value
        }
    }
    return $m.Groups[0].Value
})

# Page 1 regex (padding:12px;)
$pattern1 = '(?s)(<td width="49%" valign="top" style="background-color:#ffffff; border:1px solid #dcdcdc; border-radius:8px; padding:12px; vertical-align:top;">)(.*?)(</td>)'
$content = [regex]::Replace($content, $pattern1, {
    param($m)
    $inner = $m.Groups[2].Value
    if ($inner -match 'Shopsuche:\s*<strong>([^<]+)</strong>') {
        $sid = $matches[1].Trim()
        if ($inner -notmatch '<a href=') {
            return $m.Groups[1].Value + "`n                  <a href=`"https://www.hamburgpapier-shop.de/search?search=$sid`" target=`"_blank`" style=`"text-decoration:none; color:inherit; display:block;`">" + $inner + "`n                  </a>`n                " + $m.Groups[3].Value
        }
    }
    return $m.Groups[0].Value
})

# Nitril-Handschuhe Replace
$content = $content.Replace("<!-- Nitril-Handschuhe -->`n                  <table", "<!-- Nitril-Handschuhe -->`n                  <a href=`"https://www.hamburgpapier-shop.de/search?search=Nitril-Handschuhe`" target=`"_blank`" style=`"text-decoration:none; color:inherit; display:block;`">`n                  <table")
$content = $content.Replace("</table>`n`n                  <!-- Müllsäcke -->", "</table>`n                  </a>`n`n                  <!-- Müllsäcke -->")

# Müllsäcke Replace
$content = $content.Replace("<!-- Müllsäcke -->`n                  <table", "<!-- Müllsäcke -->`n                  <a href=`"https://www.hamburgpapier-shop.de/search?search=Müllsäcke+Deiss`" target=`"_blank`" style=`"text-decoration:none; color:inherit; display:block;`">`n                  <table")
$content = $content.Replace("</table>`n                </td>`n`n                <!-- Abstand zwischen Spalten -->", "</table>`n                  </a>`n                </td>`n`n                <!-- Abstand zwischen Spalten -->")

Set-Content -LiteralPath $path -Value $content -Encoding UTF8
Write-Output "Links applied!"
