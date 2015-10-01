# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

import re


TIMEOUT_TAG = 'timeout'

class TestTargetMixin(object):
  """Mix this in with test targets to get timeout and other test-specific target parameters
  """

  @classmethod
  def create(cls, parse_context, timeout = None, **kwargs):
    if timeout is not None:
      timeout_tag = "%s: %d" % (TIMEOUT_TAG, timeout)
      if 'tags' in kwargs:
        kwargs['tags'].append(timeout_tag)
      else:
        kwargs['tags'] = [timeout_tag]

    parse_context.create_object(cls, type_alias=cls.alias(), **kwargs)

  @property
  def timeout(self):
    p = re.compile(TIMEOUT_TAG + r': ([0-9]+)$')
    matches = [m.groups()[0] for m in map(p.match, self.tags) if m and m.groups()]
    return matches[0] if matches else None
