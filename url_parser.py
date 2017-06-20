from urllib.parse import urlparse, parse_qs, urlencode, ParseResult
from utils import merge
from copy import copy
from functools import partial


def update_query(self, query_dict):
  new_query = urlencode(merge(parse_qs(self.query), query_dict))

  return ParseResult(**merge(self._asdict(), {'query': new_query}))

ParseResult.update_query = update_query
