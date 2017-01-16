# Stubs for django.db.models.manager (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

from django.db.models.query import QuerySet


def ensure_default_manager(cls): ...

class BaseManager:
    creation_counter = ...  # type: int
    use_in_migrations = ...  # type: bool
    def __new__(cls, *args, **kwargs): ...
    model = ...  # type: Any
    name = ...  # type: Any
    def __init__(self) -> None: ...
    def deconstruct(self): ...
    def check(self, **kwargs): ...
    @classmethod
    def from_queryset(cls, queryset_class, class_name: Optional[Any] = ...): ...
    def contribute_to_class(self, model, name): ...
    def db_manager(self, using: Optional[Any] = ..., hints: Optional[Any] = ...): ...
    @property
    def db(self): ...
    def get_queryset(self): ...
    def all(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __hash__(self): ...

# bit hacky, QuerySet methods get pulled into manager, but only in a very specific fashion
# missing (for example) iterators.
class Manager(BaseManager.from_queryset(QuerySet)): ...

class ManagerDescriptor:
    manager = ...  # type: Any
    def __init__(self, manager) -> None: ...
    def __get__(self, instance, type: Optional[Any] = ...): ...

class AbstractManagerDescriptor:
    model = ...  # type: Any
    def __init__(self, model) -> None: ...
    def __get__(self, instance, type: Optional[Any] = ...): ...

class SwappedManagerDescriptor:
    model = ...  # type: Any
    def __init__(self, model) -> None: ...
    def __get__(self, instance, type: Optional[Any] = ...): ...

class EmptyManager(Manager):
    model = ...  # type: Any
    def __init__(self, model) -> None: ...
    def get_queryset(self): ...
