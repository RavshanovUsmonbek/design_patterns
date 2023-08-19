from threading import Lock, Thread
from typing import Any


class SingletonMeta(type):
    _instances = {}
    _lock = Lock()
    
    def __call__(cls, *args, **kwargs) -> Any:
        with cls._lock:
            if cls not in cls._instances:
                obj = super().__call__(*args, **kwargs)
                cls._instances[cls] = obj
        return cls._instances[cls]



class Singleton(metaclass=SingletonMeta):
    def __init__(self, value: str):
        self.value = value
        
    def some_business_logic(self):
        pass


def test_singleton(value):
    obj = Singleton(value)
    print(obj.value)


process1 = Thread(target=test_singleton, args=("FOO",))
process2 = Thread(target=test_singleton, args=("BAR",))
process1.start()
process2.start()
            