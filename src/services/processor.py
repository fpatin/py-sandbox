from src.drivers.driver import Driver
from src.parsers.parser import Parser


class Processor(object):
    def __init__(self, driver: Driver, parser: Parser):
        self.driver = driver
        self.parser = parser

    def run(self):
        with self.driver as connection:
            raw = self.parser.receive_message(connection)
            self.parser.parse(raw)
