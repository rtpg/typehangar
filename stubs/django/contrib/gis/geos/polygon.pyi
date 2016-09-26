# Stubs for django.contrib.gis.geos.polygon (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.gis.geos import prototypes as capi
from django.contrib.gis.geos.geometry import GEOSGeometry

class Polygon(GEOSGeometry):
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    @classmethod
    def from_bbox(cls, bbox): ...
    @property
    def num_interior_rings(self): ...
    exterior_ring = ...  # type: Any
    shell = ...  # type: Any
    @property
    def tuple(self): ...
    coords = ...  # type: Any
    @property
    def kml(self): ...
