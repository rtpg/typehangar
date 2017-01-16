from datetime import date
from datetime import datetime
from typing import Any
from typing import Callable, TypeVar, Generic

from decimal import Decimal
from django.core.files import File
from typing import Type

CASCADE = ...  # type: Any
PROTECT = ...  # type: Any
SET_NULL = ...  # type: Any

class F:
    def __init__(self, expr:str ): ...
class Q:
    def __init__(self, expr:Any ): ...
class Count:
    def __init__(self, expr:Any ): ...
class Sum:
    def __init__(self, expr:Any ): ...

T = TypeVar('T')

class Field(Generic[T]):
    # hack to get field constructors to properly bind
    # on model instances
    def __call__(self, *args, **kwargs) -> T: ...


class QuerySet(Generic[T]):
    def as_manager(self) -> 'Manager[T]': ...


class Manager(Generic[T]):

    def create(self, **kwargs) -> T: ...

    def all(self) -> QuerySet[T]: ...

    def filter(self, **kwargs) -> QuerySet[T]: ...

    def from_queryset(self, queryset: Type[QuerySet[T]]) -> 'Type[Manager[T]]': ...

class Model(Generic[T]):

    objects = ... # type: Manager['self']
    # @property
    # def objects(self:T) -> Manager[T]: ...

    # allow any init for now
    def __init__(self, **kwargs): ...

    def save(self): ...

    def delete(self): ...


BooleanField = ...  # type: Field[bool]
NullBooleanField = ...  # type: Field[bool]
CharField = ...  # type: Field[str]
DateField = ...  # type: Field[date]
DateTimeField = ...  # type: Field[datetime]
DecimalField = ... # type: Field[Decimal]
EmailField = ...  # type: Field[str]
FileField = ...  # type: Field[File]
IntegerField = ...  # type: Field[int]
PositiveIntegerField = ...  # type: Field[int]
PositiveSmallIntegerField = ...  # type: Field[int]
SlugField = ...  # type: Field[str]
TextField = ...  # type: Field[str]
URLField = ... # type: Field[str]

OneToOneField = ...  # type: Field[Any]
ManyToManyField = ...  # type: Field[Any]
ForeignKey = ...  # type: Callable[Type[T], ..., T]

TEXTFIELD_MAX_LENGTH = ...
