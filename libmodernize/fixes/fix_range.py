# Copyright 2008 Armin Ronacher.
# Licensed to PSF under a Contributor Agreement.

from lib2to3 import fixer_base
from lib2to3.fixer_util import Call, Name, touch_import


class FixRange(fixer_base.BaseFix):

    BM_compatible = True
    order = "pre"

    PATTERN = """
        power<
            (name='range'|name='xrange')
            trailer< '(' (
                args=(not(argument<any '=' any>) any)
            ) ')' >
        >
    """

    def transform(self, node, results):
        name = results.get('name')
        if name is None:
            return
        elif name.value == 'xrange':
            touch_import(u'six.moves', u'range', node)
            name.replace(Name('range', prefix=name.prefix))
        else:
            original_args = [x.clone() for x in results['args']]
            range_call = Call(Name('range'), original_args)
            return Call(Name("list"), [range_call])
