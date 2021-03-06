# Stubs for django.db.backends.oracle.schema (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.db.backends.base.schema import BaseDatabaseSchemaEditor

class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_create_column = ...  # type: str
    sql_alter_column_type = ...  # type: str
    sql_alter_column_null = ...  # type: str
    sql_alter_column_not_null = ...  # type: str
    sql_alter_column_default = ...  # type: str
    sql_alter_column_no_default = ...  # type: str
    sql_delete_column = ...  # type: str
    sql_delete_table = ...  # type: str
    def quote_value(self, value): ...
    def delete_model(self, model): ...
    def alter_field(self, model, old_field, new_field, strict: bool = ...): ...
    def normalize_name(self, name): ...
    def prepare_default(self, value): ...
