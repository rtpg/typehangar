# Stubs for django.template.smartif (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class TokenBase:
    id = ...  # type: Any
    value = ...  # type: Any
    first = ...  # type: Any
    second = ...  # type: Any
    def nud(self, parser): ...
    def led(self, left, parser): ...
    def display(self): ...

def infix(bp, func): ...
def prefix(bp, func): ...

OPERATORS = ...  # type: Any

class Literal(TokenBase):
    id = ...  # type: str
    lbp = ...  # type: int
    value = ...  # type: Any
    def __init__(self, value) -> None: ...
    def display(self): ...
    def nud(self, parser): ...
    def eval(self, context): ...

class EndToken(TokenBase):
    lbp = ...  # type: int
    def nud(self, parser): ...

EndToken = ...  # type: Any

class IfParser:
    error_class = ...  # type: Any
    tokens = ...  # type: Any
    pos = ...  # type: int
    current_token = ...  # type: Any
    def __init__(self, tokens) -> None: ...
    def translate_token(self, token): ...
    def next_token(self): ...
    def parse(self): ...
    def expression(self, rbp: int = ...): ...
    def create_var(self, value): ...
