from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import, Name


class FixUnicodeCallable(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
        power< name='unicode'
            trailer< '(' [any] ')' >
            any *
        >
    """

    def transform(self, node, results):
        touch_import(None, u'six', node)
        name = results['name']
        name.replace(Name(u'six.text_type', prefix=name.prefix))
