from __future__ import absolute_import

from lib2to3.fixes import fix_import
import libmodernize


class FixImport(fix_import.FixImport):

    # Make sure this runs before any other fixer to guarantee that any other
    # added absolute_import doesn't block this fixer's execution.
    run_order = 1

    def transform(self, node, results):
        results = super(FixImport, self).transform(node, results)
        if results is None:
            return
        libmodernize.add_future(node, 'absolute_import')
        return results
