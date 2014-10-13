import sys
try:
    from StringIO import StringIO  # Python 2
except ImportError:
    from io import StringIO  # Python 3

from libmodernize.main import main as modernize_main

def test_list_fixers():
    sio = StringIO()
    real_stdout = sys.stdout
    sys.stdout = sio
    try:
        exitcode = modernize_main(['-l'])
    finally:
        sys.stdout = real_stdout
    assert exitcode == 0, exitcode
    assert 'xrange_six' in sio.getvalue()
