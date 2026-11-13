# ai-joke-03 entry: writes one joke about AI coding agents to
# $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt in the grader).
# Standard library only, deterministic: both runs write identical bytes.
import os

JOKE = "My agent's favorite debugging technique is deleting the test that fails."

# The gate requires 1-280 characters and at least one non-space character.
assert 1 <= len(JOKE) <= 280 and any(not c.isspace() for c in JOKE)

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(JOKE)
