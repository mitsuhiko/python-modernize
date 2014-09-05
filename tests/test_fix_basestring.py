from utils import check_on_input


BASESTRING = ("""\
isinstance(x, basestring)
""", """\
import six
isinstance(x, six.string_types)
""")


def test_basestring():
    check_on_input(*BASESTRING)
