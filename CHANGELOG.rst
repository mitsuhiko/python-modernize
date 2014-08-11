Version 0.3
===========

Changes since 0.2:
------------------

* New fixer for `raise E, V, T`, changed to `six.reraise(E, V, T)`.
* New fixer for metaclasses, using `six.with_metaclass`.
* Avoid adding redundant parentheses to `print(x)`.
* python-modernize can now be installed and run on Python 3.
* Fixed a bug where `__future__` imports were added multiple times.
* Fixed a bug where fixer for `zip()` was recognising `map()`.
