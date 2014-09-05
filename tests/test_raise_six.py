from utils import check_on_input

# To make sure the fixer is not too aggressive.
RAISE_VALUE = ("""\
raise Exception, value
""", """\
raise Exception(value)
""")

RAISE_TRACEBACK = ("""\
raise Exception, value, traceback
""", """\
import six
six.reraise(Exception, value, traceback)
""")


def test_raise_value():
    check_on_input(*RAISE_VALUE)

def test_raise_traceback():
    check_on_input(*RAISE_TRACEBACK)
