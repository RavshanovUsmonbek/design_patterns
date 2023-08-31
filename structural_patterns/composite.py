from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    
    @abstractmethod
    def execute(self):
        pass


class Leaf(Component):
    def execute(self):
        return 1


class Composite(Component):
    def __init__(self) -> None:
        self._children: List[Component] = []
    
    
    def add(self, component: Component):
        self._children.append(component)
    
    def remove(self, component: Component):
        self._children.remove(component)
    
    def get_by_index(self, index):
        try:
            return self._children[index]
        except Exception as e:
            return -1
    
    def execute(self) -> int:
        return 1 + sum(comp.execute() for comp in self._children)


def client_code():
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)
    
    print(f"RESULT: {tree.execute()}")


client_code()

            