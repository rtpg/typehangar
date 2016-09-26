# Stubs for django.views.generic.detail (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.utils.translation import ugettext as _
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

class SingleObjectMixin(ContextMixin):
    model = ...  # type: Any
    queryset = ...  # type: Any
    slug_field = ...  # type: str
    context_object_name = ...  # type: Any
    slug_url_kwarg = ...  # type: str
    pk_url_kwarg = ...  # type: str
    query_pk_and_slug = ...  # type: bool
    def get_object(self, queryset: Optional[Any] = ...): ...
    def get_queryset(self): ...
    def get_slug_field(self): ...
    def get_context_object_name(self, obj): ...
    def get_context_data(self, **kwargs): ...

class BaseDetailView(SingleObjectMixin, View):
    object = ...  # type: Any
    def get(self, request, *args, **kwargs): ...

class SingleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_field = ...  # type: Any
    template_name_suffix = ...  # type: str
    def get_template_names(self): ...

class DetailView(SingleObjectTemplateResponseMixin, BaseDetailView): ...
