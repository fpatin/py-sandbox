from src.drivers.driver import Connection


class Parser(object):

    def __int__(self, buffer_size: int = 2048, first_char: str | None = None):
        self.first_char = first_char
        self.buffer_size = buffer_size

    def receive_message(self, connection: Connection) -> str:
        chunks = []
        bytes_received = -1
        first_char_check = self.first_char is None
        while bytes_received != 0:
            chunk = connection.recv(self.buffer_size)
            if first_char_check or chunk.decode('UTF-8').startswith(self.first_char):
                first_char_check = True
            else:
                raise Exception
            chunks.append(chunk)
            bytes_received = len(chunk)

        return b''.join(chunks).decode('UTF-8')

    def parse(self, s: str) -> None:
        pass
