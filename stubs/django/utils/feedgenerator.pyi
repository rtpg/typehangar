# Stubs for django.utils.feedgenerator (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def rfc2822_date(date): ...
def rfc3339_date(date): ...
def get_tag_uri(url, date): ...

class SyndicationFeed:
    feed = ...  # type: Any
    items = ...  # type: Any
    def __init__(self, title, link, description, language: Optional[Any] = ..., author_email: Optional[Any] = ..., author_name: Optional[Any] = ..., author_link: Optional[Any] = ..., subtitle: Optional[Any] = ..., categories: Optional[Any] = ..., feed_url: Optional[Any] = ..., feed_copyright: Optional[Any] = ..., feed_guid: Optional[Any] = ..., ttl: Optional[Any] = ..., **kwargs) -> None: ...
    def add_item(self, title, link, description, author_email: Optional[Any] = ..., author_name: Optional[Any] = ..., author_link: Optional[Any] = ..., pubdate: Optional[Any] = ..., comments: Optional[Any] = ..., unique_id: Optional[Any] = ..., unique_id_is_permalink: Optional[Any] = ..., enclosure: Optional[Any] = ..., categories: Any = ..., item_copyright: Optional[Any] = ..., ttl: Optional[Any] = ..., updateddate: Optional[Any] = ..., enclosures: Optional[Any] = ..., **kwargs): ...
    def num_items(self): ...
    def root_attributes(self): ...
    def add_root_elements(self, handler): ...
    def item_attributes(self, item): ...
    def add_item_elements(self, handler, item): ...
    def write(self, outfile, encoding): ...
    def writeString(self, encoding): ...
    def latest_post_date(self): ...

class Enclosure:
    url = ...  # type: Any
    def __init__(self, url, length, mime_type) -> None: ...

class RssFeed(SyndicationFeed):
    content_type = ...  # type: str
    def write(self, outfile, encoding): ...
    def rss_attributes(self): ...
    def write_items(self, handler): ...
    def add_root_elements(self, handler): ...
    def endChannelElement(self, handler): ...
    @property
    def mime_type(self): ...

class RssUserland091Feed(RssFeed):
    def add_item_elements(self, handler, item): ...

class Rss201rev2Feed(RssFeed):
    def add_item_elements(self, handler, item): ...

class Atom1Feed(SyndicationFeed):
    content_type = ...  # type: str
    ns = ...  # type: str
    def write(self, outfile, encoding): ...
    def root_attributes(self): ...
    def add_root_elements(self, handler): ...
    def write_items(self, handler): ...
    def add_item_elements(self, handler, item): ...
    @property
    def mime_type(self): ...

DefaultFeed = ...  # type: Any
