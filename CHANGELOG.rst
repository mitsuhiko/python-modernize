Version 0.3
===========

Changes since 0.2:

* New fixer for `raise E, V, T`, changed to `six.reraise(E, V, T)`.
* New fixer for metaclasses, using `six.with_metaclass`.
* Avoid adding redundant parentheses to `print(x)`.
* python-modernize can now be installed and run on Python 3.
* Fixed a bug where `__future__` imports were added multiple times.
* Fixed a bug where fixer for `zip()` was recognising `map()`.
* The default is now to leave Unicode literals unchanged.
  (In previous versions this required the ``--compat-unicode`` option,
  which has now been removed.) A new ``--six-unicode`` option has been
  added to obtain the previous behaviour of adding ``six.u`` wrappers
  around Unicode literals.
