from utils import check_on_input


MAP_1_ARG = ("""\
map(x)
""", """\
map(x)
""")

MAP_2_ARGS = ("""\
map(x, [1])
""", """\
from six.moves import map
map(x, [1])
""")

MAP_3_ARGS = ("""\
map(x, [1], [2])
""", """\
from six.moves import map
map(x, [1], [2])
""")

MAP_4_ARGS = ("""\
map(x, [1], [2], [3])
""", """\
from six.moves import map
map(x, [1], [2], [3])
""")

MAP_REF = ("""\
x = map
""", """\
x = map
""")


def test_map_1_arg():
    check_on_input(*MAP_1_ARG)

def test_map_2_args():
    check_on_input(*MAP_2_ARGS)

def test_map_3_args():
    check_on_input(*MAP_3_ARGS)

def test_map_4_args():
    check_on_input(*MAP_4_ARGS)

def test_map_ref():
    check_on_input(*MAP_REF)
