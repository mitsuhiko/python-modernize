from __future__ import absolute_import

from utils import check_on_input


FILTER_CALL = ("""\
filter(func, [1])
""", """\
from __future__ import absolute_import
from six.moves import filter
list(filter(func, [1]))
""")


FILTER_ITERATOR_CONTEXT = ("""\
for a in filter(func, [1]):
    pass
""", """\
from __future__ import absolute_import
from six.moves import filter
for a in filter(func, [1]):
    pass
""")


def test_filter_call():
    check_on_input(*FILTER_CALL)

def test_filter_iterator_context():
    check_on_input(*FILTER_ITERATOR_CONTEXT)
