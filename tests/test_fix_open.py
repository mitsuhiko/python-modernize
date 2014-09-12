from utils import check_on_input


OPEN = ("""\
open('some/path')
""", """\
from io import open
open('some/path')
""")


def test_open():
    check_on_input(*OPEN, extra_flags=['-f', 'libmodernize.fixes.fix_open'])

def test_open_optional():
    check_on_input(OPEN[0], OPEN[0])
