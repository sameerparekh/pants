# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).


python_library(
  name = 'build_graph',
  sources = globs('*.py'),
  dependencies = [
    '3rdparty/python:six',
    '3rdparty/python/twitter/commons:twitter.common.collections',
    'src/python/pants/backend/core:wrapped_globs',
    'src/python/pants/base:address',
    'src/python/pants/base:address_lookup_error',
    'src/python/pants/base:build_file',
    'src/python/pants/base:build_file_target_factory',
    'src/python/pants/base:build_environment',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:fingerprint_strategy',
    'src/python/pants/base:hash_utils',
    'src/python/pants/base:parse_context',
    'src/python/pants/base:payload',
    'src/python/pants/base:payload_field',
    'src/python/pants/base:source_root',
    'src/python/pants/option',
    'src/python/pants/subsystem',
    'src/python/pants/util:memo',
    'src/python/pants/util:meta',
  ]
)
