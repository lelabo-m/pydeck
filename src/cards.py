from generic import Deck


class Card(object):

    def __init__(self, family, value):
        self.family = family
        self.value = value

    def __repr__(self):
        return "{}{}".format(self.value, self.family)


class CardDeck(Deck):

    def build(self):
        families = ["C", "D", "H", "S"]
        values = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
        for f in families:
            for v in values:
                self.stock_stack.put(Card(f, v))
