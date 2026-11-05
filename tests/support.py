"""Test models, built with BIMForge (a TEST-only dependency; the ifcsection
package itself never imports it): a three-element alignment with a vertical
curve, and a deck swept along it.

Copied from BIMForge's own test fixtures (bimforge/author/tests/
test_emit_alignment.py), which its wheel does not ship.
"""
from __future__ import annotations

import uuid

import ifcopenshell
from bimforge.author.alignment import Alignment, Profile
from bimforge.author.emit_ifc import emit_ifc
from bimforge.author.model import Element, StructureModel
from bimforge.author.project import ProjectContext
from bimforge.author.sweep import SweptSection

POB = {"station": 1000.0, "northing": 1_943_100.0, "easting": 6_594_050.0}
RUN = [{"kind": "tangent", "bearing": "N 10-0-0 E", "length": 120.0},
       {"kind": "curve", "delta": "25-0-0", "radius": 400.0, "turn": "R",
        "length": 174.533},
       {"kind": "curve", "delta": "15-0-0", "radius": 300.0, "turn": "L",
        "length": 78.540}]
PROFILE = [{"bvc_station": 1050.0, "bvc_elev": 240.0, "g_in_pct": 3.0,
            "g_out_pct": -2.0, "length_ft": 200.0, "evc_station": 1250.0,
            "evc_elev": 240.0 + 0.03 * 200.0 - 0.05 / 400.0 * 200.0 ** 2}]
RECT = [(-6.0, -3.0), (6.0, -3.0), (6.0, 0.0), (-6.0, 0.0)]

#: BIMForge's Element.voids (an IfcEarthworksCut voiding the ground) is
#: newer than some releases; the tests that build one skip without it
HAS_VOIDS = "voids" in getattr(Element, "__dataclass_fields__", {})


def _model(schema="IFC4X3_ADD2", profile=True):
    ctx = ProjectContext(name="Alignment Fixture", schema=schema, epsg=2226,
                         base_e=6_594_000.0, base_n=1_943_000.0, base_h=200.0,
                         guid_ns=uuid.UUID(int=332))
    al = Alignment(POB, RUN, name="ML")
    prof = Profile(PROFILE) if profile else None
    sw = SweptSection("deck", RECT, al, 1010.0, 1360.0, profile=prof,
                      origin=ctx)
    m = StructureModel("align", ctx)
    m.add(Element.from_geometry("deck", sw, ifc_class="IfcSlab",
                                quantities={"volume_cf": sw.volume_cf}))
    return m, al, prof


def _emit(tmp_path, m, name="a.ifc"):
    out = tmp_path / name
    emit_ifc(m, str(out))
    return out, ifcopenshell.open(str(out))
