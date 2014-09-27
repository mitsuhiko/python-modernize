# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.
from __future__ import absolute_import

from lib2to3 import fixer_base
from lib2to3.fixes import fix_xrange
from libmodernize import touch_import


class FixXrangeSix(fixer_base.ConditionalFix, fix_xrange.FixXrange):

    skip_on = 'six.moves.range'

    def transform(self, node, results):
        if self.should_skip(node):
            return
        touch_import(u'six.moves', u'range',  node)
        return super(FixXrangeSix, self).transform(node, results)
