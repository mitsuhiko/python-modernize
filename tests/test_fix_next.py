from __future__ import absolute_import

from utils import check_on_input


NEXT_METHOD = ("""
spam.next()
""",
"""
next(spam)
""")

NEXT_NESTED = ("""
eggs.spam.next()
""",
"""
next(eggs.spam)
""")


def test_next_method():
    check_on_input(*NEXT_METHOD)


def test_next_nested():
    check_on_input(*NEXT_NESTED)
