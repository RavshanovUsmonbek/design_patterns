## Subsystems
class Subsystem1:
    def operation1(self):
        return "Subsystem1 operation1"

    def operation2(self):
        return "Subsystem1 operation2"


class Subsystem2:
    def operation1(self):
        return "Subsystem2 operation1"

    def operation2(self):
        return "Subsystem2 operation2"


# Facade class
class Facade:
    
    def __init__(self, subsystem1: Subsystem1 = None, subsystem2: Subsystem2 = None):
        self._sub1 = subsystem1 or Subsystem1()
        self._sub2 = subsystem2 or Subsystem2()
    
    
    def operation1(self):
        return self._sub1.operation1()+ " " + self._sub1.operation2()
    
    def operation2(self):
        return self._sub2.operation1() + " " + self._sub2.operation2()

    def operation(self):
        return self.operation1() + " " + self.operation2()



if __name__ == "__main__":
    facade = Facade()
    result = facade.operation()
    print(result)