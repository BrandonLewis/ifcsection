# IfcSection

Cross sections and developed elevations along an **IFC4X3 alignment**, live in
Blender with [Bonsai](https://bonsaibim.org), and drawn to DXF sheets.

Slide a section along a road, wall or bridge alignment by station, read
station / offset / elevation anywhere, and export what you see. Cuts are
filled and hatched by material (concrete, rebar, compacted fill, native
earth, gravel, ...), and the model can be shown as it stands on any day of
its 4D schedule.

## Features

- **Station slider**: a section square to the alignment at any station
  (first to last, in feet or metres). An orthographic section camera looks
  down the line. The slider can follow the timeline for a fly-through.
- **Offset slider**: moves the 3D cursor across the section (Lt / Rt) and
  reads the surface there. An offset ruler (CL, 10' Lt, ...) runs across the
  view. Go to Selected reads an element's station range from the IFC.
- **Fills by material**: each cut is filled in its IFC surface style's true
  colour, unlit, with a hatch per kind: stipple, sand, earth, gravel. Tiny
  bars draw as dots.
- **Excavation is ground removed**: an excavation is never drawn as a block
  in the hole. Its outline is the dashed limit of excavation (pay line).
  Before its dig date it is still ground. It can also be shown solid or
  hidden.
- **4D**: show the model on a date of the IFC's schedule (IfcTask links).
  What is not built yet, or is already removed, is hidden and not cut.
- **Developed elevations**: unroll the model along an offset line (a wall
  face, a barrier back) from either side, with hidden lines removed, in
  their own scene.
- **DXF sheets**: export the cross section or a developed elevation as a
  paper-space sheet at a standard scale. Hatch patterns and line weights go
  on their own layers.

## Install

1. Install [Bonsai](https://bonsaibim.org) (it provides ifcopenshell; 0.8.x
   and 0.9 both work).
2. Download `ifcsection_addon-vX.Y.Z.zip` from
   [Releases](https://github.com/BrandonLewis/ifcsection/releases).
3. Blender > Edit > Preferences > Add-ons > **Install from Disk** > the zip,
   then enable **IfcSection**.
4. View3D > Sidebar (N) > **Section**: choose the IFC that Bonsai has open
   (or a file), then click **Load**.

The DXF export needs `ezdxf` in Blender's Python. If it is missing, the add-on
says so.

Coming from BIMForge's "Alignment Section (bimforge)" add-on? Remove that one
first and restart Blender. This is its successor.

## Use from Python

The drawing and stationing modules do not need Blender:

```python
import ifcopenshell
from ifcsection.developed import SectionView, cross_section, write_dxf

f = ifcopenshell.open("model.ifc")
sec = cross_section(f, SectionView("STA 1+00", station=100.0, width=40, depth=5))
write_dxf([sec], "section.dxf")
```

`ifcsection.alignment_station` stations any point (`locate`, `point_at`,
`frame_at_station`). `ifcsection.developed.develop` draws developed
elevations, and `load_set` reads a sheet set (an overall view plus enlarged
segments). `ifcsection.schedule_state` answers what stands on a day.

## Relationship to BIMForge

IfcSection was split out of [BIMForge](https://github.com/BrandonLewis/BIMForge)
with its history. BIMForge keeps its own copies of the stationing and
drawing modules for its command line (`est-bim stations`,
`est-bim elevation`). It does not depend on this add-on. IfcSection reads the
`BIMForge_LinearReference` property set (an element's station and offset)
when an IFC carries one, but it works on any IFC4X3 file with an
IfcAlignment.

## Development

```bash
pip install -e '.[test]'      # BIMForge builds the test models (tests only)
python -m pytest              # the Blender tests skip without bpy
pip install bpy==5.2.3        # Python 3.13: run the add-on headless
python -m pytest tests/blender
python -m ifcsection          # build ./ifcsection_addon.zip
```

Releases: bump `version` in `pyproject.toml` and `__init__.py`, update
`CHANGELOG.md`, then either tag `vX.Y.Z` or run the Release workflow on `main`
(which tags it). Either way it attaches the add-on zip.

## License

Apache-2.0. See `LICENSE` and `NOTICE`.
