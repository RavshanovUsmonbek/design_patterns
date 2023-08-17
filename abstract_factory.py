from abc import ABC, abstractmethod

# Abstract products
class Monitor(ABC):
    @abstractmethod
    def assemble(self):
        pass


class GPU(ABC):
    @abstractmethod
    def assemble(self):
        pass


# Concrete products
class MsiMonitor(Monitor):
    def assemble(self):
        return "MSI Monitor" 


class AsusMonitor(Monitor):
    def assemble(self):
        return "Asus Monitor"


class MsiGpu(GPU):
    def assemble(self):
        return "MSI GPU"


class AsusGpu(GPU):
    def assemble(self):
        return "Asus GPU"


# Abstract Creator
class Company(ABC):
    @abstractmethod
    def create_gpu(self)-> GPU:
        pass
    
    @abstractmethod
    def create_monitor(self) -> Monitor:
        pass


# Concrete creators
class MsiManifacturer(Company):
    def create_gpu(self):
        return MsiGpu()

    def create_monitor(self) -> Monitor:
        return MsiMonitor()


class AsusManifacturer(Company):
    def create_gpu(self):
        return AsusGpu()

    def create_monitor(self) -> Monitor:
        return AsusMonitor()


# Client code
def manifacture(factory: Company):
    gpu = factory.create_gpu()
    monitor = factory.create_monitor()
    
    print(gpu.assemble())
    print(monitor.assemble())


asus_manifacturer = AsusManifacturer()
msi_manifacturer = MsiManifacturer()
manifacture(asus_manifacturer)
manifacture(msi_manifacturer)
