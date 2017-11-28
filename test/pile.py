from src.generic import Pile


def test_init():
    new_pile = Pile()
    assert new_pile.empty()


def test_add_and_remove():
    new_pile = Pile()
    new_pile.put(42)
    assert new_pile.empty() == False
    assert new_pile.members[0] == 42
