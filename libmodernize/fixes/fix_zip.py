# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.
from __future__ import absolute_import

from lib2to3.fixes import fix_zip
import libmodernize

class FixZip(fix_zip.FixZip):

    skip_on = "six.moves.zip"

    def transform(self, node, results):
        result = super(FixZip, self).transform(node, results)
        # Always use six.moves.zip so that even Python 2.7 gets performance
        # boost from using itertools in iterator contexts.
        libmodernize.touch_import(u'six.moves', u'zip', node)
        return result
