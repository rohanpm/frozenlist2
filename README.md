frozenlist2
===========

An immutable list.

![Build status](https://github.com/rohanpm/frozenlist2/workflows/Python%20tests/badge.svg?branch=master&event=push)
[![Coverage Status](https://coveralls.io/repos/github/rohanpm/frozenlist2/badge.svg?branch=master)](https://coveralls.io/github/rohanpm/frozenlist2?branch=master)

- [Source](https://github.com/rohanpm/frozenlist2)
- [Documentation](https://rohanpm.github.io/frozenlist2/)
- [PyPI](https://pypi.org/project/frozenlist2)

This library provides a simple immutable list class for Python.

- drop-in replacement for `list`
- hashable (if list contents are hashable)

Installation
------------

Install the `frozenlist2` package from PyPI.

```
pip install frozenlist2
```

Usage Example
-------------


```python
from frozenlist2 import frozenlist

# Make a list
elems = frozenlist([1, 2, 4, 8])

# Attempt to modify it
elems.append(16)  # Will raise exception!
```

License
-------

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
