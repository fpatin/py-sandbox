from collections import namedtuple


class DriverConfig(object):
    __slots__ = ('_host', '_port', '_buffer_size')  # Replace the instance dictionary

    def __init__(self, host: str, port: int, buffer_size: int = 2048):
        self._host = host
        self._port = port
        self._buffer_size = buffer_size

    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self._host}\',{self._port},{self._buffer_size})"

    @property
    def host(self) -> str:
        return self._host

    @property
    def port(self) -> int:
        return self._port

    @property
    def buffer_size(self) -> int:
        return self._buffer_size
