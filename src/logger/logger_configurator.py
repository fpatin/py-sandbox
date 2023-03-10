import logging.config
import os
from pathlib import Path

import yaml


class LoggerConfigurator:
    @staticmethod
    def configure() -> None:
        config_file = LoggerConfigurator.__get_config_file()

        print(f"Loading logging configuration [{config_file}]...")
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)
        print("Logging configuration loaded")

    @staticmethod
    def __get_config_file() -> Path:
        return Path(os.environ['LOGGING_CONF']) if 'LOGGING_CONF' in os.environ else \
            Path(__file__).parent.joinpath('dev_logging.yml')
