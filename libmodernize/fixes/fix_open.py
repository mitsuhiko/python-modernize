from libmodernize.fixes import fix_file
from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import


class FixOpen(fix_file.FixFile):

    BM_compatible = True
    order = "pre"

    PATTERN = """
    power< name=('open'|'file') trailer< '(' any+ ')' > any* >
    """

    def transform(self, node, results):
        touch_import(u'io', u'open', node)
        if len(results['name']) == 1 and results['name'][0].value == 'file':
            results['name'] = results['name'][0]
            super(FixOpen, self).transform(node, results)
