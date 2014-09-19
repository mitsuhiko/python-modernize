from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import


class FixOpen(fixer_base.BaseFix):

    run_order = 10  # Must run after fix_file.
    BM_compatible = True
    # Fixers don't directly stack, so make sure the 'file' case is covered.
    PATTERN = """
    power< ('open' | 'file') trailer< '(' any+ ')' > >
    """

    def transform(self, node, results):
        touch_import(u'io', u'open', node)
