"""Build the installable Blender add-on zip.

Blender installs an add-on from a zip holding one package. The zip carries
`addon.py` as the package's __init__ and its sibling modules (stationing,
the developed / cross-section drawing, the 4D state, the section styles).
The drawing needs shapely, which Bonsai ships, and ezdxf for its DXF.

Examples:
    python -m ifcsection                       # -> ./ifcsection_addon.zip
    python -m ifcsection --out dist/ifcsection.zip
    # Blender: Edit > Preferences > Add-ons > Install from Disk... > the zip
"""
from __future__ import annotations

import zipfile
from pathlib import Path

ADDON = "ifcsection_addon"
#: the modules the add-on carries next to its __init__
MODULES = ("alignment_station", "developed", "schedule_state", "section_style")


def build_addon(out: str | Path) -> Path:
    """Write the installable add-on zip to `out`; returns the path."""
    here = Path(__file__).resolve().parent
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(here / "addon.py", f"{ADDON}/__init__.py")
        for name in MODULES:
            z.write(here / f"{name}.py", f"{ADDON}/{name}.py")
    return out
