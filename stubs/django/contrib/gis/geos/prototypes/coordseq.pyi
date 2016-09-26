# Stubs for django.contrib.gis.geos.prototypes.coordseq (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.contrib.gis.geos.libgeos import GEOSFuncFactory

def check_cs_op(result, func, cargs): ...
def check_cs_get(result, func, cargs): ...

class CsInt(GEOSFuncFactory):
    argtypes = ...  # type: Any
    restype = ...  # type: Any
    errcheck = ...  # type: Any

class CsOperation(GEOSFuncFactory):
    restype = ...  # type: Any
    errcheck = ...  # type: Any
    argtypes = ...  # type: Any
    def get_func(self, ordinate: bool = ..., get: bool = ...): ...

class CsOutput(GEOSFuncFactory):
    restype = ...  # type: Any
    argtypes = ...  # type: Any
    def get_func(self, argtypes): ...
    @staticmethod
    def errcheck(result, func, cargs): ...

cs_clone = ...  # type: Any
create_cs = ...  # type: Any
get_cs = ...  # type: Any
cs_getordinate = ...  # type: Any
cs_setordinate = ...  # type: Any
cs_getx = ...  # type: Any
cs_gety = ...  # type: Any
cs_getz = ...  # type: Any
cs_setx = ...  # type: Any
cs_sety = ...  # type: Any
cs_setz = ...  # type: Any
cs_getsize = ...  # type: Any
cs_getdims = ...  # type: Any
