# Stubs for django.utils.decorators (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from contextlib import ContextDecorator

from typing import Any, Optional

# actually derived from classmethod but mypy doesn't like this so
# deriving from object for now
class classonlymethod(object):
    def __get__(self, instance, owner): ...

def method_decorator(decorator, name: str = ...): ...
def decorator_from_middleware_with_args(middleware_class): ...
def decorator_from_middleware(middleware_class): ...
def available_attrs(fn): ...
def make_middleware_decorator(middleware_class): ...

class classproperty:
    fget = ...  # type: Any
    def __init__(self, method: Optional[Any] = ...) -> None: ...
    def __get__(self, instance, owner): ...
    def getter(self, method): ...
