import os
from setuptools import setup

readme = open(os.path.join(os.path.dirname(__file__), 'README'), 'r').read()

setup(
    name='modernize',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='0.1',
    url='http://github.com/mitsuhiko/modernize',
    packages=['modernize', 'modernize.fixes'],
    description='A hack on top of 2to3 for modernizing code for '
                'hybrid codebases.',
    long_description=readme,
    zip_safe=False,
    test_suite='tests',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: PHP',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
