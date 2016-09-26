# Stubs for django.contrib.admindocs.utils (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

docutils_is_available = ...  # type: bool

def trim_docstring(docstring): ...
def parse_docstring(docstring): ...
def parse_rst(text, default_reference_context, thing_being_parsed: Optional[Any] = ...): ...

ROLES = ...  # type: Any

def create_reference_role(rolename, urlbase): ...
def default_reference_role(name, rawtext, text, lineno, inliner, options: Optional[Any] = ..., content: Optional[Any] = ...): ...
