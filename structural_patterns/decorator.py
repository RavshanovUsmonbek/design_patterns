from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    def operation(self):
        return "CONCRETE"


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component
    
    def operation(self):
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self):
        return "ConcreteDecoratorA__"+self.component.operation()


class ConcreteDecoratorB(Decorator):
    def operation(self):
        return "ConcreteDecoratorB__"+self.component.operation()



simple = ConcreteComponent()
decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
print(decorator2.operation())  