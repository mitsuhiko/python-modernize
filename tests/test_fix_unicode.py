from __future__ import absolute_import

from utils import check_on_input

UNICODE_LITERALS = """\
a = u''
b = U"\\u2041"
c = ur'''blah
foo'''
import sys
"""

UNICODE_LITERALS_six = """\
from __future__ import absolute_import
import six
a = six.u('')
b = six.u("\\u2041")
c = six.u(r'''blah
foo''')
import sys
"""

UNICODE_LITERALS_compat = """\
from __future__ import absolute_import
a = u''
b = U"\\u2041"
c = ur'''blah
foo'''
import sys
"""

UNICODE_LITERALS_future = """\
from __future__ import absolute_import
from __future__ import unicode_literals
a = ''
b = "\\u2041"
c = r'''blah
foo'''
import sys
"""

def test_unicode_six():
    check_on_input(UNICODE_LITERALS, UNICODE_LITERALS_six, extra_flags=['--six-unicode'])

def test_unicode_compat():
    check_on_input(UNICODE_LITERALS, UNICODE_LITERALS_compat)

def test_unicode_future():
    check_on_input(UNICODE_LITERALS, UNICODE_LITERALS_future, extra_flags=['--future-unicode'])
