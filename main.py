"""Password Strength Checker: a small CLI that scores a password against common rules."""

import string
import sys
from getpass import getpass
from pathlib import Path

WIDTH = 32
COMMON_PW_FILE = Path("common_pw.txt")

# (minimum ratio of rules passed, label). Checked from top to bottom.
LEVELS = [
    (1.0, "Very Strong"),
    (0.8, "Strong"),
    (0.6, "Moderate"),
    (0.4, "Weak"),
    (0.0, "Very Weak"),
]


def load_common_passwords(path):
    """Read the common-password file into a lowercase set."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        sys.exit(f"Error: {path} not found.")
    return {line.strip().lower() for line in lines if line.strip()}


def build_rules(common_pw):
    """Return a list of (label, test) pairs. Each test takes a password, returns bool."""
    return [
        ("At least 12 characters", lambda p: len(p) >= 12),
        ("An uppercase letter", lambda p: any(c.isupper() for c in p)),
        ("A lowercase letter", lambda p: any(c.islower() for c in p)),
        ("A number", lambda p: any(c.isdigit() for c in p)),
        ("A special character", lambda p: any(c in string.punctuation for c in p)),
        ("Not a commonly used password", lambda p: p.lower() not in common_pw),
    ]


def get_strength(score, total):
    """Map a score to a strength label using the ratio of rules passed."""
    ratio = score / total
    for threshold, label in LEVELS:
        if ratio >= threshold:
            return label


def main():
    rules = build_rules(load_common_passwords(COMMON_PW_FILE))

    print("Password Strength Checker")
    print("=" * WIDTH)
    password = getpass("Enter password (hidden): ")

    print("\nRequirements")
    print("-" * WIDTH)
    score = 0
    for label, test in rules:
        passed = test(password)
        score += passed  # True counts as 1
        print(f"{'✓' if passed else '✗'} {label}")

    print("=" * WIDTH)
    print(f"Score:    {score} / {len(rules)}")
    print(f"Strength: {get_strength(score, len(rules))}")


if __name__ == "__main__":
    main()