# Stubs for django.db.models.fields.related (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.translation import ugettext_lazy as _
from .related_descriptors import ForwardManyToOneDescriptor as ForwardManyToOneDescriptor, ManyToManyDescriptor as ManyToManyDescriptor, ReverseManyToOneDescriptor as ReverseManyToOneDescriptor, ReverseOneToOneDescriptor as ReverseOneToOneDescriptor
from .related_lookups import RelatedExact as RelatedExact, RelatedGreaterThan as RelatedGreaterThan, RelatedGreaterThanOrEqual as RelatedGreaterThanOrEqual, RelatedIn as RelatedIn, RelatedIsNull as RelatedIsNull, RelatedLessThan as RelatedLessThan, RelatedLessThanOrEqual as RelatedLessThanOrEqual
from .reverse_related import ForeignObjectRel as ForeignObjectRel, ManyToManyRel as ManyToManyRel, ManyToOneRel as ManyToOneRel, OneToOneRel as OneToOneRel

RECURSIVE_RELATIONSHIP_CONSTANT = ...  # type: str

def resolve_relation(scope_model, relation): ...
def lazy_related_operation(function, model, *related_models, **kwargs): ...
def add_lazy_relation(cls, field, relation, operation): ...

class RelatedField(Field):
    one_to_many = ...  # type: bool
    one_to_one = ...  # type: bool
    many_to_many = ...  # type: bool
    many_to_one = ...  # type: bool
    def related_model(self): ...
    def check(self, **kwargs): ...
    def db_type(self, connection): ...
    opts = ...  # type: Any
    def contribute_to_class(self, cls, name, virtual_only: bool = ...): ...
    def get_forward_related_filter(self, obj): ...
    def get_reverse_related_filter(self, obj): ...
    @property
    def swappable_setting(self): ...
    name = ...  # type: Any
    verbose_name = ...  # type: Any
    def set_attributes_from_rel(self): ...
    @property
    def related(self): ...
    def do_related_class(self, other, cls): ...
    def get_limit_choices_to(self): ...
    def formfield(self, **kwargs): ...
    def related_query_name(self): ...
    @property
    def target_field(self): ...

class ForeignObject(RelatedField):
    many_to_many = ...  # type: bool
    many_to_one = ...  # type: bool
    one_to_many = ...  # type: bool
    one_to_one = ...  # type: bool
    requires_unique_target = ...  # type: bool
    related_accessor_class = ...  # type: Any
    rel_class = ...  # type: Any
    from_fields = ...  # type: Any
    to_fields = ...  # type: Any
    swappable = ...  # type: Any
    def __init__(self, to, on_delete, from_fields, to_fields, rel: Optional[Any] = ..., related_name: Optional[Any] = ..., related_query_name: Optional[Any] = ..., limit_choices_to: Optional[Any] = ..., parent_link: bool = ..., swappable: bool = ..., **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def resolve_related_fields(self): ...
    @property
    def related_fields(self): ...
    @property
    def reverse_related_fields(self): ...
    @property
    def local_related_fields(self): ...
    @property
    def foreign_related_fields(self): ...
    def get_local_related_value(self, instance): ...
    def get_foreign_related_value(self, instance): ...
    @staticmethod
    def get_instance_value_for_fields(instance, fields): ...
    def get_attname_column(self): ...
    def get_joining_columns(self, reverse_join: bool = ...): ...
    def get_reverse_joining_columns(self): ...
    def get_extra_descriptor_filter(self, instance): ...
    def get_extra_restriction(self, where_class, alias, related_alias): ...
    def get_path_info(self): ...
    def get_reverse_path_info(self): ...
    def get_lookup(self, lookup_name): ...
    def get_transform(self, *args, **kwargs): ...
    @property
    def attnames(self): ...
    def get_defaults(self): ...
    def contribute_to_class(self, cls, name, virtual_only: bool = ...): ...
    def contribute_to_related_class(self, cls, related): ...

class ForeignKey(ForeignObject):
    many_to_many = ...  # type: bool
    many_to_one = ...  # type: bool
    one_to_many = ...  # type: bool
    one_to_one = ...  # type: bool
    rel_class = ...  # type: Any
    empty_strings_allowed = ...  # type: bool
    default_error_messages = ...  # type: Any
    description = ...  # type: Any
    db_constraint = ...  # type: Any
    def __init__(self, to, on_delete: Optional[Any] = ..., related_name: Optional[Any] = ..., related_query_name: Optional[Any] = ..., limit_choices_to: Optional[Any] = ..., parent_link: bool = ..., to_field: Optional[Any] = ..., db_constraint: bool = ..., **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    @property
    def target_field(self): ...
    def get_reverse_path_info(self): ...
    def validate(self, value, model_instance): ...
    def get_attname(self): ...
    def get_attname_column(self): ...
    def get_default(self): ...
    def get_db_prep_save(self, value, connection): ...
    def get_db_prep_value(self, value, connection, prepared: bool = ...): ...
    def value_to_string(self, obj): ...
    def contribute_to_related_class(self, cls, related): ...
    def formfield(self, **kwargs): ...
    def db_type(self, connection): ...
    def db_parameters(self, connection): ...
    def convert_empty_strings(self, value, expression, connection, context): ...
    def get_db_converters(self, connection): ...
    def get_col(self, alias, output_field: Optional[Any] = ...): ...

class OneToOneField(ForeignKey):
    many_to_many = ...  # type: bool
    many_to_one = ...  # type: bool
    one_to_many = ...  # type: bool
    one_to_one = ...  # type: bool
    related_accessor_class = ...  # type: Any
    rel_class = ...  # type: Any
    description = ...  # type: Any
    def __init__(self, to, on_delete: Optional[Any] = ..., to_field: Optional[Any] = ..., **kwargs) -> None: ...
    def deconstruct(self): ...
    def formfield(self, **kwargs): ...
    def save_form_data(self, instance, data): ...

def create_many_to_many_intermediary_model(field, klass): ...

class ManyToManyField(RelatedField):
    many_to_many = ...  # type: bool
    many_to_one = ...  # type: bool
    one_to_many = ...  # type: bool
    one_to_one = ...  # type: bool
    rel_class = ...  # type: Any
    description = ...  # type: Any
    has_null_arg = ...  # type: Any
    db_table = ...  # type: Any
    swappable = ...  # type: Any
    def __init__(self, to, related_name: Optional[Any] = ..., related_query_name: Optional[Any] = ..., limit_choices_to: Optional[Any] = ..., symmetrical: Optional[Any] = ..., through: Optional[Any] = ..., through_fields: Optional[Any] = ..., db_constraint: bool = ..., db_table: Optional[Any] = ..., swappable: bool = ..., **kwargs) -> None: ...
    def check(self, **kwargs): ...
    def deconstruct(self): ...
    def get_path_info(self): ...
    def get_reverse_path_info(self): ...
    def get_choices_default(self): ...
    def value_to_string(self, obj): ...
    m2m_db_table = ...  # type: Any
    def contribute_to_class(self, cls, name, **kwargs): ...
    m2m_column_name = ...  # type: Any
    m2m_reverse_name = ...  # type: Any
    m2m_field_name = ...  # type: Any
    m2m_reverse_field_name = ...  # type: Any
    m2m_target_field_name = ...  # type: Any
    m2m_reverse_target_field_name = ...  # type: Any
    def contribute_to_related_class(self, cls, related): ...
    def set_attributes_from_rel(self): ...
    def value_from_object(self, obj): ...
    def save_form_data(self, instance, data): ...
    def formfield(self, **kwargs): ...
    def db_type(self, connection): ...
    def db_parameters(self, connection): ...
