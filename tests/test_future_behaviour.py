# Tests for problem with multiple futures added to single file
from __future__ import absolute_import

import tempfile
import os
import shutil
from libmodernize.main import main as modernize_main

from utils import check_on_input

SINGLE_PRINT_CONTENT = """
print 'world'
"""

TWO_PRINTS_CONTENT = """
print 'Hello'
print 'world'
"""

COMPLICATED_CONTENT = """
print 'Hello'
print u'world'
def sub(x):
    print x, u"here"
"""

PROBLEMATIC_CONTENT = '''

"""
Hello
"""

from a.b.c import d

def test_existing():
    print d
'''

def _check_for_multiple_futures(file_name, source_content):
    """
    Checks for multiple identical futures in given file,
    raises if found.
    Returns dictionary of found futures (name => 1)
    """
    counts = {}
    result_content = ""
    with open(file_name, "rt") as input:
        for line in input:
            if line.startswith("from __future__"):
                counts[line] = 1 + counts.get(line, 0)
            result_content += line
    for future, how_many in counts.items():
        if how_many > 1:
            raise Exception("The same future repeated more than once ({0} times):\n{1}\n\n* Input file:\n{2}\n\n* Output file:\n{3}\n".format(how_many, future, source_content, result_content))
    return counts

def _check_on_input(file_content, extra_flags = []):
    try:
        tmpdirname = tempfile.mkdtemp()
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "wt") as input:
            input.write(file_content)
        modernize_main(extra_flags + ["-w", test_input_name])
        _check_for_multiple_futures(test_input_name, file_content)
    finally:
        shutil.rmtree(tmpdirname)

def test_single_print():
    _check_on_input(SINGLE_PRINT_CONTENT)

def test_two_prints():
    _check_on_input(TWO_PRINTS_CONTENT)

def test_many_prints_and_unicode():
    _check_on_input(COMPLICATED_CONTENT, ["--future-unicode"])

def test_two_files_on_single_run():
    # Mostly to test whether second file gets its "from future ..."
    try:
        tmpdirname = tempfile.mkdtemp()
        input_names = [ os.path.join(tmpdirname, "input_{0}.py".format(idx))
                        for idx in range(0,3) ]
        for input_name in input_names:
            with open(input_name, "wt") as input:
                input.write(TWO_PRINTS_CONTENT)
        modernize_main(["-w"] + input_names)
        for input_name in input_names:
            futs = _check_for_multiple_futures(input_name, TWO_PRINTS_CONTENT)
            if not futs:
                raise Exception("File {0} got no from __future__ (but it should)")
    finally:
        shutil.rmtree(tmpdirname)

def test_problematic_file():
    # ON this one I get crash
    _check_on_input(PROBLEMATIC_CONTENT)

FUTURE_IMPORT_AS = ("""\
from __future__ import print_function as pf
print("abc")
""", """\
from __future__ import print_function as pf
print("abc")
""")

FUTURE_IMPORT_AS_MULTIPLE = ("""\
from __future__ import print_function as pf, division as dv
print("abc")
""", """\
from __future__ import print_function as pf, division as dv
print("abc")
""")

def test_future_import_as():
    check_on_input(*FUTURE_IMPORT_AS)

def test_future_import_as_multiple():
    check_on_input(*FUTURE_IMPORT_AS_MULTIPLE)
