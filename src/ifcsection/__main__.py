"""Build the IfcSection Blender add-on zip.

Examples:
    python -m ifcsection
    python -m ifcsection --out dist/ifcsection.zip
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from ifcsection.build import ADDON, build_addon


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m ifcsection",
                                 description=__doc__.splitlines()[0])
    ap.add_argument("--out", type=Path, default=Path(f"{ADDON}.zip"),
                    help="zip to write (default: ./%(default)s)")
    args = ap.parse_args(argv)
    out = build_addon(args.out)
    print(f"wrote {out} - install it in Blender: Edit > Preferences > "
          f"Add-ons > Install from Disk", file=sys.stderr)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
