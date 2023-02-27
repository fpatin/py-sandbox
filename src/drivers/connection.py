import socket


class Connection(object):

    def __init__(self, client: socket):
        self.client = client

    def recv(self, buffer_size: int) -> bytes:
        return self.client.recv(buffer_size)
