from lib2to3 import fixer_base
from lib2to3.fixer_util import Name


class FixFile(fixer_base.BaseFix):

    BM_compatible = True
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
