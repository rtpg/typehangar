# Stubs for django.template.backends.django (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .base import BaseEngine as BaseEngine

class DjangoTemplates(BaseEngine):
    app_dirname = ...  # type: str
    engine = ...  # type: Any
    def __init__(self, params) -> None: ...
    def from_string(self, template_code): ...
    def get_template(self, template_name, dirs: Any = ...): ...
    def get_templatetag_libraries(self, custom_libraries): ...

class Template:
    template = ...  # type: Any
    backend = ...  # type: Any
    def __init__(self, template, backend) -> None: ...
    @property
    def origin(self): ...
    def render(self, context: Optional[Any] = ..., request: Optional[Any] = ...): ...

def copy_exception(exc, backend: Optional[Any] = ...): ...
def reraise(exc, backend): ...
def get_installed_libraries(): ...
def get_package_libraries(pkg): ...
