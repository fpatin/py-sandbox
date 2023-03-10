class SubDriverConfig(object):
    __slots__ = ('_host', '_port')  # Replace the instance dictionary

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port

    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self._host}\',{self._port})"

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port
