#!/usr/bin/env python3
import ast
import sys
import difflib
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from data import quotes

DATA_FILE = "data.py"

def load_quotes_from_data():
    with open(DATA_FILE, "r") as f:
        node = ast.parse(f.read())

    for item in node.body:
        if isinstance(item, ast.Assign) and isinstance(item.value, ast.List):
            return [elt.value for elt in item.value.elts if isinstance(elt, ast.Constant)]
    return []

def load_quotes_from_file(file_path):
    with open(file_path, "r") as f:
        node = ast.parse(f.read())

    for item in node.body:
        if isinstance(item, ast.Assign) and isinstance(item.value, ast.List):
            return [elt.value for elt in item.value.elts if isinstance(elt, ast.Constant)]
    return []

def find_internal_duplicates(quotes):
    seen = set()
    duplicates = set()
    for q in quotes:
        if q in seen:
            duplicates.add(q)
        seen.add(q)
    return duplicates

def fuzzy_match(quote, existing_quotes):
    best_ratio = 0
    best_match = None
    for eq in existing_quotes:
        ratio = difflib.SequenceMatcher(None, quote, eq).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = eq
    return best_ratio, best_match

def save_quotes_to_data(new_quotes):
    with open(DATA_FILE, "r") as f:
        content = f.read()

    insert_index = content.rfind("]")
    updated = content[:insert_index] + "".join(f'    "{q}",\n' for q in new_quotes) + content[insert_index:]

    with open(DATA_FILE, "w") as f:
        f.write(updated)

def main():
    if len(sys.argv) < 2:
        print("Usage: python bulk_add.py <quotes_file.py>")
        sys.exit(1)

    file_path = sys.argv[1]
    if not Path(file_path).exists():
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)

    existing_quotes = load_quotes_from_data()
    new_quotes = load_quotes_from_file(file_path)

    # Strict duplicate detection
    duplicates = find_internal_duplicates(new_quotes)
    if duplicates:
        print("❌ Strict Mode Error: Duplicate quotes found within the input file:")
        for d in duplicates:
            print(f"   -> {d}")
        print("\nFix the duplicates inside the file and try again.")
        sys.exit(1)

    quotes_to_add = []
    conflicts = []

    for quote in new_quotes:
        if quote in existing_quotes:
            conflicts.append(quote)
        else:
            ratio, match = fuzzy_match(quote, existing_quotes)
            if ratio > 0.7:
                print(f"⚠ Fuzzy match warning:\n   New quote: {quote}\n   Similar existing: {match}\n   Similarity: {ratio:.2f}")

            quotes_to_add.append(quote)

    if conflicts:
        print("\n⚠ The following quotes already exist and were skipped:")
        for c in conflicts:
            print(f"   -> {c}")

    if quotes_to_add:
        save_quotes_to_data(quotes_to_add)
        print(f"\n✅ Added {len(quotes_to_add)} new quotes successfully.")
    else:
        print("\nℹ No new quotes to add.")

if __name__ == "__main__":
    main()

