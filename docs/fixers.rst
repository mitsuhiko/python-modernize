Fixers
======

Fixers come in two types: Default_ and Opt-in_. Default fixers should not break
code except for corner cases and are idempotent. Opt-in fixers are allowed to
break these rules.

Python 2 code from Python 2.6 and older will be upgraded to code that is
compatible with Python 2.6, 2.7 and Python 3. If code is
using a feature unique to Python 2.7 it will not be downgraded to work with
Python 2.6, e.g. ``dict.viewitems()`` usage will not be removed to make the code
compatible with Python 2.6.

Some fixers rely on the latest release of the `six project`_ to work
(see `Fixers requiring six`_).
If you wish to turn off these fixers to avoid an external dependency on ``six``,
then use the ``--nosix`` flag.

Fixers use the API defined by 2to3. For details of how this works, and how to
implement your own fixers, see `Extending 2to3 with your own fixers, at
python3porting.com <http://python3porting.com/fixers.html>`_.


Default
-------

A default fixer will be used if:

- It is not listed in ``-x``/``--nofix``
- They are dependent on the `six project`_ and ``--nosix`` was **not** specified
  (see `Fixers requiring six`_)
- It is listed in ``-f``/``--fix`` either explicitly or ``all`` is specified


Fixers requiring six
++++++++++++++++++++

The `six project`_ provides the ``six`` module which contains various tidbits in
helping to support Python 2/3 code. All ``six``-related fixers assume the latest
version of ``six`` is installed.

.. 2to3fixer:: basestring

   Replaces all references to :func:`basestring` with :data:`six.string_types`.

   .. versionadded:: 0.4

.. 2to3fixer:: dict_six

   Fixes various methods on the ``dict`` type for getting all keys, values, or
   items. E.g.::

       x.values()
       x.itervalues()
       x.viewvalues()

   becomes::

       list(x.values())
       six.itervalues(x)
       six.itervalues(x)

   Care is taken to only call ``list()`` when not in an iterating context
   (e.g. not the iterable for a ``for`` loop).

.. 2to3fixer:: filter

   When a call to :func:`filter <python2:filter>` is discovered, ``from six.moves import filter`` is
   added to the module. Wrapping the use in a call to ``list()`` is done when
   necessary.

.. 2to3fixer:: imports_six

   Uses :mod:`six.moves` to fix various renamed modules, e.g.::

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

   .. versionadded:: 0.4

.. 2to3fixer:: input_six

   Changes::

       input(x)
       raw_input(x)

   to::

       from six.moves import input
       eval(input(x))
       input(x)

   .. versionadded:: 0.4

.. 2to3fixer:: int_long_tuple

   Changes ``(int, long)`` or ``(long int)`` to :data:`six.integer_types`.

   .. versionadded:: 0.4

.. 2to3fixer:: map

   If a call to :func:`map <python2:map>` is discovered, ``from six.moves import map`` is added to
   the module. Wrapping the use in a call to ``list()`` is done when necessary.

.. 2to3fixer:: metaclass

   Changes::

       class Foo:
           __metaclass__ = Meta

   to::

       import six
       class Foo(six.with_metaclass(Meta)):
           pass
    
   .. seealso::
      :func:`six.with_metaclass`

.. 2to3fixer:: raise_six

   Changes ``raise E, V, T`` to ``six.reraise(E, V, T)``.

.. 2to3fixer:: unicode_type

   Changes all reference of :func:`unicode <python2:unicode>` to
   :data:`six.text_type`.

.. 2to3fixer:: xrange_six

   Changes::

       w = xrange(x)
       y = range(z)

   to::

       from six.moves import range
       w = range(x)
       y = list(range(z))

   Care is taken not to call ``list()`` when ``range()`` is used in an iterating
   context.

.. 2to3fixer:: zip

   If :func:`zip <python2:zip>` is called, ``from six.moves import zip`` is added to the module.
   Wrapping the use in a call to ``list()`` is done when necessary.


``2to3`` fixers
+++++++++++++++

Some `fixers from lib2to3 <https://docs.python.org/3/library/2to3.html#fixers>`_
in Python's standard library are run by default unmodified as their
transformations are Python 2 compatible.

- :2to3fixer:`apply <python:apply>`
- :2to3fixer:`except <python:except>`
- :2to3fixer:`exec <python:exec>`
- :2to3fixer:`execfile <python:execfile>`
- :2to3fixer:`exitfunc <python:exitfunc>`
- :2to3fixer:`funcattrs <python:funcattrs>`
- :2to3fixer:`has_key <python:has_key>`
- :2to3fixer:`idioms <python:idioms>`
- :2to3fixer:`long <python:long>`
- :2to3fixer:`methodattrs <python:methodattrs>`
- :2to3fixer:`ne <python:ne>`
- :2to3fixer:`numliterals <python:numliterals>`
- :2to3fixer:`operator <python:operator>`
- :2to3fixer:`paren <python:paren>`
- :2to3fixer:`reduce <python:reduce>`
- :2to3fixer:`repr <python:repr>`
- :2to3fixer:`set_literal <python:set_literal>`
- :2to3fixer:`standarderror <python:standarderror>`
- :2to3fixer:`sys_exc <python:sys_exc>`
- :2to3fixer:`throw <python:throw>`
- :2to3fixer:`tuple_params <python:tuple_params>`
- :2to3fixer:`types <python:types>`
- :2to3fixer:`ws_comma <python:ws_comma>`
- :2to3fixer:`xreadlines <python:xreadlines>`

Fixers with no dependencies
+++++++++++++++++++++++++++

.. 2to3fixer:: file

   Changes all calls to :func:`file <python2:file>` to :func:`open <python2:open>`.

   .. versionadded:: 0.4

.. 2to3fixer:: import

   Changes implicit relative imports to explicit relative imports and adds
   ``from __future__ import absolute_import``.

   .. versionadded:: 0.4

.. 2to3fixer:: next

   Changes all method calls to ``x.next()`` to ``next(x)``.

.. 2to3fixer:: print

   Changes all usage of the ``print`` statement to use the :func:`print` function
   and adds ``from __future__ import print_function``.

.. 2to3fixer:: raise

   Changes comma-based ``raise`` statements from::

       raise E, V
       raise (((E, E1), E2), E3), V

   to::

       raise E(V)
       raise E(V)


Opt-in
------

To specify an opt-in fixer while also running all the default fixers, make sure
to specify the ``all`` fixer, e.g.::

    python-modernize -f all -f libmodernize.fixes.fix_open

.. 2to3fixer:: open

   When a call to :func:`open <python2:open>` is discovered, add ``from io import open`` at the top
   of the module so as to use :func:`io.open` instead. This fixer is opt-in because it
   changes what object is returned by a call to ``open()``.

   .. versionadded:: 0.4

.. _six project: http://pythonhosted.org/six
