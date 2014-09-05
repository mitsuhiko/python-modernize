from utils import check_on_input


# range()
RANGE_1_ARG = ("""\
range(1)
""", """\
list(range(1))
""")

RANGE_2_ARGS = ("""\
range(1, 2)
""", """\
list(range(1, 2))
""")

RANGE_3_ARGS = ("""\
range(1, 2, 3)
""", """\
list(range(1, 2, 3))
""")

RANGE_TOO_MANY_ARGS = ("""\
range(1, 2, 3, 4)
""", """\
range(1, 2, 3, 4)
""")

RANGE_TOO_FEW_ARGS= ("""\
range()
""", """\
range()
""")

RANGE_KWARGS = ("""\
range(stop=1)
""", """\
range(stop=1)
""")

# xrange()
XRANGE_1_ARG = ("""\
xrange(1)
""", """\
from six.moves import range
range(1)
""")

XRANGE_2_ARGS= ("""\
xrange(1, 2)
""", """\
from six.moves import range
range(1, 2)
""")

XRANGE_3_ARGS= ("""\
xrange(1, 2, 3)
""", """\
from six.moves import range
range(1, 2, 3)
""")

XRANGE_KWARGS = ("""\
xrange(stop=1)
""", """\
xrange(stop=1)
""")


def test_range_1_arg():
    check_on_input(*RANGE_1_ARG)

def test_range_2_args():
    check_on_input(*RANGE_2_ARGS)

def test_range_3_args():
    check_on_input(*RANGE_3_ARGS)

def test_range_kwargs():
    check_on_input(*RANGE_KWARGS)

def test_xrange_1_arg():
    check_on_input(*XRANGE_1_ARG)

def test_xrange_2_args():
    check_on_input(*XRANGE_2_ARGS)

def test_xrange_3_args():
    check_on_input(*XRANGE_3_ARGS)

def test_xrange_kwargs():
    check_on_input(*XRANGE_KWARGS)
