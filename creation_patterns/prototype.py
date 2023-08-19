from copy import deepcopy


class Prototype:
    def __init__(self):
        self._objects = {}
    
    def register_object(self, name, obj):
        self._objects[name] = obj
    
    def unregister_object(self, name):
        del self._objects[name]
    
    def clone(self, name, attrs):
        obj = deepcopy(self._objects[name])
        obj.__dict__.update(attrs)
        return obj
    

class Car:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    
    def __str__(self):
        return f"Car({self.name}, {self.brand})"
    

lambo = Car('skylark', 'Lamborgine')
proto = Prototype()
proto.register_object('skylark', lambo)
lambo2 = proto.clone('skylark', {'name': "new skylark"})

print(f"CAR1 = {lambo}")
print(f"CAR2 = {lambo2}")
