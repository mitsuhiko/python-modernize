from __future__ import absolute_import

import sys

try:
    from six.moves import tkinter
except ImportError:
    tkinter = None

from libmodernize.fixes import fix_imports_six

from utils import check_on_input


MOVED_MODULE = ("""\
import ConfigParser
ConfigParser.ConfigParser()
""", """\
import six.moves.configparser
six.moves.configparser.ConfigParser()
""")

MOVED_MODULE_FROMLIST = ("""\
from ConfigParser import ConfigParser
ConfigParser()
""", """\
from six.moves.configparser import ConfigParser
ConfigParser()
""")


def test_moved_module():
    check_on_input(*MOVED_MODULE)

def test_moved_module_fromlist():
    check_on_input(*MOVED_MODULE_FROMLIST)

def test_validate_mapping():
    for py2_name, six_name in fix_imports_six.FixImportsSix.mapping.items():
        try:
            __import__(py2_name)
            __import__(six_name)
        except ImportError as exc:
            if 'tkinter' in six_name and tkinter is not None:
                raise
            elif 'winreg' in six_name and sys.platform.startswith('win'):
                raise
