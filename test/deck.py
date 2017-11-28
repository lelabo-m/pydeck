from src import CardDeck, Card


def test_init():
    new_deck = CardDeck()
    assert not new_deck.empty()
    assert new_deck.size == 52


def test_deck_shuffle_and_deal():
    new_deck = CardDeck()
    new_deck.shuffle()
    hand = new_deck.deal()
    assert type(hand) == Card
    assert new_deck.remaining == 51
    new_deck.discard(hand)
    assert new_deck.remaining == 51
    assert new_deck.discarded == 1


def test_deal_many():
    new_deck = CardDeck()
    new_deck.shuffle()
    hand = new_deck.deal(10)
    assert len(hand) == 10
    assert new_deck.remaining == 42
    new_deck.discard(hand)
    assert new_deck.remaining == 42
    assert new_deck.discarded == 10


def test_deal_till_empty():
    new_deck = CardDeck()
    new_deck.shuffle()
    hand = new_deck.deal(52)
    assert len(hand) == 52
    assert new_deck.remaining == 0
    second_hand = new_deck.deal(3)
    assert not second_hand
    new_deck.discard(hand)
    assert new_deck.remaining == 0
    assert new_deck.discarded == 52
    second_hand = new_deck.deal(3)
    assert len(second_hand) == 3
    assert new_deck.remaining == 49
    assert new_deck.discarded == 0
    new_deck.discard(second_hand)
    assert new_deck.remaining == 49
    assert new_deck.discarded == 3

