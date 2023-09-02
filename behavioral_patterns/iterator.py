from collections.abc import Iterable, Iterator
from typing import List


class WordsIterator(Iterator):
    
    _position = None
    
    def __init__(self, collection):
        self._collection = collection
        self._position = 0
        
    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += 1
            return value
        except IndexError:
            raise StopIteration()


class WordsCollection(Iterable):
    def __init__(self, collection: List = []):
        self._collection = collection
        
    def __iter__(self):
        return WordsIterator(self._collection)
    
    def add_word(self, word):
        self._collection.append(word)


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_word('Hello')
    collection.add_word("World")
    collection.add_word("frustration")
    collection.add_word("Hope")

    for word in collection:
        print(word)
