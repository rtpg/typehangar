# Stubs for django.utils.translation.trans_null (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def ngettext(singular, plural, number): ...

ngettext_lazy = ...  # type: Any

def ungettext(singular, plural, number): ...
def pgettext(context, message): ...
def npgettext(context, singular, plural, number): ...

activate = ...  # type: Any
deactivate = ...  # type: Any
deactivate_all = ...  # type: Any
get_language = ...  # type: Any
get_language_bidi = ...  # type: Any
check_for_language = ...  # type: Any

def gettext(message): ...
def ugettext(message): ...

gettext_noop = ...  # type: Any

gettext_lazy = ...  # type: Any
def to_locale(language): ...
def get_language_from_request(request, check_path: bool = ...): ...
def get_language_from_path(request): ...
