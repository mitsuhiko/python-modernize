# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.
from __future__ import absolute_import

from lib2to3.fixes import fix_filter
import libmodernize


class FixFilter(fix_filter.FixFilter):

    skip_on = "six.moves.filter"

    def transform(self, node, results):
        result = super(FixFilter, self).transform(node, results)
        if not libmodernize.is_listcomp(result):
            # Keep performance improvement from six.moves.filter in iterator
            # contexts on Python 2.7.
            libmodernize.touch_import(u'six.moves', u'filter', node)
        return result
