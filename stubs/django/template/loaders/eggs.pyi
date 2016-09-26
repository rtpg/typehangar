# Stubs for django.template.loaders.eggs (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.template import Origin
from .base import Loader as BaseLoader

resource_string = ...  # type: Any

class EggOrigin(Origin):
    app_name = ...  # type: Any
    pkg_name = ...  # type: Any
    def __init__(self, app_name, pkg_name, *args, **kwargs) -> None: ...

class Loader(BaseLoader):
    def __init__(self, engine) -> None: ...
    def get_contents(self, origin): ...
    def get_template_sources(self, template_name): ...
    def load_template_source(self, template_name, template_dirs: Optional[Any] = ...): ...
