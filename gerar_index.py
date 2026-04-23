import os, re

pasta = '.'
arquivos = sorted([
    f for f in os.listdir(pasta)
    if f.endswith('.html') and f != 'index.html'
])

cards = ''
for f in arquivos:
    titulo = re.sub(r'[-_]+', ' ', f.replace('.html', '')).title()
    cards += f'<a class="card" href="{f}" target="_blank"><div class="card-name">{titulo}</div><div class="card-file">{f}</div></a>\n'

with open('index.html', 'r', encoding='utf-8') as fh:
    html = fh.read()

# Substitui o bloco entre as marcações
novo = re.sub(
    r'<!-- FILES:START -->.*?<!-- FILES:END -->',
    f'<!-- FILES:START -->\n{cards}<!-- FILES:END -->',
    html, flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as fh:
    fh.write(novo)

print(f'{len(arquivos)} arquivo(s) listado(s).')
