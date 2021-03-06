# Stubs for django.contrib.gis.db.backends.spatialite.schema (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.db.backends.sqlite3.schema import DatabaseSchemaEditor

class SpatialiteSchemaEditor(DatabaseSchemaEditor):
    sql_add_geometry_column = ...  # type: str
    sql_add_spatial_index = ...  # type: str
    sql_drop_spatial_index = ...  # type: str
    sql_remove_geometry_metadata = ...  # type: str
    sql_discard_geometry_columns = ...  # type: str
    sql_update_geometry_columns = ...  # type: str
    geometry_tables = ...  # type: Any
    geometry_sql = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def geo_quote_name(self, name): ...
    def column_sql(self, model, field, include_default: bool = ...): ...
    def remove_geometry_metadata(self, model, field): ...
    def create_model(self, model): ...
    def delete_model(self, model, **kwargs): ...
    def add_field(self, model, field): ...
    def remove_field(self, model, field): ...
    def alter_db_table(self, model, old_db_table, new_db_table): ...
