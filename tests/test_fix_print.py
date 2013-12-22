
import tempfile
import os
import shutil
from libmodernize.main import main as modernize_main


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


def _check_as_expected(input_content, output_content, expected_content):
    if output_content != expected_content:
        raise Exception("Input:\n%sOutput:\n%s\nExpecting:\n%s" % (input_content, output_content, expected_content))

def _check_on_input(input_content, expected_content, extra_flags = []):
    try:
        tmpdirname = tempfile.mkdtemp()
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "wt") as input_file:
            input_file.write(input_content)
        modernize_main(extra_flags + ["-w", test_input_name])

        output_content = ""
        with open(test_input_name, "rt") as output_file:
            for line in output_file:
                if line:
                    output_content += line

        _check_as_expected(input_content, output_content, expected_content)
    finally:
        shutil.rmtree(tmpdirname)

def test_print_bare():
    _check_on_input(*PRINT_BARE)

def test_print_simple():
    _check_on_input(*PRINT_SIMPLE)

def test_print_multiple():
    _check_on_input(*PRINT_MULTIPLE)

def test_print_with_parens():
    _check_on_input(*PRINT_WITH_PARENS)

def test_print_with_comma():
    _check_on_input(*PRINT_WITH_COMMA)

def test_print_to_stream():
    _check_on_input(*PRINT_TO_STREAM)

def test_print_to_stream_with_comma():
    _check_on_input(*PRINT_TO_STREAM_WITH_COMMA)
