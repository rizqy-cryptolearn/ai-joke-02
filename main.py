"""ai-joke-02 entry: write one joke about AI coding agents to /output/entry.txt.

The joke: I asked my agent for a one-line fix. It gave me a 400-line
refactor and a 2,000-word explanation of why the one line was
'problematic'. Standard library only, no network, deterministic:
two runs write the same bytes.
"""

import os

JOKE = "I asked my agent for a one-line fix. It gave me a 400-line refactor and a 2,000-word explanation of why the one line was 'problematic'."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as handle:
    handle.write(JOKE)
# Guard: the gate takes 1 to 280 characters of UTF-8 text.
if not (1 <= len(JOKE) <= 280) or not JOKE.strip():
    raise SystemExit("entry.txt must hold 1 to 280 characters")
