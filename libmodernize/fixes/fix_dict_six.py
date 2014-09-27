"""Fixer for iterkeys() -> six.iterkeys(), and similarly for iteritems and itervalues."""
from __future__ import absolute_import

# Local imports
from lib2to3 import fixer_util
from lib2to3.fixes import fix_dict
import libmodernize


class FixDictSix(fix_dict.FixDict):

    def transform_iter(self, method_name, node, base):
        """Call six.iteritems() and friends."""
        if method_name.startswith(u'view'):
            method_name = u'iter' + method_name[4:]
        libmodernize.touch_import(None, u'six', node)
        new_node = [n.clone() for n in base]
        new_node[0].prefix = u''
        name = fixer_util.Name(u'six.' + method_name, prefix=node.prefix)
        node.replace(fixer_util.Call(name, new_node))

    def transform(self, node, results):
        method = results['method'][0]
        method_name = method.value
        if method_name in ('keys', 'items', 'values'):
            return super(FixDictSix, self).transform(node, results)
        else:
            return self.transform_iter(method_name, node, results['head'])
