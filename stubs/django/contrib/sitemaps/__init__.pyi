# Stubs for django.contrib.sitemaps (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from django.apps import apps as django_apps

PING_URL = ...  # type: str

class SitemapNotFound(Exception): ...

def ping_google(sitemap_url: Optional[Any] = ..., ping_url: Any = ...): ...

class Sitemap:
    limit = ...  # type: int
    protocol = ...  # type: Any
    def items(self): ...
    def location(self, obj): ...
    paginator = ...  # type: Any
    def get_urls(self, page: int = ..., site: Optional[Any] = ..., protocol: Optional[Any] = ...): ...

class GenericSitemap(Sitemap):
    priority = ...  # type: Any
    changefreq = ...  # type: Any
    queryset = ...  # type: Any
    date_field = ...  # type: Any
    def __init__(self, info_dict, priority: Optional[Any] = ..., changefreq: Optional[Any] = ...) -> None: ...
    def items(self): ...
    def lastmod(self, item): ...

default_app_config = ...  # type: str
