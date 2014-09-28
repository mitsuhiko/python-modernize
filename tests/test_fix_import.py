from __future__ import absolute_import

from utils import check_on_input


NO_IMPORTS = ("""\
""", """\
""")

ONLY_FUTURE_IMPORTS = ("""\
from __future__ import print_function
""", """\
from __future__ import print_function
""")

ONLY_NORMAL_IMPORTS = ("""\
import foo
""", """\
from __future__ import absolute_import
import foo
""")

NORMAL_AND_FUTURE_IMPORTS = ("""\
from __future__ import print_function
import foo
""", """\
from __future__ import print_function
from __future__ import absolute_import
import foo
""")


def test_no_imports():
    check_on_input(*NO_IMPORTS)

def test_only_future_imports():
    check_on_input(*ONLY_FUTURE_IMPORTS)

def test_only_normal_imports():
    check_on_input(*ONLY_NORMAL_IMPORTS)

def test_normal_and_future_imports():
    check_on_input(*NORMAL_AND_FUTURE_IMPORTS)
