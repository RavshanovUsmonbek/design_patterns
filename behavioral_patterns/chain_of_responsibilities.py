from abc import ABC, abstractmethod


class Handler(ABC):
    
    @abstractmethod
    def set_next(self, handler: "Handler") -> "Handler":
        pass

    @abstractmethod
    def handle(self, request):
        pass
    

class BaseHandler(Handler):
    
    _next_handler: Handler = None
    
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler
    
    @abstractmethod
    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)


# Concrete Handlers
class MonkeyHandler(BaseHandler):
    def handle(self, request):
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        return super().handle(request)


class SquirrelHandler(BaseHandler):
    def handle(self, request):
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        return super().handle(request)


class DogHandler(BaseHandler):
    def handle(self, request):
        if request == "Bone":
            return f"Dog: I'll eat the {request}"
        return super().handle(request)


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)
    
    for meal in ("Bone", "Nut", "Banana"):
        result = monkey.handle(meal)
        print(result)