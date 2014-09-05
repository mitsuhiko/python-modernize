from utils import check_on_input


RAISE = ("""\
raise
""", """\
raise
""")

RAISE_EXC= ("""\
raise e
""", """\
raise e
""")

RAISE_VALUE= ("""\
raise e, v
""", """\
raise e(v)
""")

RAISE_TUPLE = ("""\
raise ((((E1, E2), E3), E4), E5), V
""", """\
raise E1(V)
""")

# Can't be converted; translation would emit a warning.
RAISE_STRING = ("""\
raise 'exception'
""", """\
raise 'exception'
""")


def test_raise():
    check_on_input(*RAISE)

def test_raise_exc():
    check_on_input(*RAISE_EXC)

def test_raise_value():
    check_on_input(*RAISE_VALUE)

def test_raise_tuple():
    check_on_input(*RAISE_TUPLE)

def test_raise_string():
    check_on_input(*RAISE_STRING)
