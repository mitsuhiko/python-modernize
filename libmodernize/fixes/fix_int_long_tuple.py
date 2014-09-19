from __future__ import absolute_import

from lib2to3 import fixer_base
from lib2to3 import fixer_util


class FixIntLongTuple(fixer_base.BaseFix):

    run_order = 4  # Must run before fix_long.

    PATTERN = """
    pair=atom < '(' testlist_gexp < (
        ('int' ',' 'long') |
        ('long' ',' 'int')
    ) > ')' >
    """

    def transform(self, node, results):
        if 'name' in results:
            name = results['name']
            name.replace(fixer_util.Name('int', prefix=name.prefix))
        else:
            fixer_util.touch_import(None, 'six', node)
            pair = results['pair']
            pair.replace(fixer_util.Name('six.integer_types', prefix=pair.prefix))
