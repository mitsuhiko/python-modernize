from __future__ import absolute_import

from utils import check_on_input


FILE_CALL = ("""\
file('some/file/path', 'r')
""", """\
open('some/file/path', 'r')
""")

FILE_CONTEXT_MANAGER = ("""\
with file('some/file/path', 'r') as file_:
    pass
""", """\
with open('some/file/path', 'r') as file_:
    pass
""")

FILE_ATTR = ("""\
file('path').readlines
""", """\
open('path').readlines
""")

FILE_REF = ("""\
file
""", """\
file
""")


def test_file_call():
    check_on_input(*FILE_CALL)

def test_file_context_manager():
    check_on_input(*FILE_CONTEXT_MANAGER)

def test_file_attr():
    check_on_input(*FILE_ATTR)

def test_file_ref():
    check_on_input(*FILE_REF)
