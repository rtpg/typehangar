# Stubs for django.utils.html (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from .html_parser import HTMLParseError as HTMLParseError, HTMLParser as HTMLParser

TRAILING_PUNCTUATION = ...  # type: Any
WRAPPING_PUNCTUATION = ...  # type: Any
DOTS = ...  # type: Any
unencoded_ampersands_re = ...  # type: Any
word_split_re = ...  # type: Any
simple_url_re = ...  # type: Any
simple_url_2_re = ...  # type: Any
simple_email_re = ...  # type: Any
link_target_attribute_re = ...  # type: Any
html_gunk_re = ...  # type: Any
hard_coded_bullets_re = ...  # type: Any
trailing_empty_content_re = ...  # type: Any

def escape(text): ...

escape = ...  # type: Any

def escapejs(value): ...

escapejs = ...  # type: Any

def conditional_escape(text): ...
def format_html(format_string, *args, **kwargs): ...
def format_html_join(sep, format_string, args_generator): ...
def linebreaks(value, autoescape: bool = ...): ...

linebreaks = ...  # type: Any

class MLStripper(HTMLParser):
    fed = ...  # type: Any
    def __init__(self) -> None: ...
    def handle_data(self, d): ...
    def handle_entityref(self, name): ...
    def handle_charref(self, name): ...
    def get_data(self): ...

def strip_tags(value): ...

strip_tags = ...  # type: Any

def remove_tags(html, tags): ...

remove_tags = ...  # type: Any

def strip_spaces_between_tags(value): ...

strip_spaces_between_tags = ...  # type: Any

def strip_entities(value): ...

strip_entities = ...  # type: Any

def smart_urlquote(url): ...
def urlize(text, trim_url_limit: Optional[Any] = ..., nofollow: bool = ..., autoescape: bool = ...): ...

urlize = ...  # type: Any

def avoid_wrapping(value): ...
def html_safe(klass): ...
