:tocdepth: 3

Python-Modernize
////////////////

.. toctree::
   :maxdepth: 2

   fixers


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
modernize_

A note about handling text literals
===================================

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

Indices and tables
//////////////////

* :ref:`genindex`
* :ref:`search`


.. _modernize: https://pypi.python.org/pypi/modernize
.. _project website: https://github.com/python-modernize/python-modernize
