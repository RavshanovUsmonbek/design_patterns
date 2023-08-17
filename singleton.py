class Borg:
    _shared_data = {}
    
    def __init__(self):
        self.__dict__ = self._shared_data


class Singleton(Borg):
    def __init__(self, **kwargs):
        super().__init__()
        self._shared_data.update(**kwargs)
    
    def __str__(self):
        return str(self._shared_data)



connection1 = Singleton(HTTP="Hyper Text Transform Protocol")

print(connection1)

connection2 = Singleton(SNMP="Simple Network Management Protocol")

print(connection2)