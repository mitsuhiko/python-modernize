from utils import check_on_input


UNICODE_TYPE_REF = ("""\
isinstance(u'str', unicode)
""", """\
import six
isinstance(u'str', six.text_type)
""")

UNICODE_TYPE_CALL = ("""\
unicode(x)
""", """\
import six
six.text_type(x)
""")


def test_unicode_type_ref():
    check_on_input(*UNICODE_TYPE_REF)


def test_unicode_type_call():
    check_on_input(*UNICODE_TYPE_CALL)
