from abc import ABC, abstractmethod


class Pet(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def speak(self):
        pass


class Dog(Pet):
    def speak(self):
        return "Woof!"


class Cat(Pet):
    def speak(self):
        return "Meow"



def get_pet(pet="dog"):
    """ Factory Method """
    
    pets = dict(dog=Dog("Simba"), cat=Cat("Mosh"))
    return pets[pet]


c = get_pet("cat")
print(c.speak())

