from abc import ABC, abstractmethod

class IClient(ABC):
    @abstractmethod
    def request(self):
        pass


class Client(IClient):
    def request(self) -> str:
        return "Some function"



class Adaptee:
    """ 3-rd party code that needs to be adapted"""
    def specific_function(self):
        return "Incompatible response"


class Adapter(IClient):
    
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
    
    def request(self):
        third_party_response = self.adaptee.specific_function()
        compatible_response = third_party_response[2:]
        return compatible_response


adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())
