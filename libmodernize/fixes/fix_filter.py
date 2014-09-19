# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.
from __future__ import absolute_import

from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, in_special_context
from libmodernize import touch_import


class FixFilter(fixer_base.ConditionalFix):

    BM_compatible = True
    order = "pre"
    skip_on = "six.moves.filter"

    PATTERN = """
    power< 'filter'
        trailer< '('
            arglist< (
                not(argument<any '=' any>) any ','
                not(argument<any '=' any>) any
            ) >
        ')' >
    >
    """

    def transform(self, node, results):
        if self.should_skip(node):
            # Make the fixer idempotent - if six.moves.filter is already imported,
            # skip it. should_skip() caches the state the first time we check,
            # so it doesn't skip after *we've* added the six.moves import.
            return

        touch_import(u'six.moves', u'filter', node)
        if in_special_context(node):
            # The node is somewhere where it only needs to be an iterator,
            # e.g. a for loop - don't wrap in list()
            return

        new = node.clone()
        new.prefix = ""
        new = Call(Name("list"), [new])
        new.prefix = node.prefix
        return new
