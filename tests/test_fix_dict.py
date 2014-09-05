from utils import check_on_input

DICT_ITERITEMS = ("""\
x.iteritems()
""", """\
import six
six.iteritems(x)
""")

DICT_ITERKEYS = ("""\
x.iterkeys()
""", """\
import six
six.iterkeys(x)
""")

DICT_ITERVALUES = ("""\
x.itervalues()
""", """\
import six
six.itervalues(x)
""")

DICT_TOO_MANY_ARGS = ("""\
x.iteritems(42)
""", """\
x.iteritems(42)
""")


def test_dict_iteritems():
    check_on_input(*DICT_ITERITEMS)

def test_dict_iterkeys():
    check_on_input(*DICT_ITERKEYS)

def test_dict_itervalues():
    check_on_input(*DICT_ITERVALUES)

def test_dict_too_many_args():
    check_on_input(*DICT_TOO_MANY_ARGS)
