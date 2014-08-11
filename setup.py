import os, re
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README.rst'), 'r').read()

module_file = open(os.path.join(os.path.dirname(__file__), 'libmodernize', '__init__.py'), 'r').read()
version_match = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", module_file, re.M)
if not version_match:
    raise Exception("couldn't find version number")
version = version_match.group(1)

setup(
    name='modernize',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version=version,
    url='https://github.com/python-modernize/python-modernize',
    packages=['libmodernize', 'libmodernize.fixes'],
    description='A hack on top of 2to3 for modernizing code for '
                'hybrid codebases.',
    long_description=readme,
    entry_points={
        'console_scripts': [
            'python-modernize = libmodernize.main:main'
        ]
    },
    zip_safe=False,
    tests_require='nose',
    test_suite='nose.collector',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 3',
    ]
)
