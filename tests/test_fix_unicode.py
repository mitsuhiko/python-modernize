from utils import check_on_input

UNICODE_LITERALS = """\
a = u''
b = U"\\u2041"
c = ur'''blah
foo'''
"""

UNICODE_LITERALS_six = """\
import six
a = six.u('')
b = six.u("\\u2041")
c = six.u(r'''blah
foo''')
"""

UNICODE_LITERALS_compat = UNICODE_LITERALS

UNICODE_LITERALS_future = """\
from __future__ import unicode_literals
a = ''
b = "\\u2041"
c = r'''blah
foo'''
"""

def test_unicode_six():
    check_on_input(UNICODE_LITERALS, UNICODE_LITERALS_six, extra_flags=['--six-unicode'])

def test_unicode_compat():
    check_on_input(UNICODE_LITERALS, UNICODE_LITERALS_compat)

def test_unicode_future():
    check_on_input(UNICODE_LITERALS, UNICODE_LITERALS_future, extra_flags=['--future-unicode'])

UNICODE_NAME = ("""\
unicode(x)
""", """\
import six
six.text_type(x)
"""
)

def test_unicode_name():
    check_on_input(*UNICODE_NAME, extra_flags=['--six-unicode'])
    # TODO: This should be independent of what we want to do with unicode literals
