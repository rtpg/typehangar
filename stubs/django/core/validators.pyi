# Stubs for django.core.validators (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.translation import ugettext_lazy as _

EMPTY_VALUES = ...  # type: Any

class RegexValidator:
    regex = ...  # type: str
    message = ...  # type: Any
    code = ...  # type: str
    inverse_match = ...  # type: bool
    flags = ...  # type: int
    def __init__(self, regex: Optional[Any] = ..., message: Optional[Any] = ..., code: Optional[Any] = ..., inverse_match: Optional[Any] = ..., flags: Optional[Any] = ...) -> None: ...
    def __call__(self, value): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...

class URLValidator(RegexValidator):
    ul = ...  # type: str
    ipv4_re = ...  # type: str
    ipv6_re = ...  # type: str
    hostname_re = ...  # type: Any
    domain_re = ...  # type: Any
    tld_re = ...  # type: Any
    host_re = ...  # type: Any
    regex = ...  # type: Any
    message = ...  # type: Any
    schemes = ...  # type: Any
    def __init__(self, schemes: Optional[Any] = ..., **kwargs) -> None: ...
    def __call__(self, value): ...

integer_validator = ...  # type: Any

def validate_integer(value): ...

class EmailValidator:
    message = ...  # type: Any
    code = ...  # type: str
    user_regex = ...  # type: Any
    domain_regex = ...  # type: Any
    literal_regex = ...  # type: Any
    domain_whitelist = ...  # type: Any
    def __init__(self, message: Optional[Any] = ..., code: Optional[Any] = ..., whitelist: Optional[Any] = ...) -> None: ...
    def __call__(self, value): ...
    def validate_domain_part(self, domain_part): ...
    def __eq__(self, other): ...

validate_email = ...  # type: Any
slug_re = ...  # type: Any
validate_slug = ...  # type: Any
slug_unicode_re = ...  # type: Any
validate_unicode_slug = ...  # type: Any
ipv4_re = ...  # type: Any
validate_ipv4_address = ...  # type: Any

def validate_ipv6_address(value): ...
def validate_ipv46_address(value): ...

ip_address_validator_map = ...  # type: Any

def ip_address_validators(protocol, unpack_ipv4): ...
def int_list_validator(sep: str = ..., message: Optional[Any] = ..., code: str = ...): ...

validate_comma_separated_integer_list = ...  # type: Any

class BaseValidator:
    compare = ...  # type: Any
    clean = ...  # type: Any
    message = ...  # type: Any
    code = ...  # type: str
    limit_value = ...  # type: Any
    def __init__(self, limit_value, message: Optional[Any] = ...) -> None: ...
    def __call__(self, value): ...
    def __eq__(self, other): ...

class MaxValueValidator(BaseValidator):
    compare = ...  # type: Any
    message = ...  # type: Any
    code = ...  # type: str

class MinValueValidator(BaseValidator):
    compare = ...  # type: Any
    message = ...  # type: Any
    code = ...  # type: str

class MinLengthValidator(BaseValidator):
    compare = ...  # type: Any
    clean = ...  # type: Any
    message = ...  # type: Any
    code = ...  # type: str

class MaxLengthValidator(BaseValidator):
    compare = ...  # type: Any
    clean = ...  # type: Any
    message = ...  # type: Any
    code = ...  # type: str

class DecimalValidator:
    messages = ...  # type: Any
    max_digits = ...  # type: Any
    decimal_places = ...  # type: Any
    def __init__(self, max_digits, decimal_places) -> None: ...
    def __call__(self, value): ...
    def __eq__(self, other): ...
