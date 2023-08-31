from abc import ABC, abstractmethod


class StreammingInterface(ABC):
    
    @abstractmethod
    def stream(self):
        pass


class Twitch(StreammingInterface):
    def stream(self):
        return "TWITCH IS STREAMING"


class StreamProxy(ABC):
    def __init__(self, streaming_service: StreammingInterface):
        self._real_service = streaming_service
    
    def check_access(self) -> bool:
        print("CHECKING USERS ACCESS RIGHTS...")
        return True
    
    def log_access(self) -> None:
        print("INFO: LOGGING ACTIVITY")
    
    def stream(self):
        if self.check_access():
            print(self._real_service.stream())
            self.log_access()



service = Twitch()

proxy = StreamProxy(service)

proxy.stream()


        
    
    
    
    