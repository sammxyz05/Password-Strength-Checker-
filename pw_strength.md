# Password Strength Checker

A small Python command-line tool that scores a password against common strength rules and checks it against a list of commonly used passwords.

## Features

- Hidden input (the password is not echoed to the terminal)
- Six rules, each shown with a ✓ or ✗
- Checks against a common-password list (case-insensitive)
- Strength level based on the ratio of rules passed, so adding a rule never breaks scoring
- No third-party dependencies

## Rules checked

| # | Rule |
|---|------|
| 1 | At least 12 characters |
| 2 | An uppercase letter |
| 3 | A lowercase letter |
| 4 | A number |
| 5 | A special character (from `string.punctuation`) |
| 6 | Not a commonly used password |

## Strength levels

| Rules passed | Strength |
|--------------|----------|
| 100% | Very Strong |
| 80% and up | Strong |
| 60% and up | Moderate |
| 40% and up | Weak |
| Below 40% | Very Weak |

## Requirements

- Python 3.8+
- A `common_pw.txt` file in the same folder, one password per line

A good source for a list is [SecLists](https://github.com/danielmiessler/SecLists) (`Passwords/Common-Credentials`).

## Usage

```bash
python password_checker.py
```

Example output:

```
Password Strength Checker
================================
Enter password (hidden):

Requirements
--------------------------------
✓ At least 12 characters
✓ An uppercase letter
✓ A lowercase letter
✓ A number
✗ A special character
✓ Not a commonly used password
================================
Score:    5 / 6
Strength: Strong
```

> Note: `getpass` may not work in some IDE consoles (for example PyCharm's run window). Use a real terminal.

## How it works

- Each rule is a `(label, test)` pair, where `test` is a small function returning `True` or `False`.
- `main()` loops over the rules, prints the result, and adds up the score.
- `get_strength()` converts the score into a label using the ratio of rules passed.

## Adding a rule

Add one line to the list in `build_rules()`:

```python
("No spaces", lambda p: " " not in p),
```

The score total and strength levels update automatically.

## Project structure

```
.
├── password_checker.py
├── common_pw.txt
└── README.md
```

## Disclaimer

This is a learning project. Passing every rule does not guarantee a password is safe. Use a password manager and generate long, unique passwords.

## License

MIT