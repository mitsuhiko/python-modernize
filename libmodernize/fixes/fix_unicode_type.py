from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import, Name


class FixUnicodeType(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """'unicode'"""

    def transform(self, node, results):
        touch_import(None, u'six', node)
        return Name(u'six.text_type', prefix=node.prefix)
