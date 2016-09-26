# Stubs for django.core.serializers.xml_serializer (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any
import base
from xml.sax.expatreader import ExpatParser as _ExpatParser

class Serializer(base.Serializer):
    def indent(self, level): ...
    xml = ...  # type: Any
    def start_serialization(self): ...
    def end_serialization(self): ...
    def start_object(self, obj): ...
    def end_object(self, obj): ...
    def handle_field(self, obj, field): ...
    def handle_fk_field(self, obj, field): ...
    def handle_m2m_field(self, obj, field): ...

class Deserializer(base.Deserializer):
    event_stream = ...  # type: Any
    db = ...  # type: Any
    ignore = ...  # type: Any
    def __init__(self, stream_or_string, **options) -> None: ...
    def __next__(self): ...

def getInnerText(node): ...

class DefusedExpatParser(_ExpatParser):
    def __init__(self, *args, **kwargs) -> None: ...
    def start_doctype_decl(self, name, sysid, pubid, has_internal_subset): ...
    def entity_decl(self, name, is_parameter_entity, value, base, sysid, pubid, notation_name): ...
    def unparsed_entity_decl(self, name, base, sysid, pubid, notation_name): ...
    def external_entity_ref_handler(self, context, base, sysid, pubid): ...
    def reset(self): ...

class DefusedXmlException(ValueError): ...

class DTDForbidden(DefusedXmlException):
    name = ...  # type: Any
    sysid = ...  # type: Any
    pubid = ...  # type: Any
    def __init__(self, name, sysid, pubid) -> None: ...

class EntitiesForbidden(DefusedXmlException):
    name = ...  # type: Any
    value = ...  # type: Any
    base = ...  # type: Any
    sysid = ...  # type: Any
    pubid = ...  # type: Any
    notation_name = ...  # type: Any
    def __init__(self, name, value, base, sysid, pubid, notation_name) -> None: ...

class ExternalReferenceForbidden(DefusedXmlException):
    context = ...  # type: Any
    base = ...  # type: Any
    sysid = ...  # type: Any
    pubid = ...  # type: Any
    def __init__(self, context, base, sysid, pubid) -> None: ...
