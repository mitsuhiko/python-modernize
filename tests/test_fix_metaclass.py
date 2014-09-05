from utils import check_on_input


METACLASS_NO_BASE = ("""\
class Foo:
    __metaclass__ = Meta
""", """\
import six
class Foo(six.with_metaclass(Meta)):
    pass
""")

METACLASS_NO_BASE_PARENS = ("""\
class Foo():
    __metaclass__ = Meta
""", """\
import six
class Foo(six.with_metaclass(Meta)):
    pass
""")

METACLASS_SINGLE_BASE = ("""\
class Foo(Bar):
    __metaclass__ = Meta
""", """\
import six
class Foo(six.with_metaclass(Meta, Bar)):
    pass
""")

METACLASS_MANY_BASES = ("""\
class Foo(Bar, Spam):
    __metaclass__ = Meta
""", """\
import six
class Foo(six.with_metaclass(Meta, type('NewBase', (Bar, Spam), {}))):
    pass
""")

METACLASS_ONE_LINER = ("""\
class Foo: __metaclass__ = Meta
""", """\
import six
class Foo(six.with_metaclass(Meta)): pass
""")


def test_metaclass_no_base():
    check_on_input(*METACLASS_NO_BASE)

def test_metaclass_no_base_parens():
    check_on_input(*METACLASS_NO_BASE_PARENS)

def test_metaclass_single_base():
    check_on_input(*METACLASS_SINGLE_BASE)

def test_metaclass_MANY_BASES():
    check_on_input(*METACLASS_MANY_BASES)

def test_metaclass_one_liner():
    check_on_input(*METACLASS_ONE_LINER)
