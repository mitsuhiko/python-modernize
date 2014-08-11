import os.path
import tempfile
import shutil

from libmodernize.main import main as modernize_main

def _check_as_expected(input_content, output_content, expected_content):
    if output_content != expected_content:
        raise AssertionError("Input:\n%sOutput:\n%s\nExpecting:\n%s" %
                    (input_content, output_content, expected_content))

def check_on_input(input_content, expected_content, extra_flags = []):
    """Check that input_content is fixed to expected_content.
    
    Writes input_content to a temporary file, runs modernize on it with any
    extra arguments as given in extra_flags, and asserts that the resulting file
    matches expected_content.
    """
    tmpdirname = tempfile.mkdtemp()
    try:
        test_input_name = os.path.join(tmpdirname, "input.py")
        with open(test_input_name, "wt") as input_file:
            input_file.write(input_content)
        modernize_main(extra_flags + ["-w", test_input_name])

        output_content = ""
        with open(test_input_name, "rt") as output_file:
            for line in output_file:
                if line:
                    output_content += line

        _check_as_expected(input_content, output_content, expected_content)
    finally:
        shutil.rmtree(tmpdirname)