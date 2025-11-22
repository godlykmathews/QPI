#!/usr/bin/env python3

import argparse
import ast
import sys
from difflib import SequenceMatcher
from typing import List, Tuple
import shutil

from pathlib import Path 

sys.path.append(str(Path(__file__).parent.parent))

from data import quotes 

def normalize(s: str, ignore_case: bool) -> str:
    s = " ".join(s.split())
    return s.lower() if ignore_case else s

def extract_string_literals(source: str) -> List[Tuple[str, int]]:
    literals = []
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return literals

    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            literals.append((node.value, getattr(node, "lineno", None)))
    return literals

def fuzzy_ratio(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()

def find_matches(query: str, source: str, ignore_case: bool, threshold: float):
    qn = normalize(query, ignore_case)
    literals = extract_string_literals(source)

    exact_matches = []
    fuzzy_matches = []

    for val, lineno in literals:
        vn = normalize(val, ignore_case)
        if vn == qn:
            exact_matches.append((val, lineno))
        else:
            score = fuzzy_ratio(vn, qn)
            if score >= threshold:
                fuzzy_matches.append((val, lineno, score))

    return exact_matches, fuzzy_matches

def add_quote_to_file(file_path: str, quote: str):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    backup_path = file_path + ".bak"
    shutil.copy(file_path, backup_path)
    print(f"📦 Backup created: {backup_path}")

    inserted = False
    new_lines = []

    for line in lines:
        # insert before closing bracket of list
        if line.strip() == "]" and not inserted:
            new_lines.append(f'    "{quote}",\n')
            inserted = True
        new_lines.append(line)

    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("✨ Quote added successfully!")

def main():
    ap = argparse.ArgumentParser(description="Check duplicate or similar quotes and optionally add")
    ap.add_argument("quote", help="Quote to check")
    ap.add_argument("--file", "-f", default="data.py", help="File to check and modify")
    ap.add_argument("--add", action="store_true", help="Add the quote if not found")
    ap.add_argument("--threshold", type=float, default=0.75, help="Fuzzy similarity threshold (0-1)")
    args = ap.parse_args()

    try:
        with open(args.file, "r", encoding="utf-8") as fh:
            src = fh.read()
    except FileNotFoundError:
        print(f"File not found: {args.file}", file=sys.stderr)
        sys.exit(2)

    exact, fuzzy = find_matches(args.quote, src, ignore_case=True, threshold=args.threshold)

    if exact:
        print("✔ Exact match already exists:")
        for val, ln in exact:
            print(f"  line {ln}: {val!r}")
        sys.exit(0)

    if fuzzy:
        print("⚠ Similar quote(s) found:")
        for val, ln, score in sorted(fuzzy, key=lambda x: -x[2]):
            print(f"  {score:.2f} similarity at line {ln}: {val!r}")
        print("\nNot adding due to similarity.")
        sys.exit(1)

    print("✖ No match found.")

    if args.add:
        add_quote_to_file(args.file, args.quote)
        sys.exit(0)
    else:
        print("Use --add to append it:")
        print(f'  python check_quote.py "{args.quote}" --add')
        sys.exit(1)

if __name__ == "__main__":
    main()

