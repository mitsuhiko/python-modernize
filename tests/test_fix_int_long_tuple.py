from __future__ import absolute_import

from utils import check_on_input


INT_LONG_ISINSTANCE = ("""\
isinstance(1, (int, long))
""", """\
import six
isinstance(1, six.integer_types)
""")

LONG_INT_ISINSTANCE = ("""\
isinstance(1, (long, int))
""", """\
import six
isinstance(1, six.integer_types)
""")


def test_int_long_isinstance():
    check_on_input(*INT_LONG_ISINSTANCE)

def test_long_int_isinstance():
    check_on_input(*LONG_INT_ISINSTANCE)
