from __future__ import absolute_import

from lib2to3 import fixer_base
from lib2to3.fixer_util import Name


class FixFile(fixer_base.BaseFix):

    BM_compatible = True
    order = 'pre'

    PATTERN = """
    power< name='file'
        trailer<
            '(' any ')'
        > any*
    >
    """

    def transform(self, node, results):
        name = results["name"]
        name.replace(Name("open", prefix=name.prefix))
