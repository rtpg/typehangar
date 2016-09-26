# Stubs for django.template.exceptions (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class TemplateDoesNotExist(Exception):
    backend = ...  # type: Any
    tried = ...  # type: Any
    chain = ...  # type: Any
    def __init__(self, msg, tried: Optional[Any] = ..., backend: Optional[Any] = ..., chain: Optional[Any] = ...) -> None: ...

class TemplateSyntaxError(Exception): ...
