# Stubs for django.contrib.admin.templatetags.admin_list (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
from django.utils.translation import ugettext as _

register = ...  # type: Any
DOT = ...  # type: str

def paginator_number(cl, i): ...
def pagination(cl): ...
def result_headers(cl): ...
def items_for_result(cl, result, form): ...

class ResultList(list):
    form = ...  # type: Any
    def __init__(self, form, *items) -> None: ...

def results(cl): ...
def result_hidden_fields(cl): ...
def result_list(cl): ...
def date_hierarchy(cl): ...
def search_form(cl): ...
def admin_list_filter(cl, spec): ...
def admin_actions(context): ...
