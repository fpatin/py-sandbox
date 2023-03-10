from test.config.sub_driver_config import SubDriverConfig


class ComplexDriverConfig(object):
    __slots__ = ('_sub_driver_config', '_servers', '_buffer_size', '_names')  # Replace the instance dictionary

    def __init__(self, sub_driver_config: SubDriverConfig, servers: list[SubDriverConfig], names: list[str],
                 buffer_size: int = 2048):
        self._sub_driver_config = sub_driver_config
        self._servers = servers
        self._names = names
        self._buffer_size = buffer_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(sub_driver_config={self.sub_driver_config},servers={self.servers},names={self.names},buffer_size={self.buffer_size})"

    @property
    def sub_driver_config(self) -> SubDriverConfig:
        return self._sub_driver_config

    @property
    def servers(self) -> list[SubDriverConfig]:
        return self._servers

    @property
    def names(self) -> list[str]:
        return self._names

    @property
    def buffer_size(self) -> int:
        return self._buffer_size
