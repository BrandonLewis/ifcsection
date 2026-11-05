# Changelog

Newest first. Versions follow `pyproject.toml`; a tag `vX.Y.Z` publishes the add-on zip.

## Unreleased

### Fixed

Ported from BIMForge (its fix for this project's PR #1 review):

- **Ground still to dig draws its edges beyond the cut.** Before the dig
  date, the visible edges beyond a section or elevation now show the ground
  as it stands, not the ground with its hole already dug. When every void
  of a host is still to dig, the host is drawn uncut beyond the plane. A
  ground solid that its cut removes entirely, lying behind the plane, no
  longer vanishes from the pre-dig view. A host with some voids already
  dug is drawn as before, with all of its voids. Ground that is not
  standing at the date (placed later, or already removed) restores nothing.

## 0.1.1 - 2026-11-05

### Fixed

Ported from BIMForge 0.1.100 (its PR #8 review):

- **Restored ground stays inside its host.** Before its dig date, a cut
  that voids the ground restores only the ground, not the air above it. A
  cut can reach past grade, as an opening runs past its wall.
  - **Sections and DXF:** the restored fill is clipped to the host's uncut
    section.
  - **Blender add-on:** the same clip applies to Solid mode's
    volume-removed fill.

  A pay-item excavation body (unhosted) is the soil itself, so it is still
  restored whole.
- **No ground is restored where the section misses the host.** When the
  section plane cuts a hosted cut but not the ground it voids, the add-on
  no longer fills the whole cut there (in either the pre-dig view or Solid
  mode). This matches the DXF sections.
- **Drawing extents take in the limits of excavation**, so a section of an
  excavation alone is no longer clipped.

## 0.1.0 - 2026-11-05

First release as its own project, split out of BIMForge (0.1.98 and the
unreleased excavation work after it), with its history.

- **Renamed** from "Alignment Section (bimforge)" to **IfcSection**.
  - Blender identifiers changed: the scene property `ifcsection`, the
    operators `ifcsection.*`, the add-on package `ifcsection_addon`.
  - Remove the old add-on before installing this one.
  - Scenes saved with the old add-on keep their old settings, but this one
    does not read them.
- **Python package:** `ifcsection` carries the stationing, drawing, 4D and
  section-style modules. It needs only ifcopenshell, numpy and shapely (plus
  ezdxf for DXF), and never imports Blender or BIMForge.
- **Carried over from BIMForge:**
  - the station and offset sliders and the 4D date filter;
  - fills and hatches by material;
  - Export Section DXF;
  - developed elevations, and Exit;
  - excavation drawn as ground removed (the dashed limit of excavation; the
    Limits / Solid / Hidden modes);
  - enclosed cavities cut as holes;
  - compatibility with ifcopenshell 0.8 (Bonsai 0.8.x).
