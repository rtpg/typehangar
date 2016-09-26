# Stubs for django.db.backends.base.creation (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

TEST_DATABASE_PREFIX = ...  # type: str

class BaseDatabaseCreation:
    connection = ...  # type: Any
    def __init__(self, connection) -> None: ...
    def create_test_db(self, verbosity: int = ..., autoclobber: bool = ..., serialize: bool = ..., keepdb: bool = ...): ...
    def set_as_test_mirror(self, primary_settings_dict): ...
    def serialize_db_to_string(self): ...
    def deserialize_db_from_string(self, data): ...
    def clone_test_db(self, number, verbosity: int = ..., autoclobber: bool = ..., keepdb: bool = ...): ...
    def get_test_db_clone_settings(self, number): ...
    def destroy_test_db(self, old_database_name: Optional[Any] = ..., verbosity: int = ..., keepdb: bool = ..., number: Optional[Any] = ...): ...
    def sql_table_creation_suffix(self): ...
    def test_db_signature(self): ...
