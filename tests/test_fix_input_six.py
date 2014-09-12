from utils import check_on_input


INPUT = ("""\
input()
""", """\
from six.moves import input
eval(input())
""")

INPUT_ARGS = ("""\
input('hello')
""", """\
from six.moves import input
eval(input('hello'))
""")

RAW_INPUT = ("""\
raw_input()
""", """\
from six.moves import input
input()
""")

RAW_INPUT_TRAILER = ("""\
raw_input()[0]
""", """\
from six.moves import input
input()[0]
""")

RAW_INPUT_INPUT = ("""\
raw_input()
input()
""", """\
from six.moves import input
input()
eval(input())
""")


def test_input():
    check_on_input(*INPUT)

def test_input_args():
    check_on_input(*INPUT_ARGS)

def test_raw_input():
    check_on_input(*RAW_INPUT)

def test_raw_input_trailer():
    check_on_input(*RAW_INPUT_TRAILER)

def test_raw_input_input():
    check_on_input(*RAW_INPUT_INPUT)
