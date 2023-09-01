from abc import ABC, abstractmethod


class Receiver:
    """
        The Receiver classes contain some important business logic. They know how to
        perform all kinds of operations, associated with carrying out a request. In
        fact, any class may serve as a Receiver.
    """
    
    def to_string(self, value):
        return "Converted from receiver " + str(value)
    
    def handle(self, payload):
        handler = payload["handler"]
        return getattr(self, handler)(payload['value'])


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    """Simple commands can implement operations on their own"""

    def __init__(self, payload):
        self.payload = payload
    
    def execute(self):
        return f"Printing payload: {self.payload}"


class ComplexCommand(Command):
    "Complex Command transmits execution of operation to Receiver"
    
    def __init__(self, reciever: Receiver, payload: dict):
        self._reciever = reciever
        self._payload = payload
    
    
    def execute(self):
        return self._reciever.handle(self._payload)


class Invoker:
    
    def set_transformer(self, command: Command):
        self._transformer = command
    
    
    def do_stuff(self):
        print(self._transformer.execute())
    


if __name__ == "__main__":
    invoker = Invoker()
    invoker.set_transformer(SimpleCommand(545))
    invoker.do_stuff()
    
    receiver = Receiver()
    invoker.set_transformer(ComplexCommand(receiver, {
        "handler": "to_string",
        "value": 453.43
    }))
        
    invoker.do_stuff()        
        
        


