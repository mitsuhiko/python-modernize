# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from lib2to3 import fixer_util
from lib2to3.fixes import fix_filter


class FixFilter(fix_filter.FixFilter):

    skip_on = "six.moves.filter"

    def transform(self, node, results):
        result = super(FixFilter, self).transform(node, results)
        # Keep performance improvement from six.moves.filter in iterator
        # contexts on Python 2.7.
        fixer_util.touch_import(u'six.moves', u'filter', node)
        return result
