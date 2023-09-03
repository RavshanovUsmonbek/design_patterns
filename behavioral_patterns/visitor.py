from abc import ABC, abstractmethod
from math import pi
from typing import List


# Components
class Component(ABC):
    @abstractmethod
    def accept(self, visitor: "Visitor"):
        pass
    

class Rectangle(Component):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def accept(self, visitor: "Visitor"):
        visitor.visit_rectangle(self)


class Square(Component):
    def __init__(self, side):
        self.side = side
    
    def accept(self, visitor: "Visitor"):
        visitor.visit_square(self)


class Circle(Component):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor: "Visitor"):
        visitor.visit_circle(self)
        

# Visitor part
class Visitor(ABC):
    @abstractmethod
    def visit_rectangle(self, element: Rectangle):
        pass
    
    @abstractmethod
    def visit_circle(self, element: Circle):
        pass
    
    @abstractmethod
    def visit_square(self, element: Square):
        pass


class AreaCalculateVisitor(Visitor):
    def visit_rectangle(self, element: Rectangle):
        result = element.width * element.height
        print(f"AREA of {element}: {result}")
        return result
    
    def visit_square(self, element: Square):
        result = element.side * element.side
        print(f"AREA of {element}: {result}")
        return result
    
    def visit_circle(self, element: Circle):
        result = pi * element.radius * element.radius
        print(f"AREA of {element}: {result}")
        return result
    

class PerimeterCalculateVisitor(Visitor):
    def visit_circle(self, element: Circle):
        result = 2 * pi * element.radius
        print(f"Perimeter of {element}: {result}")
        return result
    
    def visit_rectangle(self, element: Rectangle):
        result = element.height + element.width
        print(f"Perimeter of {element}: {result}")
        return result
    
    def visit_square(self, element: Square):
        result = 2 * element.side
        print(f"Perimeter of {element}: {result}")
        return result


def client_code(components: List[Component], visitor: Visitor):
    for comp in components:
        comp.accept(visitor)


if __name__ == "__main__":
    components = [Rectangle(3, 4), Square(3), Circle(2)]
    area_visitor = AreaCalculateVisitor()
    perimeter_visitor = PerimeterCalculateVisitor()
    client_code(components, area_visitor)
    client_code(components, perimeter_visitor)
    
    

