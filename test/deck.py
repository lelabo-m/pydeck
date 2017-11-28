from src import CardDeck, Card


def test_init():
    new_deck = CardDeck()
    assert not new_deck.empty()
    assert new_deck.size == 52


def test_deck_shuffle_and_deal():
    new_deck = CardDeck()
    new_deck.shuffle()
    print new_deck.stock_stack.size
    hand = new_deck.deal()
    print hand
    assert False
