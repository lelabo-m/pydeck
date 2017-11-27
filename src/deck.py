from .pile import Pile


class Deck(object):

    def __init__(self):
        self.stock_stack = Pile()
        self.discard_stack = Pile()

    def deal(self, numbers=1):
        pass

    def discard(self, objects):
        pass

    def shuffle(self):
        self.stock_stack.shuffle()

    def build(self):
        pass
