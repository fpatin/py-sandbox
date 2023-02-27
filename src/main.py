from src.config.driver_config import DriverConfig
from src.services.processor import Processor
from src.drivers.xml_driver import XMLDriver
from src.parsers.specific_parser import SpecificParser


def main(processor: Processor):
    processor.run()


if __name__ == '__main__':
    main(
        Processor(
            driver=XMLDriver(DriverConfig("host", 123)),
            parser=SpecificParser()
        )
    )
