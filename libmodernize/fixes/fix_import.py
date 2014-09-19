from __future__ import absolute_import

from lib2to3.fixes import fix_import
import libmodernize


class FixImport(fix_import.FixImport):

    def transform(self, node, results):
        results = super(FixImport, self).transform(node, results)
        if results is None:
            return
        libmodernize.add_future(node, 'absolute_import')
        return results
