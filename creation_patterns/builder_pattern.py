from abc import ABC, abstractmethod

# Product
class Vehicle(ABC):
    pass

class Car(Vehicle):
    def __init__(self, id, brand, model, color):
        self._id = id
        self._brand = brand
        self._model = model
        self._color = color
    
    def __str__(self):
        return f"Car(id={self._id}, brand={self._brand}, model={self._model}, color={self._color})"


class CarSchema(Vehicle):
    def __init__(self, id, brand, model, color):
        self._id = id
        self._brand = brand
        self._model = model
        self._color = color

    def __str__(self):
        return f"CarSchema(id={self._id}, brand={self._brand}, model={self._model}, color={self._color})"

# End of products

# Builders
class Builder(ABC):  
    def set_id(self, id: int):
        self._id = id
    
    def set_brand(self, brand: str):
        self._brand = brand
    
    def set_model(self, model: str):
        self._model = model
    
    def set_color(self, color: str):
        self._color = color
    
    @abstractmethod
    def build(self):
        pass
    

class CarBuilder(Builder):
   def build(self):
       return Car(self._id, self._brand, self._model, self._color)


class CarSchemaBuilder(Builder):
    def build(self):
        return CarSchema(self._id, self._brand, self._model, self._color)

# End of Builders


class Director:
    def __init__(self, builder: Builder):
        self._builder = builder
    
    def build_bugatti(self) -> Vehicle:
        self._builder.set_id(1)
        self._builder.set_brand('Bugatti')
        self._builder.set_model("Veyron")
        self._builder.set_color('black')
        return self._builder.build()
    
    def build_lamborgine(self) -> Vehicle:
        self._builder.set_id(1)
        self._builder.set_brand('Lamborgine')
        self._builder.set_model("Gallardo")
        self._builder.set_color('white')
        return self._builder.build()
    


director = Director(builder=CarBuilder())
bugatti = director.build_bugatti()
print(bugatti)