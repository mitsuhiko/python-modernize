from __future__ import absolute_import

from lib2to3 import fixer_base
import libmodernize


class FixOpen(fixer_base.ConditionalFix):

    BM_compatible = True
    order = "pre"
    skip_on = "io.open"

    PATTERN = """
    power< 'open' trailer< '(' any+ ')' > >
    """

    def transform(self, node, results):
        if self.should_skip(node):
            return
        libmodernize.touch_import(u'io', u'open', node)
