# coding=utf-8
# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import (absolute_import, division, generators, nested_scopes, print_function,
                        unicode_literals, with_statement)

from abc import abstractmethod

from pants.util.timeout import Timeout


class TestTaskMixin(object):
  """A mixin to combine with test runner tasks.
  """

  @classmethod
  def register_options(cls, register):
    super(TestTaskMixin, cls).register_options(register)
    register('--skip', action='store_true', help='Skip running tests.')
    register('--timeouts', action='store_true', default=True,
             help='Enable test timeouts')
    register('--default-timeout', action='store', default=0, type=int,
             help='The default timeout for a test if timeout is not set in BUILD')

  def execute(self):
    """Run the task
    """

    if not self.get_options().skip:
      targets = self._get_targets()
      self._validate_targets(targets)
      timeout = self._timeout_for_targets(targets)
      with Timeout(timeout):
        self._execute(targets)
      
  def _timeout_for_targets(self, targets):
    timeouts = [target.timeout for target in targets]
    if 0 in timeouts or None in timeouts:
      timeout = None
    else:
      timeout = sum(timeouts)

    if self.get_options().timeouts:
      if not timeout:
        return self.get_options().default_timeout
      else:
        return timeout
    else:
      return None
    
  @abstractmethod
  def _get_targets(self):
    """Returns the targets that are relevant test targets
    """

  @abstractmethod
  def _validate_targets(self, targets):
    """Ensures that these targets are valid and should be run

    :param targets: list of the targets to validate
    """

  @abstractmethod
  def _execute(self, targets):
    """Actually goes ahead and runs the tests for the targets

    :param targets: list of the targets whose tests are to be run
    """
