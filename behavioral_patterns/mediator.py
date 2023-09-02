from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, payload):
        pass


class FanOutMediator(Mediator):
    def __init__(self):
        self._components = set()
        
    def add(self, component):
        self._components.add(component)
    
    def notify(self, payload):
        origin = payload['origin']
        for comp in self._components:
            if not comp == origin:
                comp.receive(payload['value']) 


class Component(ABC):    
    def __init__(self, mediator: Mediator, name):
        self._mediator = mediator
        self._name = name
    
    @abstractmethod
    def notify(self, message: str):
        pass
    
    @abstractmethod
    def receive(self, message: str):
        pass

    def get_payload(self, message):
        return {"origin": self, "value": message}


class ComponentA(Component):    
    def notify(self, message):
        print(f"Sending data from {self._name}: {message}")
        self._mediator.notify(self.get_payload(message))
    
    def receive(self, message):
        print(f"Handling data in {self._name}: {message}")


class ComponentB(Component):
    def notify(self, message):
        print(f"Sending data from {self._name}: {message}")
        self._mediator.notify(self.get_payload(message))
        
    def receive(self, message):
        print(f"Handling data in {self._name}: {message}")


if __name__ == "__main__":
    mediator = FanOutMediator()
    component_a = ComponentA(mediator, "COMP_A")
    component_b = ComponentB(mediator, "COMP_B")
    mediator.add(component_a)
    mediator.add(component_b)
    
    component_a.notify("HELLO")
    component_b.notify("BYE")