from abc import ABC, abstractmethod


# Strategies 
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(Flyable):
    def fly(self):
        print("Flying with fings")


class NoFly(Flyable):
    def fly(self):
        print("No fly behavior")


# Context
class Duck(ABC):
    def __init__(self, behavior: Flyable):
        self._flying_behavior = behavior
    
    @property
    def flying_behavior(self) -> Flyable:
        return self._flying_behavior

    @flying_behavior.setter
    def flying_behavior(self, behavior: Flyable) -> None:
        self._flying_behavior = behavior

    @abstractmethod
    def fly(self):
        self.flying_behavior.fly()


class WildDuck(Duck):
    def __init__(self):
        super().__init__(FlyWithWings())
    
    def fly(self):
        return super().fly()


class CityDuck(Duck):
    def __init__(self):
        super().__init__(NoFly())
    
    def fly(self):
        return super().fly()


if __name__ == "__main__":
    city_dock = CityDuck()
    city_dock.fly()
    
    wild_duck = WildDuck()
    wild_duck.fly()

    