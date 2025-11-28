#!/usr/bin/env python3
import json
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'generated_materials'
COMBINED = ROOT / 'all_materials_combined.json'
MD = ROOT / 'revision_guide.md'
HTML = ROOT / 'revision_guide.html'

def main():
    data = json.loads(COMBINED.read_text())
    keys = list(data.keys())

    src_key = 'GAME2016 L12 - Collision Detection'
    after_key = 'GAME2016 L9 - Pendulum, Circular, Harmonic motion'

    if src_key in keys:
        keys.remove(src_key)
        # find index of after_key, place src_key after it
        try:
            idx = keys.index(after_key)
            keys.insert(idx+1, src_key)
        except ValueError:
            # if after_key not found, append to end
            keys.append(src_key)

    # rebuild ordered dict
    ordered = OrderedDict((k, data[k]) for k in keys if k in data)

    # write JSON back
    COMBINED.write_text(json.dumps(ordered, indent=2, ensure_ascii=False))

    # regenerate MD and simple HTML guides from ordered combined JSON
    with MD.open('w', encoding='utf-8') as f:
        f.write('# Revision Guide\n\n')
        for k, v in ordered.items():
            title = v.get('file_stem', k)
            overview = v.get('summary', {}).get('overview', '')
            f.write(f'## {title}\n\n')
            f.write(overview + '\n\n')

    with HTML.open('w', encoding='utf-8') as f:
        f.write('<!doctype html>\n<html><head><meta charset="utf-8"><title>Revision Guide</title></head><body>\n')
        f.write('<h1>Revision Guide</h1>\n')
        for k, v in ordered.items():
            title = v.get('file_stem', k)
            overview = v.get('summary', {}).get('overview', '')
            f.write(f'<h2>{title}</h2>\n')
            f.write(f'<p>{overview}</p>\n')
        f.write('</body></html>')

    print('Reordered combined JSON and regenerated guides.')

if __name__ == '__main__':
    main()
