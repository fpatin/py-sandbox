import socket

from src.drivers.connection import Connection
from test.config.driver_config import DriverConfig


# https://www.geeksforgeeks.org/with-statement-in-python/
# https://docs.python.org/fr/3/howto/sockets.html
class Driver(object):

    def __init__(self, config: DriverConfig, first_char: str | None = None):
        self.host = config.host
        self.port = config.port
        self.buffer_size = config.buffer_size
        self.first_char = first_char
        self.client = None

    def __enter__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.host, self.port))
        return Connection(self.client)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()
