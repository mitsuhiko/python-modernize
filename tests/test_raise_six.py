from utils import check_on_input


RAISE_TRACEBACK = ("""\
raise Exception, value, traceback
""", """\
import six
six.reraise(Exception, value, traceback)
""")


def test_raise_traceback():
    check_on_input(*RAISE_TRACEBACK)
