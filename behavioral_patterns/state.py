from abc import ABC, abstractmethod


class State(ABC):
    
    @property
    def context(self):
        return self._context
    
    @context.setter
    def context(self, context):
        self._context = context
    
    @abstractmethod
    def publish(self):
        pass


# Context:
class Document:
    def __init__(self, state: State):
        self.update_state(state)
    
    def update_state(self, state: State):
        self._state = state
        self._state.context = self

    def publish(self):
        self._state.publish()


# Concrete State 
class Public(State):
    def publish(self):
        print("Document is already in public")


class Moderation(State):
    def publish(self):
        print("Moved from moderation to public")
        self.context.update_state(Public())


class Draft(State):
    def publish(self):
        print("Moved from draft to moderation")
        self.context.update_state(Moderation())


if __name__ == "__main__":
    document = Document(Draft())
    document.publish()
    document.publish()
    document.publish()
