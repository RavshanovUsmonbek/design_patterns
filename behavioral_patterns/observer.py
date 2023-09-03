from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass
    

class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer: Observer):
        pass
    
    @abstractmethod
    def unsubscribe(self, observer: Observer):
        pass
    
    @abstractmethod
    def notify(self):
        pass



# Concrete observer and subjects
class Shop(Subject):
    
    def __init__(self):
        self._product_arrived = False
        self._observers: List[Observer] = []
    
    def subscribe(self, observer: Observer):
        return self._observers.append(observer)

    def unsubscribe(self, observer: Observer):
        return self._observers.remove(observer)
    
    def notify(self):
        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)
    
    def receive_products(self):
        self._product_arrived = True
        self.notify()
    
    @property
    def product_arrived(self):
        return self._product_arrived


class CustomerA(Observer):
    
    def __init__(self, name):
        self._name = name
    
    def buy_product(self):
        print(f"{self._name}: Buying product from Shop...")
    
    def update(self, subject: Subject):
        if subject.product_arrived:
            self.buy_product()



if __name__ == "__main__":
    shop = Shop()
    
    customer1 = CustomerA("Susan")
    customer2 = CustomerA("John")
    shop.subscribe(customer1)
    shop.subscribe(customer2)
    shop.receive_products()
    print("---------------\n")
    
    shop.unsubscribe(customer1)
    shop.receive_products()
    print("---------------\n")
    
    shop.unsubscribe(customer2)
    shop.receive_products()

        
    
    
