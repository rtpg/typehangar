# Stubs for django.http.cookie (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import http_cookies

cookie_pickles_properly = ...  # type: Any
SimpleCookie = ...  # type: Any
Morsel = ...  # type: Any

class SimpleCookie(http_cookies.SimpleCookie):
    def __setitem__(self, key, value): ...
    def value_encode(self, val): ...
    bad_cookies = ...  # type: Any
    def load(self, rawdata): ...

def parse_cookie(cookie): ...
