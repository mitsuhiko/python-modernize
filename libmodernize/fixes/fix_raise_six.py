"""Fixer for 'raise E, V, T'

raise E, V, T -> six.reraise(E, V, T)

Not very well-tested, based on examples
"""
# Author : Markus Unterwaditzer

# Local imports
from lib2to3 import fixer_base
from lib2to3.fixer_util import Name, Call, Comma, touch_import

class FixRaiseSix(fixer_base.BaseFix):

    BM_compatible = True
    PATTERN = """
    raise_stmt< 'raise' exc=any ',' val=any ',' tb=any >
    """

    def transform(self, node, results):
        exc = results["exc"].clone()
        val = results["val"].clone()
        tb = results["tb"].clone()

        exc.prefix = u""
        val.prefix = tb.prefix = u" "

        touch_import(u'six', u'reraise', node)
        return Call(Name(u"six.reraise"), [exc, Comma(), val, Comma(), tb],
                    prefix=node.prefix)
