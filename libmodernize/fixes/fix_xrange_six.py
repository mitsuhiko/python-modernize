# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, touch_import
from lib2to3.fixes import fix_xrange


class FixXrangeSix(fixer_base.ConditionalFix, fix_xrange.FixXrange):

    skip_on = 'six.moves.range'

    def transform(self, node, results):
        if self.should_skip(node):
            return
        touch_import(u'six.moves', u'range',  node)
        return super(FixXrangeSix, self).transform(node, results)
