from lib2to3 import refactor
import sys

from libmodernize import fixes


LIB2TO3_FIXES_PKG = 'lib2to3.fixes'
LIBMODERNIZE_FIXES_PKG = 'libmodernize.fixes'


def check_existence(prefix, module_names):
    """Check that module_names have the expected prefix and exist."""
    dotted_prefix = prefix + '.'
    for module_name in module_names:
        if not module_name.startswith(dotted_prefix):
            msg = '{0!r} does not start with {1!r}'.format(module_name, prefix)
            raise AssertionError(msg)
        try:
            __import__(module_name)
        except ImportError:
            raise AssertionError('{0!r} cannot be imported'.format(module_name))


def test_lib2to3_fix_names():
    check_existence(LIB2TO3_FIXES_PKG, fixes.lib2to3_fix_names)


def test_six_fix_names():
    check_existence(LIBMODERNIZE_FIXES_PKG, fixes.six_fix_names)


def test_fixers_importable():
    fixers = refactor.get_fixers_from_package(LIBMODERNIZE_FIXES_PKG)
    for module_name in fixers:
        try:
            __import__(module_name)
        except ImportError:
            raise AssertionError('{0!r} cannot be imported'.format(module_name))
