from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import


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
        touch_import(u'io', u'open', node)
