"""Genera index.html autocontenido (sin red) a partir de las mismas piezas que la versión publicada."""
import base64, pathlib, re, sys
root = pathlib.Path(__file__).parent
P = root / 'parts'
vend = root.parent / 'vendor' / 'package' / 'dist'
fonts = root.parent / 'vendor-fonts'
def inline_imgs(html):
    """Sustituye src="img/x.webp" por la imagen incrustada en base64."""
    def rep(m):
        data = base64.b64encode((root / 'img' / m.group(1)).read_bytes()).decode()
        return 'src="data:image/webp;base64,' + data + '"'
    return re.sub(r'src="img/([^"]+\.webp)"', rep, html)
out_dir = pathlib.Path(sys.argv[1])
out_dir.mkdir(parents=True, exist_ok=True)

# KaTeX CSS con sus fuentes incrustadas (igual que build.py)
kcss = (vend / 'katex.min.css').read_text()
def repl(m):
    block = m.group(0)
    w2 = re.search(r'url\(fonts/([^)]+\.woff2)\)', block)
    data = base64.b64encode((vend / 'fonts' / w2.group(1)).read_bytes()).decode()
    return re.sub(r'src:[^;}]*', f'src:url(data:font/woff2;base64,{data}) format("woff2")', block)
kcss = re.sub(r'@font-face\{[^}]*\}', repl, kcss)

# Tipografías de la página incrustadas (sustituyen a Google Fonts)
FACES = [('IBM Plex Sans', 'fontsource-ibm-plex-sans-5.0.20', 'ibm-plex-sans', [(400,'normal'),(500,'normal'),(600,'normal'),(700,'normal'),(400,'italic')]),
         ('IBM Plex Mono', 'fontsource-ibm-plex-mono-5.0.13', 'ibm-plex-mono', [(400,'normal'),(500,'normal')]),
         ('Source Serif 4', 'fontsource-source-serif-4-5.0.19', 'source-serif-4', [(400,'normal'),(600,'normal'),(400,'italic')])]
ff = []
for fam, pkg, stem, variants in FACES:
    for wgt, sty in variants:
        f = fonts / pkg / 'package' / 'files' / f'{stem}-latin-{wgt}-{sty}.woff2'
        data = base64.b64encode(f.read_bytes()).decode()
        ff.append(f'@font-face{{font-family:"{fam}";font-style:{sty};font-weight:{wgt};font-display:swap;src:url(data:font/woff2;base64,{data}) format("woff2")}}')
font_css = '\n'.join(ff)

order = [l.strip() for l in (root / 'order.txt').read_text().splitlines() if l.strip() and not l.startswith('#')]
head_parts = [n for n in order if n < '10']
body_parts = [n for n in order if n >= '10']

head = '\n'.join((P / n).read_text() for n in head_parts)
head = head.replace('/*{{KATEX_CSS}}*/', kcss)
head = re.sub(r'<link rel="preconnect"[^>]*>\s*', '', head)
head = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com[^>]*>', '<style>' + font_css + '</style>', head)
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', '')

body = '\n'.join((P / n).read_text() for n in body_parts)
body = body.replace('/*{{FLASH}}*/', (P / 'flash_t2.js').read_text())
kjs = (vend / 'katex.min.js').read_text()
ajs = (vend / 'contrib' / 'auto-render.min.js').read_text()
body = body.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js"></script>', '<script>' + kjs + '</script>')
body = body.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js"></script>', '<script>' + ajs + '</script>')
body = inline_imgs(body)
assert 'cdnjs' not in body and 'googleapis' not in head, 'quedan recursos externos'

reset = ('<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
         'body{margin:0;font:14px system-ui,-apple-system,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>')
html = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        + reset + '\n' + head + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')
(out_dir / 'index.html').write_text(html)
print('index.html', len(html)//1024, 'KB')
