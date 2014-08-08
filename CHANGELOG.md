# Version 0.3

Changes since 0.2:

* New fixer for `raise E, V, T`, changed to `six.reraise(E, V, T)`
* New fixer for metaclasses, using `six.with_metaclass`
* Avoid adding redundant parentheses to `print(x)`
* Fixed bug where `__future__` imports were added multiple times
* Fixed bug where fixer for `zip()` was recognising `map()`
