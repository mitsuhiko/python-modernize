from utils import check_on_input


FILTER_CALL = ("""\
filter(None, [1])
""", """\
from six.moves import filter
list(filter(None, [1]))
""")

FILTER_TOO_FEW_ARGS = ("""\
filter(None)
""", """\
filter(None)
""")

FILTER_TOO_MANY_ARGS = ("""\
filter(None, [1], [2])
""", """\
filter(None, [1], [2])
""")

FILTER_KWARGS = ("""\
filter(function=None, [1])
""", """\
filter(function=None, [1])
""")

FILTER_ITERATOR_CONTEXT = ("""\
for a in filter(None, [1]):
    pass
""", """\
from six.moves import filter
for a in filter(None, [1]):
    pass
""")


def test_filter_call():
    check_on_input(*FILTER_CALL)

def test_filter_too_few_args():
    check_on_input(*FILTER_TOO_FEW_ARGS)

def test_filter_too_many_args():
    check_on_input(*FILTER_TOO_MANY_ARGS)

def test_filter_kwargs():
    check_on_input(*FILTER_KWARGS)

def test_filter_iterator_context():
    check_on_input(*FILTER_ITERATOR_CONTEXT)
