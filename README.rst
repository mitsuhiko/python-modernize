::

    Python           _              _        
       _ __  ___  __| |___ _ _ _ _ (_)______ 
      | '  \/ _ \/ _` / -_) '_| ' \| |_ / -_)
      |_|_|_\___/\__,_\___|_| |_||_|_/__\___|

This library is a very thin wrapper around ``lib2to3`` to utilize it
to make Python 2 code more modern with the intention of eventually
porting it over to Python 3.

It does not guarantee, but it attempts to spit out a Python 2/3
compatible codebase.  The code that it generates has a runtime
dependency on ``six``, unless the ``--no-six`` option is used.

See the ``LICENSE`` file for the license of ``python-modernize``.
Using this tool does not affect licensing of the modernized code.


Unicode Literal Control:
------------------------

- By default modernize does not change Unicode literals at all, which means that
  you can take advantage of `PEP 414 <http://legacy.python.org/dev/peps/pep-0414/>`_.
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


.. image:: https://travis-ci.org/python-modernize/python-modernize.svg?branch=master
    :target: https://travis-ci.org/python-modernize/python-modernize
