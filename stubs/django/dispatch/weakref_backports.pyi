# Stubs for django.dispatch.weakref_backports (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from weakref import ref

class WeakMethod(ref):
    def __new__(cls, meth, callback: Optional[Any] = ...): ...
    def __call__(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    __hash__ = ...  # type: Any