# Flyweight class
class BookType:
    def __init__(self, type, press, description):
        self._type = type
        self._press = press
        self._description = description
    
    def __str__(self):
        return f"BookType(type={self._type}, press={self._press}, desc={self._description})"


# Flyweight Factory
class BookTypeFactory:
    _book_types = {}
    
    @classmethod
    def get_book_type(cls, name, press, desc):
        type = cls._book_types.get(name)
        if not type:
            cls._book_types[name] = BookType(name, press, desc)
        return cls._book_types[name]            


# Context
class Book:
    def __init__(self, name, price, book_type):
        self._name = name
        self._price = price
        self._book_type = book_type
    
    def __str__(self):
        return f"Book(name={self._name}, price={self._price}, type={id(self._book_type)})"    


if __name__ == "__main__":
    book_type = BookTypeFactory.get_book_type('fiction', 'penguin', 'fiction books')
    book1 = Book("Harry Potter", 78.99, book_type)
    book2 = Book("Hobbit", 67.89, book_type)
    print(book1)
    print(book2)
    
    
    