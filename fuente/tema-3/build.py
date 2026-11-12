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
def inline_imgs(html):
    """Sustituye src="img/x.webp" por la imagen incrustada en base64."""
    def rep(m):
        data = base64.b64encode((root / 'img' / m.group(1)).read_bytes()).decode()
        return 'src="data:image/webp;base64,' + data + '"'
    return re.sub(r'src="img/([^"]+\.webp)"', rep, html)
P = root / 'parts'
order = [l.strip() for l in (root / 'order.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
out = []
for name in order:
    t = (P / name).read_text()
    t = t.replace('/*{{KATEX_CSS}}*/', css)
    out.append(t)
html = inline_imgs('\n'.join(out))
dst = root / 'mlearn-tema3.html'
dst.write_text(html)
print('written', dst, len(html)//1024, 'KB')
