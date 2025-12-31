#!/usr/bin/env python3
"""
Script per convertire Quaderno_Ricette_Completo.md in formato JSON
per l'editor collaborativo di ricette.
"""

import json
import re
from pathlib import Path

def crea_slug(titolo):
    """Crea uno slug URL-friendly dal titolo della ricetta"""
    slug = titolo.lower()
    slug = re.sub(r'[àáâã]', 'a', slug)
    slug = re.sub(r'[èéêë]', 'e', slug)
    slug = re.sub(r'[ìíîï]', 'i', slug)
    slug = re.sub(r'[òóôõ]', 'o', slug)
    slug = re.sub(r'[ùúûü]', 'u', slug)
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    slug = slug.strip('-')
    return slug

def estrai_immagini(testo):
    """Estrae i riferimenti alle immagini dal formato `(IMG_XXXX.jpg)`"""
    match = re.search(r'`\((.*?)\)`', testo)
    if match:
        img_str = match.group(1)
        # Gestisce immagini multiple separate da virgola
        immagini = [img.strip() for img in img_str.split(',')]
        return immagini
    return []

def pulisci_titolo(titolo):
    """Rimuove i riferimenti alle immagini dal titolo"""
    return re.sub(r'\s*`\(.*?\)`\s*', '', titolo).strip()

def converti_markdown_a_json(file_md, file_json):
    """Converte il file Markdown in formato JSON"""

    # Leggi il file sorgente
    with open(file_md, 'r', encoding='utf-8') as f:
        contenuto = f.read()

    # Splitta per heading di livello 2
    sezioni = re.split(r'\n## ', contenuto)

    ricette = []

    for i, sezione in enumerate(sezioni):
        # Salta intestazioni vuote o la prima sezione se non inizia con ##
        if not sezione.strip() or (i == 0 and not sezione.startswith('## ')):
            continue

        # La prima riga è il titolo (senza il ## iniziale se splittato)
        righe = sezione.split('\n', 1)
        titolo_raw = righe[0].strip()

        # Estrai immagini dal titolo
        immagini = estrai_immagini(titolo_raw)

        # Pulisci titolo
        titolo = pulisci_titolo(titolo_raw)

        # Il resto è il contenuto markdown
        markdown = righe[1].strip() if len(righe) > 1 else ''

        # Rimuovi eventuali separatori --- finali
        markdown = re.sub(r'\n---\s*$', '', markdown).strip()

        # Crea slug
        slug = crea_slug(titolo)

        # Costruisci oggetto ricetta
        ricetta = {
            "id": slug,
            "titolo": titolo,
            "immagini": immagini,  # Array di immagini
            "markdown": markdown,
            "verificato": False
        }

        ricette.append(ricetta)

    # Salva in JSON
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(ricette, f, ensure_ascii=False, indent=2)

    print(f"✓ Conversione completata!")
    print(f"  {len(ricette)} ricette salvate in {file_json}")
    print(f"  {sum(1 for r in ricette if r['immagini'])} ricette con immagini")
    print(f"  {sum(1 for r in ricette if not r['immagini'])} ricette senza immagini")

if __name__ == '__main__':
    # Percorsi file
    file_sorgente = Path(__file__).parent.parent / 'Quaderno_Ricette_Completo.md'
    file_destinazione = Path(__file__).parent / 'data' / 'ricette.json'

    print(f"Conversione da: {file_sorgente}")
    print(f"           a: {file_destinazione}")
    print()

    converti_markdown_a_json(file_sorgente, file_destinazione)
