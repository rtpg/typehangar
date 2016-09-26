# Stubs for django.db.models.sql.query (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class RawQuery:
    params = ...  # type: Any
    sql = ...  # type: Any
    using = ...  # type: Any
    cursor = ...  # type: Any
    extra_select = ...  # type: Any
    annotation_select = ...  # type: Any
    context = ...  # type: Any
    def __init__(self, sql, using, params: Optional[Any] = ..., context: Optional[Any] = ...) -> None: ...
    def clone(self, using): ...
    def get_columns(self): ...
    def __iter__(self): ...
    @property
    def params_type(self): ...

class Query:
    alias_prefix = ...  # type: str
    subq_aliases = ...  # type: Any
    query_terms = ...  # type: Any
    compiler = ...  # type: str
    model = ...  # type: Any
    alias_refcount = ...  # type: Any
    alias_map = ...  # type: Any
    external_aliases = ...  # type: Any
    table_map = ...  # type: Any
    default_cols = ...  # type: bool
    default_ordering = ...  # type: bool
    standard_ordering = ...  # type: bool
    used_aliases = ...  # type: Any
    filter_is_sticky = ...  # type: bool
    select = ...  # type: Any
    tables = ...  # type: Any
    where = ...  # type: Any
    where_class = ...  # type: Any
    group_by = ...  # type: Any
    order_by = ...  # type: Any
    distinct = ...  # type: bool
    distinct_fields = ...  # type: Any
    select_for_update = ...  # type: bool
    select_for_update_nowait = ...  # type: bool
    select_related = ...  # type: bool
    max_depth = ...  # type: int
    values_select = ...  # type: Any
    annotation_select_mask = ...  # type: Any
    extra_select_mask = ...  # type: Any
    extra_tables = ...  # type: Any
    extra_order_by = ...  # type: Any
    deferred_loading = ...  # type: Any
    context = ...  # type: Any
    def __init__(self, model, where: Any = ...) -> None: ...
    @property
    def extra(self): ...
    @property
    def annotations(self): ...
    @property
    def aggregates(self): ...
    def sql_with_params(self): ...
    def __deepcopy__(self, memo): ...
    def get_compiler(self, using: Optional[Any] = ..., connection: Optional[Any] = ...): ...
    def get_meta(self): ...
    def clone(self, klass: Optional[Any] = ..., memo: Optional[Any] = ..., **kwargs): ...
    def add_context(self, key, value): ...
    def get_context(self, key, default: Optional[Any] = ...): ...
    def relabeled_clone(self, change_map): ...
    def rewrite_cols(self, annotation, col_cnt): ...
    def get_aggregation(self, using, added_aggregate_names): ...
    def get_count(self, using): ...
    def has_filters(self): ...
    def has_results(self, using): ...
    def combine(self, rhs, connector): ...
    def deferred_to_data(self, target, callback): ...
    def table_alias(self, table_name, create: bool = ...): ...
    def ref_alias(self, alias): ...
    def unref_alias(self, alias, amount: int = ...): ...
    def promote_joins(self, aliases): ...
    def demote_joins(self, aliases): ...
    def reset_refcounts(self, to_counts): ...
    def change_aliases(self, change_map): ...
    def bump_prefix(self, outer_query): ...
    def get_initial_alias(self): ...
    def count_active_tables(self): ...
    def join(self, join, reuse: Optional[Any] = ...): ...
    def join_parent_model(self, opts, model, alias, seen): ...
    def add_aggregate(self, aggregate, model, alias, is_summary): ...
    def add_annotation(self, annotation, alias, is_summary: bool = ...): ...
    def prepare_lookup_value(self, value, lookups, can_reuse, allow_joins: bool = ...): ...
    def solve_lookup_type(self, lookup): ...
    def check_query_object_type(self, value, opts, field): ...
    def check_related_objects(self, field, value, opts): ...
    def build_lookup(self, lookups, lhs, rhs): ...
    def try_transform(self, lhs, name, rest_of_lookups): ...
    def build_filter(self, filter_expr, branch_negated: bool = ..., current_negated: bool = ..., can_reuse: Optional[Any] = ..., connector: Any = ..., allow_joins: bool = ..., split_subq: bool = ...): ...
    def add_filter(self, filter_clause): ...
    def add_q(self, q_object): ...
    def names_to_path(self, names, opts, allow_many: bool = ..., fail_on_missing: bool = ...): ...
    def setup_joins(self, names, opts, alias, can_reuse: Optional[Any] = ..., allow_many: bool = ...): ...
    def trim_joins(self, targets, joins, path): ...
    def resolve_ref(self, name, allow_joins: bool = ..., reuse: Optional[Any] = ..., summarize: bool = ...): ...
    def split_exclude(self, filter_expr, prefix, can_reuse, names_with_path): ...
    def set_empty(self): ...
    def is_empty(self): ...
    high_mark = ...  # type: Any
    low_mark = ...  # type: Any
    def set_limits(self, low: Optional[Any] = ..., high: Optional[Any] = ...): ...
    def clear_limits(self): ...
    def can_filter(self): ...
    def clear_select_clause(self): ...
    def clear_select_fields(self): ...
    def add_select(self, col): ...
    def set_select(self, cols): ...
    def add_distinct_fields(self, *field_names): ...
    def add_fields(self, field_names, allow_m2m: bool = ...): ...
    def add_ordering(self, *ordering): ...
    def clear_ordering(self, force_empty): ...
    def set_group_by(self): ...
    def add_select_related(self, fields): ...
    def add_extra(self, select, select_params, where, params, tables, order_by): ...
    def clear_deferred_loading(self): ...
    def add_deferred_loading(self, field_names): ...
    def add_immediate_loading(self, field_names): ...
    def get_loaded_field_names(self): ...
    def get_loaded_field_names_cb(self, target, model, fields): ...
    def set_aggregate_mask(self, names): ...
    def set_annotation_mask(self, names): ...
    def append_aggregate_mask(self, names): ...
    def append_annotation_mask(self, names): ...
    def set_extra_mask(self, names): ...
    @property
    def annotation_select(self): ...
    @property
    def aggregate_select(self): ...
    @property
    def extra_select(self): ...
    def trim_start(self, names_with_path): ...
    def is_nullable(self, field): ...

class JoinPromoter:
    connector = ...  # type: Any
    negated = ...  # type: Any
    effective_connector = ...  # type: Any
    num_children = ...  # type: Any
    votes = ...  # type: Any
    def __init__(self, connector, num_children, negated) -> None: ...
    def add_votes(self, votes): ...
    def update_join_types(self, query): ...
