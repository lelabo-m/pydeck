from .pile import Pile
import collections


class Deck(object):

    def __init__(self):
        self.stock_stack = Pile()
        self.discard_stack = Pile()
        self.build()

    def build(self):
        pass

    def __deal(self):
        if self.stock_stack.empty():
            if self.discard_stack.empty():
                return None
            self.discard_to_stock()
        return self.stock_stack.get()

    def deal(self, numbers=1):
        if numbers <= 1:
            return self.__deal()
        else:
            objects = []
            for x in range(numbers + 1):
                obj = self.__deal()
                if not obj:
                    break
                objects.append(obj)
            return objects

    def discard(self, objects):
        if isinstance(objects, collections.Iterable):
            for obj in objects:
                self.discard_stack.put(obj)
        else:
            self.discard_stack.put(objects)

    def discard_to_stock(self):
        self.discard_stack.shuffle()
        for obj in self.discard_stack.members:
            self.stock_stack.put(obj)
        self.discard_stack.clean()

    def shuffle(self):
        self.stock_stack.shuffle()

    def reset(self):
        self.stock_stack.clean()
        self.discard_stack.clean()
        self.build()
