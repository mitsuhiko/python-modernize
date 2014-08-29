from utils import check_on_input


UNICODE_CALLABLE = ("""\
unicode(x)
""", """\
import six
six.text_type(x)
"""
)


def test_unicode_callable():
    check_on_input(*UNICODE_CALLABLE)
