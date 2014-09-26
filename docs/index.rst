.. modernize documentation master file, created by
   sphinx-quickstart on Fri Sep 26 08:36:35 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:tocdepth: 3

Python-Modernize
////////////////

.. toctree::
   :maxdepth: 2


Purpose of the project
======================

.. TODO Explain WHY someone would want to have their code be Python 2/3 compatible

This library is a very thin wrapper around ``lib2to3`` to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

The ``python-modernize`` command works like `2to3
<https://docs.python.org/3/library/2to3.html>`_. Here's how you'd rewrite a
single file::

    python-modernize -w example.py

See the ``LICENSE`` file for the license of ``python-modernize``.
Using this tool does not affect licensing of the modernized code.

The `project website`_ can be found on GitHub and the PyPI project name is
modernize_.


Fixers
======

Fixers come in two types: Default_ and Opt-in_. Default fixers should not break
code except for corner cases and are idempotent. Opt-in fixers are allowed to
break these rules.

Python 2 code from Python 2.6 and older will be upgraded to code that is
compatible with Python 2.6, 2.7 and Python 3. If code is
using a feature unique to Pyth on 2.7 it will not be downgraded to work with
Python 2.6, e.g. ``dict.viewitems()`` usage will not be removed to make the code
compatible with Python 2.6.

Some fixers rely on the latest release of the `six project`_ to work
(see `Fixers requiring six`_).
If you wish to turn off these fixers to avoid an external dependency on ``six``,
then use the ``--nosix`` flag. It is **strongly** recommended, though, that you
do not do this


A note about handling text literals
-----------------------------------

.. TODO Explain what a "native string" is if it is going to be referenced

- By default modernize does not change Unicode literals at all, which means that
  you can take advantage of
  `PEP 414 <http://legacy.python.org/dev/peps/pep-0414/>`_.
  This is the simplest option if you only want to support Python 3.3 and above
  along with Python 2.
- Alternatively, there is the ``--six-unicode`` flag which will wrap Unicode
  literals with the six helper function ``six.u()`` using the
  ``libmodernize.fixes.fix_unicode`` fixer. This is useful if you want
  to support Python 3.1 and Python 3.2 without bigger changes.
- The last alternative is the ``--future-unicode`` flag which
  imports the ``unicode_literals`` from the ``__future__`` module using the
  ``libmodernize.fixes.fix_unicode_future`` fixer.
  This requires Python 2.6 and later, and will require that you
  mark bytestrings with ``b''`` and native strings in ``str('')``
  or something similar that survives the transformation.


Default
-------

A default fixer will be used if:

- They are not listed in ``-x``/``--nofix``
- They are listed in ``-f``/``--fix`` either explicitly or ``all`` is listed
- They are dependent on the `six project`_ and ``--nosix`` was specified
  (see `Fixers requiring six`_)


Fixers requiring six
++++++++++++++++++++

The `six project`_ provides the ``six`` module which contains various tidbits in
helping to support Python 2/3 code. All ``six``-related fixers assume the latest
version of ``six`` is installed.


libmodernize.fixes.fix_basestring
'''''''''''''''''''''''''''''''''

Replaces all references to ``basestring`` with ``six.string_types``.


libmodernize.fixes.fix_dict_six
'''''''''''''''''''''''''''''''

Fixes various methods on the ``dict`` type for getting all keys, values, or
items. E.g.::

    x.values()
    x.itervalues()
    x.viewvalues()

becomes::

    list(x.values())   # x.values()
    six.itervalues(x)  # x.itervalues()
    six.itervalues(x)  # x.viewvalues()

Care is taken to only call ``list()`` when not in an iterating context
(e.g. not the iterable for a ``for`` loop).


libmodernize.fixes.fix_filter
'''''''''''''''''''''''''''''

When a call to ``filter()`` is discovered, ``from six.moves import filter`` is
added to the module.


libmodernize.fixes.fix_imports_six
''''''''''''''''''''''''''''''''''

Uses ``six.moves`` to fix various renamed modules, e.g.::

    import ConfigParser
    ConfigParser.ConfigParser()

becomes::

    import six.moves.configparser
    six.moves.configparser.ConfigParser()

The modules in Python 2 whose renaming in Python 3 is supported are:

- ``__builtin__``
- ``_winreg``
- ``BaseHTTPServer``
- ``CGIHTTPServer``
- ``ConfigParser``
- ``copy_reg``
- ``Cookie``
- ``cookielib``
- ``cPickle``
- ``Dialog``
- ``dummy_thread``
- ``FileDialog``
- ``gdbm``
- ``htmlentitydefs``
- ``HTMLParser``
- ``httplib``
- ``Queue``
- ``repr``
- ``robotparser``
- ``ScrolledText``
- ``SimpleDialog``
- ``SimpleHTTPServer``
- ``SimpleXMLRPCServer``
- ``SocketServer``
- ``thread``
- ``Tix``
- ``tkColorChooser``
- ``tkCommonDialog``
- ``Tkconstants``
- ``Tkdnd``
- ``tkFileDialog``
- ``tkFont``
- ``Tkinter``
- ``tkMessageBox``
- ``tkSimpleDialog``
- ``ttk``
- ``xmlrpclib``


libmodernize.fixes.fix_input_six
''''''''''''''''''''''''''''''''

Changes::

    input(x)
    raw_input(x)

to::

    from six.moves import input
    eval(input(x))  # input(x)
    input(x)        # raw_input(x)


libmodernize.fixes.fix_int_long_tuple
'''''''''''''''''''''''''''''''''''''

Changes ``(int, long)``/``(long int)`` to ``six.integer_types``.


libmodernize.fixes.fix_map
''''''''''''''''''''''''''

If a call to ``map()`` is discovered, ``from six.moves import map`` is added to
the module.


libmodernize.fixes.fix_metaclass
''''''''''''''''''''''''''''''''

Changes::

    class Foo:
        __metaclass__ = Meta

to::

    import six
    class Foo(six.with_metaclass(Meta)):
        pass


libmodernize.fixes.fix_raise_six
''''''''''''''''''''''''''''''''

Changes ``raise E, V, T`` to ``six.reraise(E, V, T)``.


libmodernize.fixes.fix_unicode_type
'''''''''''''''''''''''''''''''''''

Changes all reference of ``unicode`` to ``six.text_type``.


libmodernize.fixes.fix_xrange_six
'''''''''''''''''''''''''''''''''

Changes::

    w = xrange(x)
    y = range(z)

to::

    from six.moves import range
    w = range(x)
    y = list(range(z))

Care is taken not to call ``list()`` when ``range()`` is used as an iterating
context.


libmodernize.fixes.fix_zip
''''''''''''''''''''''''''

If ``zip()`` is called, ``from six.moves import zip`` is added to the module.


``2to3`` fixers
+++++++++++++++

Some `fixers from lib2to3 <https://docs.python.org/3/library/2to3.html#fixers>`_
in Python's standard library are run by default unmodified as their
transformations are Python 2 compatible.

- `lib2to3.fixes.fix_apply <https://docs.python.org/3/library/2to3.html#2to3fixer-apply>`__
- `lib2to3.fixes.fix_except <https://docs.python.org/3/library/2to3.html#2to3fixer-except>`__
- `lib2to3.fixes.fix_exec <https://docs.python.org/3/library/2to3.html#2to3fixer-exec>`__
- `lib2to3.fixes.fix_execfile <https://docs.python.org/3/library/2to3.html#2to3fixer-execfile>`__
- `lib2to3.fixes.fix_exitfunc <https://docs.python.org/3/library/2to3.html#2to3fixer-exitfunc>`__
- `lib2to3.fixes.fix_funcattrs <https://docs.python.org/3/library/2to3.html#2to3fixer-funcattrs>`__
- `lib2to3.fixes.fix_has_key <https://docs.python.org/3/library/2to3.html#2to3fixer-has_key>`__
- `lib2to3.fixes.fix_idioms <https://docs.python.org/3/library/2to3.html#2to3fixer-idioms>`__
- `lib2to3.fixes.fix_long <https://docs.python.org/3/library/2to3.html#2to3fixer-long>`__
- `lib2to3.fixes.fix_methodattrs <https://docs.python.org/3/library/2to3.html#2to3fixer-methodattrs>`__
- `lib2to3.fixes.fix_ne <https://docs.python.org/3/library/2to3.html#2to3fixer-ne>`__
- `lib2to3.fixes.fix_numliterals <https://docs.python.org/3/library/2to3.html#2to3fixer-numliterals>`__
- `lib2to3.fixes.fix_operator <https://docs.python.org/3/library/2to3.html#2to3fixer-operator>`__
- `lib2to3.fixes.fix_paren <https://docs.python.org/3/library/2to3.html#2to3fixer-paren>`__
- `lib2to3.fixes.fix_reduce <https://docs.python.org/3/library/2to3.html#2to3fixer-reduce>`__
- `lib2to3.fixes.fix_repr <https://docs.python.org/3/library/2to3.html#2to3fixer-repr>`__
- `lib2to3.fixes.fix_set_literal <https://docs.python.org/3/library/2to3.html#2to3fixer-set_literal>`__
- `lib2to3.fixes.fix_standarderror <https://docs.python.org/3/library/2to3.html#2to3fixer-standarderror>`__
- `lib2to3.fixes.fix_sys_exc <https://docs.python.org/3/library/2to3.html#2to3fixer-sys_exc>`__
- `lib2to3.fixes.fix_throw <https://docs.python.org/3/library/2to3.html#2to3fixer-throw>`__
- `lib2to3.fixes.fix_tuple_params <https://docs.python.org/3/library/2to3.html#2to3fixer-tuple_params>`__
- `lib2to3.fixes.fix_types <https://docs.python.org/3/library/2to3.html#2to3fixer-types>`__
- `lib2to3.fixes.fix_ws_comma <https://docs.python.org/3/library/2to3.html#2to3fixer-ws_comma>`__
- `lib2to3.fixes.fix_xreadlines <https://docs.python.org/3/library/2to3.html#2to3fixer-xreadlines>`__


Fixers with no dependencies
+++++++++++++++++++++++++++

libmodernize.fixes.fix_file
'''''''''''''''''''''''''''

Changes all calls to ``file()`` to ``open()``.


libmodernize.fixes.fix_import
'''''''''''''''''''''''''''''

Changes a implicit relative import to explicit relative imports and adds
``from __future__ import absolute_import``.


libmodernize.fixes.fix_next
'''''''''''''''''''''''''''

Changes all method calls to ``x.next()`` to ``next(x)``.


libmodernize.fixes.fix_print
''''''''''''''''''''''''''''

Changes all usage of the ``print`` statement to use the ``print()`` function
and adds ``from __future__ import print_function``.


libmodernize.fixes.fix_raise
''''''''''''''''''''''''''''

Changes comma-based ``raise`` statements from::

    raise E, V
    raise (((E, E1), E2), E3), V

to::

    raise E(V)  # raise E, V
    raise E(V)  # raise (((E, E1), E2), E3), V



Opt-in
------

To specify an opt-in fixer while also running all the default fixers, make sure
to specify the ``all`` fixer, e.g.::

    python-modernize -f all -f libmodernize.fixes.fix_open


libmodernize.fixes.fix_open
+++++++++++++++++++++++++++

When a call to ``open()`` is discovered, add ``from io import open`` at the top
of the module. This fixer is opt-in because it changes what object is returned
by a call to `open()`: ``io.TextIOWrapper``.


Indices and tables
//////////////////

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. _project website: https://github.com/python-modernize/python-modernize
.. _modernize: https://pypi.python.org/pypi/modernize
.. _six project: http://pythonhosted.org/six
