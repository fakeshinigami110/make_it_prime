
# Prime Pattern Generator

Converts numeric patterns into prime numbers by intelligently modifying digits while preserving the original structure.

## Features
- Transforms patterns into prime numbers with minimal changes
- Preserves visual pattern structure
- Highlights modified digits in red
- Handles large patterns (700+ digits)
- Cross-platform support (Windows/Linux/macOS)

## Example
**Input Pattern:**
```
11111111111111111111111111111111111111111111111
11111111111111111111000000000000000001111111111
11111110000111111111000000000000000001111111111
11111110000111111111000011111111111111111111111
11111110000111111111000011111111111111111111111
11111110000111111111000011111111111111111111111
11111110000000000000000000000000000001111111111
11111110000000000000000000000000000001111111111
11111111111111111111000011111111100001111111111
11111111111111111111000011111111100001111111111
11111111111111111111000011111111100001111111111
11111110000000000000000011111111100001111111111
11111110000000000000000011111111111111111111111
11111111111111111111111111111111111111111111111
```

**Prime Output:**
```
11111111111111111111111111111111111111111111111
11111111111111111111000000000000000001111111111
11111110000111111111000000000000000001111111111
11111110000111111111000011111111111111111111111
11111110000111111111000011111111111111111111111
11111110000111111111000011111111111111111111111
11111110000000000000000000000000000001111111111
11111110000000000000000000000000000001111111111
11111111111111111111000011111111100001111111111
11111111111111111111000011111111100001111111111
11111111111111111111000011111111100001111111111
11111110000000000000000011111111100001111111111
11111110000000000000000011111111111111111111111
11111131111111111111111111111111111111111111117
```
*(3 and 7 appear in red in terminal )*

---

## Installation
### Option 1: From Source
```bash
pip install numpy sympy colorama
python prime_pattern.py
```

### Option 2: Download Pre-built Executable
[![Latest Release](https://img.shields.io/github/v/release/fakeshinigami110/make_it_prime?include_prereleases&label=Download%20Windows%20EXE&style=for-the-badge)](https://github.com/fakeshinigami110/make_it_prime/releases/latest)

1. Download `prime_pattern.exe` from [Releases](https://github.com/fakeshinigami110/make_it_prime/releases/tag/prime_pattern)
2. Run directly (no Python required)

## Usage
1. Launch the program
2. Select option 2 to input a pattern
3. Paste your pattern (press Enter twice after pasting)
4. View the prime result with modified digits highlighted

## Build From Source
```bash
pyinstaller --onefile --icon=assets/app.ico prime_pattern.py
```

## Algorithm
1. Detects most frequent pattern character (e.g., '0')
2. Systematically tests minimal digit changes
3. Highlights both original pattern and modified digits
4. Uses Miller-Rabin primality test for large numbers

---

## Need Help?
Open an [issue](https://github.com/fakeshinigami110/make_it_prime/issues) if you encounter problems with the executable.
```

Key improvements:
1. Added a **download badge** that links directly to your releases
2. Structured installation options clearly (source vs pre-built)
3. Made the releases link more prominent
4. Added troubleshooting guidance
5. Kept all your existing content while making it more actionable

The shield.io badge will automatically update with future releases. Users can now get the EXE with one click!