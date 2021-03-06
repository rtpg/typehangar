# Stubs for django.contrib.auth.management.commands.createsuperuser (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.core.management.base import BaseCommand

class NotRunningInTTYException(Exception): ...

class Command(BaseCommand):
    help = ...  # type: str
    UserModel = ...  # type: Any
    username_field = ...  # type: Any
    def __init__(self, *args, **kwargs) -> None: ...
    def add_arguments(self, parser): ...
    stdin = ...  # type: Any
    def execute(self, *args, **options): ...
    def handle(self, *args, **options): ...
    def get_input_data(self, field, message, default: Optional[Any] = ...): ...
