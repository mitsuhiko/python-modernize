import re
from lib2to3.pgen2 import token
from lib2to3 import fixer_base
from lib2to3.fixer_util import touch_import, Name, Call

_mapping = {u"unichr" : u"chr", u"unicode" : u"str"}
_literal_re = re.compile(u"[uU][rR]?[\\'\\\"]")

class FixUnicode(fixer_base.BaseFix):
    BM_compatible = True
    PATTERN = """
        STRING |
        power< name='unicode'
            trailer< '(' [any] ')' >
            any *
        >
    """

    def transform(self, node, results):
        if 'name' in results:
            touch_import(None, u'six', node)
            name = results['name']
            name.replace(Name(u'six.text_type', prefix=name.prefix))
        elif node.type == token.STRING and _literal_re.match(node.value):
            touch_import(None, u'six', node)
            new = node.clone()
            new.value = new.value[1:]
            new.prefix = ''
            node.replace(Call(Name(u'six.u', prefix=node.prefix), [new]))
