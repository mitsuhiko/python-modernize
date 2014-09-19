# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from lib2to3 import fixer_util
from lib2to3.fixes import fix_map


class FixMap(fix_map.FixMap):

    skip_on = "six.moves.map"

    def transform(self, node, results):
        result = super(FixMap, self).transform(node, results)
        # Always use the import even if no change is required so as to have
        # improved performance in iterator contexts even on Python 2.7.
        fixer_util.touch_import(u'six.moves', u'map', node)
        return result
