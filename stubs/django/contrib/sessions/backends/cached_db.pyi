# Stubs for django.contrib.sessions.backends.cached_db (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.contrib.sessions.backends.db import SessionStore as DBStore

KEY_PREFIX = ...  # type: str

class SessionStore(DBStore):
    cache_key_prefix = ...  # type: Any
    def __init__(self, session_key: Optional[Any] = ...) -> None: ...
    @property
    def cache_key(self): ...
    def load(self): ...
    def exists(self, session_key): ...
    def save(self, must_create: bool = ...): ...
    def delete(self, session_key: Optional[Any] = ...): ...
    def flush(self): ...
