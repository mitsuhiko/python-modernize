from __future__ import absolute_import

from utils import check_on_input


RAISE_TRACEBACK = ("""\
raise Exception, value, traceback
""", """\
from __future__ import absolute_import
import six
six.reraise(Exception, value, traceback)
""")


def test_raise_traceback():
    check_on_input(*RAISE_TRACEBACK)
