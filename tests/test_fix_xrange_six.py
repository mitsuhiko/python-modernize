from utils import check_on_input


# range()
RANGE = ("""\
x = range(1)
""", """\
from six.moves import range
x = list(range(1))
""")

RANGE_IDEMPOTENT = ("""\
x = list(range(1))
""", """\
from six.moves import range
x = list(range(1))
""")

# xrange()
XRANGE = ("""\
xrange(1)
""", """\
from six.moves import range
range(1)
""")

XRANGE_IDEMPOTENT = ("""\
from six.moves import range
range(1)
""", """\
from six.moves import range
range(1)
""")

# Both
XRANGE_RANGE = ("""\
x = xrange(1)
y = range(1)
""", """\
from six.moves import range
x = range(1)
y = list(range(1))
""")


def test_range():
    check_on_input(*RANGE)

def test_range_idempotent():
    check_on_input(*RANGE_IDEMPOTENT)

def test_xrange():
    check_on_input(*XRANGE)

def test_xrange_idempotent():
    check_on_input(*XRANGE_IDEMPOTENT)

def test_xrange_range():
    check_on_input(*XRANGE_RANGE)
