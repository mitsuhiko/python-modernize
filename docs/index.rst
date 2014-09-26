.. modernize documentation master file, created by
   sphinx-quickstart on Fri Sep 26 08:36:35 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to modernize's documentation!
=====================================

.. toctree::
   :maxdepth: 2


Purpose of the project
//////////////////////

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
//////

Fixers come in two types: Default_ and Opt-in_. Default fixers should not break
code except for corner cases and are idempotent. Opt-in fixers are allowed to
break these rules.

Python 2 code from Python 2.6 and older will be upgraded to code that is
compatible with Python 2.6, 2.7 and the latest release of Python 3. If code is
using a feature unique to Pyth on 2.7 it will not be downgraded to work with
Python 2.6, e.g. ``dict.viewitems()`` usage will not be removed to make the code
compatible with Python 2.6.

Some fixers rely on the latest release of the `six project`_ to work
(see `Fixers requiring six`_).
If you wish to turn off these fixers to avoid an external dependency on ``six``,
then use the ``--nosix`` flag. It is **strongly** recommended, though, that you
do not do this


A note about handling text literals
+++++++++++++++++++++++++++++++++++

.. TODO Explain what a "native string" is if it is going to be referenced

- By default modernize does not change Unicode literals at all, which means that
  you can take advantage of
  `PEP 414 <http://legacy.python.org/dev/peps/pep-0414/>`_.
  This is the simplest option if you only want to support Python 3.3 and above
  along with Python 2.
- Alternatively, there is the ``--six-unicode`` flag which will wrap Unicode
  literals with the six helper function ``six.u()``. This is useful if you want
  to support Python 3.1 and Python 3.2 without bigger changes.
- The last alternative is the ``--future-unicode`` flag which
  imports the ``unicode_literals`` from the ``__future__`` module.
  This requires Python 2.6 and later, and will require that you
  mark bytestrings with ``b''`` and native strings in ``str('')``
  or something similar that survives the transformation.


Default
+++++++

A default fixer will be used if:

- They are not listed in ``-x``/``--nofix``
- They are listed in ``-f``/``--fix`` either explicitly or ``all`` is listed
- They are dependent on the `six project`_ and ``--nosix`` was specified
  (see `Fixers requiring six`_)


Fixers requiring six
--------------------

.. TODO List them and explain what they do

See fixers listed in
`libmodernize.fixes.six_fix_names <https://github.com/python-modernize/python-modernize/blob/master/libmodernize/fixes/__init__.py>`__.


``2to3`` fixers
---------------

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
---------------------------

.. TODO List them and explain what they do

All fixers found in
`libmodernize.fixes <https://github.com/python-modernize/python-modernize/tree/master/libmodernize/fixes>`__
but not listed somehow in
`libmodernize.fixes.__init__ <https://github.com/python-modernize/python-modernize/blob/master/libmodernize/fixes/__init__.py>`__.


Opt-in
++++++

.. TODO List them and explain what they do and why they are not run by default

See fixers listed in
`libmodernize.fixes.opt_in_fix_names <https://github.com/python-modernize/python-modernize/blob/master/libmodernize/fixes/__init__.py>`__.

To specify an opt-in fixer while also running all the default fixers, make sure
to specify the ``all`` fixer, e.g.::

    python-modernize -f all -f libmodernize.fixes.fix_open


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



.. _project website: https://github.com/python-modernize/python-modernize
.. _modernize: https://pypi.python.org/pypi/modernize
.. _six project: http://pythonhosted.org/six
