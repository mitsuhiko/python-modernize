from utils import check_on_input


MAP_2_ARGS = ("""\
map(x, [1])
""", """\
from six.moves import map
list(map(x, [1]))
""")

MAP_3_ARGS = ("""\
map(x, [1], [2])
""", """\
from six.moves import map
list(map(x, [1], [2]))
""")

MAP_4_ARGS = ("""\
map(x, [1], [2], [3])
""", """\
from six.moves import map
list(map(x, [1], [2], [3]))
""")

MAP_TOO_FEW_ARGS = ("""\
map(x)
""", """\
map(x)
""")

MAP_KWARGS = ("""\
map(function=x, [1])
""", """\
map(function=x, [1])
""")

MAP_REF = ("""\
x = map
""", """\
x = map
""")

MAP_ITERATOR_CONTEXT = ("""\
for a in map(x, [1]):
    pass
""", """\
from six.moves import map
for a in map(x, [1]):
    pass
""")

MAP_SIX_ALREADY = ("""\
from six.moves import map
map(x, [1])
""", """\
from six.moves import map
map(x, [1])
""")


def test_map_2_args():
    check_on_input(*MAP_2_ARGS)

def test_map_3_args():
    check_on_input(*MAP_3_ARGS)

def test_map_4_args():
    check_on_input(*MAP_4_ARGS)

def test_map_too_few_args():
    check_on_input(*MAP_TOO_FEW_ARGS)

def test_map_kwargs():
    check_on_input(*MAP_KWARGS)

def test_map_ref():
    check_on_input(*MAP_REF)

def test_map_iterator_context():
    check_on_input(*MAP_ITERATOR_CONTEXT)

def test_map_six_already():
    check_on_input(*MAP_SIX_ALREADY)
