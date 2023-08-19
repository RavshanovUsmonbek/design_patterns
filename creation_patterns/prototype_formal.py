from abc import ABC, abstractmethod
from copy import deepcopy

class Vehicle(ABC):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    def clone(self):
        return deepcopy(self)


class Car(Vehicle):
    def __init__(self, brand, model, color, top_speed):
        super().__init__(brand, model, color)
        self.top_speed = top_speed
    
    def __str__(self):
        return f"Car({self.brand},)"
        

class Bus(Vehicle):
    def __init__(self, brand, model, color, doors):
        super().__init__(brand, model, color)
        self.doors = doors



car1 = Car('lambo', 'gallordo', 'black', 220)
print(car1.clone())       