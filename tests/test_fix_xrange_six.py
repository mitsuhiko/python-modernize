from __future__ import absolute_import

from utils import check_on_input


RANGE = ("""\
x = range(1)
""", """\
from __future__ import absolute_import
from six.moves import range
x = list(range(1))
""")

XRANGE = ("""\
xrange(1)
""", """\
from __future__ import absolute_import
from six.moves import range
range(1)
""")

XRANGE_RANGE = ("""\
x = xrange(1)
y = range(1)
""", """\
from __future__ import absolute_import
from six.moves import range
x = range(1)
y = list(range(1))
""")


def test_range():
    check_on_input(*RANGE)

def test_xrange():
    check_on_input(*XRANGE)

def test_xrange_range():
    check_on_input(*XRANGE_RANGE)
