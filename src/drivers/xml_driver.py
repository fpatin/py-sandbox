from src.drivers.driver import Driver
from src.config.driver_config import DriverConfig


class XMLDriver(Driver):

    def __init__(self, config: DriverConfig):
        Driver.__init__(self, config, "<")
