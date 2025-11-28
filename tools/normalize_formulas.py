#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'generated_materials'

MATH_KEYWORDS = ['=', '^', 'sin', 'cos', 'tan', 'sqrt', 'atan2', 'pi', 'π', 'r2', 'r^2', '->', '<-', '±']

def looks_like_formula(s: str) -> bool:
    if not s or not s.strip():
        return False
    s = s.strip()
    # obvious junk
    junk_patterns = [r'\[Page', r'GAME2016', r'PowerPoint', r'Perugia', r'Course', r'Page ']
    for p in junk_patterns:
        if re.search(p, s, re.IGNORECASE):
            return False

    # if contains math keywords or typical math punctuation, keep
    for kw in MATH_KEYWORDS:
        if kw in s:
            return True

    # keep if contains digits and any of +-*()/.^
    if re.search(r'\d', s) and re.search(r'[+\-*/()^=.,]', s):
        return True

    # keep if contains common trig names or greek letters
    if re.search(r'\b(sin|cos|tan|atan|atan2|log|exp|sqrt)\b', s, re.IGNORECASE):
        return True

    # otherwise treat as not a formula (likely natural language)
    return False


def clean_practice_problem(problem: str) -> str:
    # detect patterns like "Given the relation: <formula>. Provide..."
    m = re.match(r"(Given the relation:)\s*(.+?)(\.|$)\s*(.*)", problem, re.IGNORECASE)
    if m:
        prefix, relation, rest = m.group(1), m.group(2).strip(), m.group(4)
        if not looks_like_formula(relation):
            relation = '[formula omitted due to parsing artifacts]'
        return f"{prefix} {relation}. {rest}".strip()
    return problem


def process_file(path: Path):
    try:
        data = json.loads(path.read_text())
    except Exception:
        return False

    # clean summary.formulas
    summary = data.get('summary', {})
    formulas = summary.get('formulas', []) or []
    cleaned = [f for f in formulas if looks_like_formula(f)]
    summary['formulas'] = cleaned
    data['summary'] = summary

    # clean practice problems that reference malformed formulas
    pp = data.get('practice_problems', [])
    for p in pp:
        prob = p.get('problem', '')
        newprob = clean_practice_problem(prob)
        p['problem'] = newprob
    data['practice_problems'] = pp

    path.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    return True


def main():
    files = sorted(ROOT.glob('*_materials.json'))
    updated = 0
    for f in files:
        ok = process_file(f)
        if ok:
            updated += 1

    # rebuild combined JSON from per-lecture files preserving existing ordering
    combined_path = ROOT / 'all_materials_combined.json'
    try:
        combined = json.loads(combined_path.read_text())
        keys = list(combined.keys())
    except Exception:
        keys = []

    new_combined = {}
    # if we have an ordering, use it; otherwise use file order
    ordered_files = files
    for k in keys:
        fname = combined[k].get('file_stem') + '_materials.json' if combined.get(k) else None
        if fname:
            p = ROOT / fname
            if p.exists():
                ordered_files = [p] + [x for x in ordered_files if x != p]

    for f in ordered_files:
        try:
            data = json.loads(f.read_text())
            new_combined[data.get('file_stem', f.stem.replace('_materials',''))] = data
        except Exception:
            continue

    combined_path.write_text(json.dumps(new_combined, indent=2, ensure_ascii=False))

    print(f'Normalized formulas in {updated} files, rebuilt combined JSON.')


if __name__ == '__main__':
    main()
