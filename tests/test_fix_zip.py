from utils import check_on_input


ZIP_CALL_NO_ARGS = ("""\
zip()
""", """\
from six.moves import zip
zip()
""")

ZIP_CALL_1_ARG = ("""\
zip(x)
""", """\
from six.moves import zip
zip(x)
""")

ZIP_CALL_2_ARGS = ("""\
zip(x, y)
""", """\
from six.moves import zip
zip(x, y)
""")

ZIP_CALL_STAR_ARGS = ("""\
zip(*args)
""", """\
from six.moves import zip
zip(*args)
""")

ZIP_KWARGS = ("""\
zip(arg1=[1])
""", """\
zip(arg1=[1])
""")


def test_zip_call_no_args():
    check_on_input(*ZIP_CALL_NO_ARGS)

def test_zip_call_1_arg():
    check_on_input(*ZIP_CALL_1_ARG)

def test_zip_call_2_args():
    check_on_input(*ZIP_CALL_2_ARGS)

def test_zip_call_star_args():
    check_on_input(*ZIP_CALL_STAR_ARGS)

def test_zip_kwargs():
    check_on_input(*ZIP_KWARGS)
