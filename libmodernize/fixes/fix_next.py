"""Fixer for it.next() -> advance_iterator(it)"""

# Local imports
from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import, Name, Call

bind_warning = "Calls to builtin next() possibly shadowed by global binding"


class FixNext(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
    power< base=any+ trailer< '.' attr='next' > trailer< '(' ')' > >
    """

    order = "pre" # Pre-order tree traversal

    def transform(self, node, results):
        assert results
        base = results.get('base')
        if not base:
            return
        base = [n.clone() for n in base]
        base[0].prefix = u""
        node.replace(Call(Name(u"next", prefix=node.prefix), base))
