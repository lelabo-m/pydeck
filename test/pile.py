from src.generic import Pile


def test_init():
    new_pile = Pile()
    assert new_pile.empty()


def test_add_and_remove():
    new_pile = Pile()
    new_pile.put(42)
    assert not new_pile.empty()
    assert new_pile.members[0] == 42
    assert new_pile.size == 1
    assert new_pile.see() == 42
    value = new_pile.get()
    assert new_pile.empty()
    assert new_pile.size == 0
    assert value == 42
    assert not new_pile.see()
    assert not new_pile.get()


def test_fill_and_clean():
    new_pile = Pile()
    for x in range(100):
        new_pile.put(x)
    assert new_pile.size == 100
    assert not new_pile.empty()
    for x in range(100):
        assert new_pile.see(x) == (99 - x)
    new_pile.clean()
    assert new_pile.empty()
    assert new_pile.size == 0


def test_fill_and_clean2():
    new_pile = Pile()
    for x in range(100):
        new_pile.put_below(x)
    assert new_pile.size == 100
    assert not new_pile.empty()
    for x in range(100):
        assert new_pile.see(x) == x
    new_pile.clean()
    assert new_pile.empty()
    assert new_pile.size == 0
