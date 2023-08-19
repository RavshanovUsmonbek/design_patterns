from abc import ABC, abstractmethod


# implementations
class Device(ABC):
    @abstractmethod
    def shoot(self):
        pass


class DSLCamera(Device):
    def shoot(self):
        return "DSL Camera"


class RegularCamera(Device):
    def shoot(self):
        return "Regular Camera"


# abstraction
class StreamingService(ABC):
    def __init__(self, device: Device):
        self.device = device
    
    @abstractmethod
    def stream(self):
        pass
    

class TwitchStreaming(StreamingService):
    def stream(self):
        return "Streaming on Twitch with {}".format(self.device.shoot())


class YoutubeStreaming(StreamingService):
    def stream(self):
        return "Streaming on Youtube with {}".format(self.device.shoot())
    


if __name__ == "__main__":
    dsl_cam = DSLCamera()
    regular_cam = RegularCamera()
    
    twitch_service = TwitchStreaming(dsl_cam)
    youtube_service = YoutubeStreaming(regular_cam)
    
    print(twitch_service.stream())
    print(youtube_service.stream())