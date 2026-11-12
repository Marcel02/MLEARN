import base64, re, pathlib, sys
root = pathlib.Path(__file__).parent
vend = root.parent / 'vendor' / 'package' / 'dist'
css = (vend / 'katex.min.css').read_text()
def repl(m):
    block = m.group(0)
    w2 = re.search(r'url\(fonts/([^)]+\.woff2)\)', block)
    data = base64.b64encode((vend / 'fonts' / w2.group(1)).read_bytes()).decode()
    return re.sub(r'src:[^;}]*', f'src:url(data:font/woff2;base64,{data}) format("woff2")', block)
css = re.sub(r'@font-face\{[^}]*\}', repl, css)
P = root / 'parts'
order = [l.strip() for l in (root / 'order.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
out = []
for name in order:
    t = (P / name).read_text()
    t = t.replace('/*{{KATEX_CSS}}*/', css)
    if '/*{{FLASH}}*/' in t: t = t.replace('/*{{FLASH}}*/', (root / 'parts' / 'flash_t2.js').read_text())
    out.append(t)
html = '\n'.join(out)
dst = root / 'mlearn-tema2.html'
dst.write_text(html)
print('written', dst, len(html)//1024, 'KB')
