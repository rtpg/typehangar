# Stubs for django.core.management.commands.sqlsequencereset (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from django.core.management.base import AppCommand

class Command(AppCommand):
    help = ...  # type: str
    output_transaction = ...  # type: bool
    def add_arguments(self, parser): ...
    def handle_app_config(self, app_config, **options): ...
