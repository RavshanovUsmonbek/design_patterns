from abc import ABC, abstractmethod


class Burger(ABC):
    @abstractmethod
    def prepare(self):
        pass


class BeefBurger(Burger):
    def prepare(self):
        print("Beef burger is being prepared...")


class VeggieBurger(Burger):
    def prepare(self):
        print("Veggie burger is being prepared...")


class Resturant(ABC):
    def order_burger(self) -> Burger:
        burger: Burger = self.create_burger()
        burger.prepare()
        return burger
    
    @abstractmethod
    def create_burger(self) -> Burger:
        pass


class BeefBurgerResturant(Resturant):
    def create_burger(self) -> Burger:
        return BeefBurger()


class VeggieBurgerResturant(Resturant):
    def create_burger(self) -> Burger:
        return VeggieBurger()



beef_burger = BeefBurgerResturant().order_burger()

veggie_burger = VeggieBurgerResturant().order_burger()

