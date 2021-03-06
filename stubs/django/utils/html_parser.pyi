# Stubs for django.utils.html_parser (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.utils.six.moves import html_parser as _html_parser
import _html_parser

current_version = ...  # type: Any
use_workaround = ...  # type: Any
HTMLParseError = ...  # type: Any

class HTMLParseError(Exception): ...

class HTMLParser(_html_parser.HTMLParser):
    def __init__(self, convert_charrefs: bool = ..., **kwargs) -> None: ...

HTMLParser = ...  # type: Any
tagfind = ...  # type: Any

class HTMLParser(_html_parser.HTMLParser):
    cdata_tag = ...  # type: Any
    def __init__(self) -> None: ...
    interesting = ...  # type: Any
    def set_cdata_mode(self, tag): ...
    def clear_cdata_mode(self): ...
    lasttag = ...  # type: Any
    def parse_starttag(self, i): ...
    def parse_endtag(self, i): ...
