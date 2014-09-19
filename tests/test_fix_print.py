
from utils import check_on_input


PRINT_BARE = ("""\
print
""", """\
from __future__ import print_function
print()
""")

PRINT_SIMPLE = ("""\
print 'Hello'
""", """\
from __future__ import print_function
print('Hello')
""")

PRINT_MULTIPLE = ("""\
print 'Hello', 'world'
""", """\
from __future__ import print_function
print('Hello', 'world')
""")

PRINT_WITH_PARENS = ("""\
print('Hello')
""", """\
from __future__ import print_function
print('Hello')
""")

PRINT_WITH_COMMA = ("""\
print 'Hello',
""", """\
from __future__ import print_function
print('Hello', end=' ')
""")

PRINT_TO_STREAM = ("""\
print >>x, 'Hello'
""", """\
from __future__ import print_function
print('Hello', file=x)
""")

PRINT_TO_STREAM_WITH_COMMA = ("""\
print >>x, 'Hello',
""", """\
from __future__ import print_function
print('Hello', end=' ', file=x)
""")

def test_print_bare():
    check_on_input(*PRINT_BARE)

def test_print_simple():
    check_on_input(*PRINT_SIMPLE)

def test_print_multiple():
    check_on_input(*PRINT_MULTIPLE)

def test_print_with_parens():
    check_on_input(*PRINT_WITH_PARENS)

def test_print_with_comma():
    check_on_input(*PRINT_WITH_COMMA)

def test_print_to_stream():
    check_on_input(*PRINT_TO_STREAM)

def test_print_to_stream_with_comma():
    check_on_input(*PRINT_TO_STREAM_WITH_COMMA)
