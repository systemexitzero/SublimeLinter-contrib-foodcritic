#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sheehy, Justin
# Copyright (c) 2015 Sheehy, Justin
#
# License: MIT
#

"""This module exports the Foodcritic plugin class."""

from SublimeLinter.lint import RubyLinter, util


class Foodcritic(RubyLinter):

    """Provides an interface to foodcritic."""

    syntax = ('ruby')
    cmd = 'foodcritic'
    executable = None
    version_args = '--version'
    version_re = r'\b(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 2.0'
    regex = (
        r'FC(?P<error>\d+): (?P<message>.+): (?P<file>.+):(?P<line>\d+)'
    )
    multiline = False
    line_col_base = (1, 1)
    tempfile_suffix = "-"
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*#'

