from pytest import raises

from frozenlist2 import frozenlist


def test_no_append():
    x = frozenlist()
    with raises(NotImplementedError):
        x.append(1)


def test_no_setitem():
    x = frozenlist([0])
    with raises(NotImplementedError):
        x[0] = 1234


def test_no_delitem():
    x = frozenlist([0])
    with raises(NotImplementedError):
        del x[0]


def test_no_iadd():
    x = frozenlist()
    with raises(NotImplementedError):
        x += [1]


def test_no_insert():
    x = frozenlist()
    with raises(NotImplementedError):
        x.insert(0, 123)


def test_no_sort():
    x = frozenlist([7, 5, 3])
    with raises(NotImplementedError):
        x.sort()


def test_no_extend():
    x = frozenlist()
    with raises(NotImplementedError):
        x.extend([1, 2, 3])


def test_no_pop():
    x = frozenlist([1, 2, 3])
    with raises(NotImplementedError):
        x.pop()


def test_no_remove():
    x = frozenlist([1, 2, 3])
    with raises(NotImplementedError):
        x.remove(0)
