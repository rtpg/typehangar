# Stubs for django.templatetags.l10n (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.template import Node

register = ...  # type: Any

def localize(value): ...
def unlocalize(value): ...

class LocalizeNode(Node):
    nodelist = ...  # type: Any
    use_l10n = ...  # type: Any
    def __init__(self, nodelist, use_l10n) -> None: ...
    def render(self, context): ...

def localize_tag(parser, token): ...
