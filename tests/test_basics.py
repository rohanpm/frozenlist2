from frozenlist2 import frozenlist


def test_equals_list():
    frozen = frozenlist(["a", "b", "c"])
    assert frozen == ["a", "b", "c"]
    assert frozen != ["a", "b", "d"]


def test_repr_list():
    frozen = frozenlist(["a", "b", "c"])
    assert repr(frozen) == repr(["a", "b", "c"])


def test_can_hash():
    frozen = frozenlist(["a", "b", "c"])
    assert hash(frozen)


def test_cannot_hash_with_mutable_elements():
    frozen = frozenlist(["a", "b", "c", {"d": "e"}])
    try:
        hash(frozen)
        raise AssertionError("Was expected to raise!")
    except TypeError:
        # expected behavior
        pass
