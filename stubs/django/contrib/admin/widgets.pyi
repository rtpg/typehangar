# Stubs for django.contrib.admin.widgets (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import forms
from django.forms.widgets import RadioFieldRenderer
from django.utils.translation import ugettext as _

class FilteredSelectMultiple(forms.SelectMultiple):
    @property
    def media(self): ...
    verbose_name = ...  # type: Any
    is_stacked = ...  # type: Any
    def __init__(self, verbose_name, is_stacked, attrs: Optional[Any] = ..., choices: Any = ...) -> None: ...
    def render(self, name, value, attrs: Optional[Any] = ..., choices: Any = ...): ...

class AdminDateWidget(forms.DateInput):
    @property
    def media(self): ...
    def __init__(self, attrs: Optional[Any] = ..., format: Optional[Any] = ...) -> None: ...

class AdminTimeWidget(forms.TimeInput):
    @property
    def media(self): ...
    def __init__(self, attrs: Optional[Any] = ..., format: Optional[Any] = ...) -> None: ...

class AdminSplitDateTime(forms.SplitDateTimeWidget):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...
    def format_output(self, rendered_widgets): ...

class AdminRadioFieldRenderer(RadioFieldRenderer):
    def render(self): ...

class AdminRadioSelect(forms.RadioSelect):
    renderer = ...  # type: Any

class AdminFileWidget(forms.ClearableFileInput):
    template_with_initial = ...  # type: Any
    template_with_clear = ...  # type: Any

def url_params_from_lookup_dict(lookups): ...

class ForeignKeyRawIdWidget(forms.TextInput):
    rel = ...  # type: Any
    admin_site = ...  # type: Any
    db = ...  # type: Any
    def __init__(self, rel, admin_site, attrs: Optional[Any] = ..., using: Optional[Any] = ...) -> None: ...
    def render(self, name, value, attrs: Optional[Any] = ...): ...
    def base_url_parameters(self): ...
    def url_parameters(self): ...
    def label_for_value(self, value): ...

class ManyToManyRawIdWidget(ForeignKeyRawIdWidget):
    def render(self, name, value, attrs: Optional[Any] = ...): ...
    def url_parameters(self): ...
    def label_for_value(self, value): ...
    def value_from_datadict(self, data, files, name): ...

class RelatedFieldWidgetWrapper(forms.Widget):
    template = ...  # type: str
    needs_multipart_form = ...  # type: Any
    attrs = ...  # type: Any
    choices = ...  # type: Any
    widget = ...  # type: Any
    rel = ...  # type: Any
    can_add_related = ...  # type: Any
    can_change_related = ...  # type: Any
    can_delete_related = ...  # type: Any
    admin_site = ...  # type: Any
    def __init__(self, widget, rel, admin_site, can_add_related: Optional[Any] = ..., can_change_related: bool = ..., can_delete_related: bool = ...) -> None: ...
    def __deepcopy__(self, memo): ...
    @property
    def is_hidden(self): ...
    @property
    def media(self): ...
    def get_related_url(self, info, action, *args): ...
    def render(self, name, value, *args, **kwargs): ...
    def build_attrs(self, extra_attrs: Optional[Any] = ..., **kwargs): ...
    def value_from_datadict(self, data, files, name): ...
    def id_for_label(self, id_): ...

class AdminTextareaWidget(forms.Textarea):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...

class AdminTextInputWidget(forms.TextInput):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...

class AdminEmailInputWidget(forms.EmailInput):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...

class AdminURLFieldWidget(forms.URLInput):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...
    def render(self, name, value, attrs: Optional[Any] = ...): ...

class AdminIntegerFieldWidget(forms.TextInput):
    class_name = ...  # type: str
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...

class AdminBigIntegerFieldWidget(AdminIntegerFieldWidget):
    class_name = ...  # type: str

class AdminCommaSeparatedIntegerFieldWidget(forms.TextInput):
    def __init__(self, attrs: Optional[Any] = ...) -> None: ...