"""Team Toolbox — a tiny command-line multi-tool."""

import sys

# --- IMPORT BLOCK --------------------------------------------------
# Add your import at the END of this block, on the line above the dashes.
from tools.shout import shout
# -------------------------------------------------------------------

TOOLS = {
    "shout": shout,
}


def main():
    if len(sys.argv) < 3:
        print("Team Toolbox")
        print("usage: python toolbox.py <tool> <text>")
        print("tools: " + ", ".join(sorted(TOOLS)))
        return
    tool, text = sys.argv[1], " ".join(sys.argv[2:])
    print(TOOLS[tool](text))


if __name__ == "__main__":
    main()
