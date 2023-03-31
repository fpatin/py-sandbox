import unittest

from src.config.config_decoder import ConfigDecoder
from test.config.Profiles import MainConfig
from test.config.complex_driver_config import ComplexDriverConfig
from test.config.driver_config import DriverConfig


class ConfigDescriptorTest(unittest.TestCase):

    def test_with_json_dict(self) -> None:
        json = """{"profiles":{"1":{"suffixes":["un","deux"],"nb":1}}}"""
        result = ConfigDecoder.decode_from_json(MainConfig, json)
        print(result.profiles)
        self.assertIsInstance(result, MainConfig)

    def test_with_yaml_dict(self) -> None:
        json = """
                profiles:
                    1:
                        suffixes:
                            - un
                            - deux
                        nb : 1
                """
        result = ConfigDecoder.decode_from_yaml(MainConfig, json)
        print(result.profiles)
        self.assertIsInstance(result, MainConfig)


    def test_json_mandatory(self) -> None:
        json = """{"host":"myhost","port":123,"buffer_size":1}"""
        result = ConfigDecoder.decode_from_json(DriverConfig, json)
        self.assertIsInstance(result, DriverConfig)

    def test_json_ok_mandatory(self) -> None:
        json = """{"host":"myhost","port":123}"""
        result: DriverConfig = ConfigDecoder.decode_from_json(DriverConfig, json)
        self.assertIsInstance(result, DriverConfig)

    def test_different_type(self) -> None:
        json = """{"host":"myhost","port":"123","buffer_size":1}"""
        with self.assertRaises(TypeError):
            ConfigDecoder.decode_from_json(DriverConfig, json)

    def test_yaml_ok_all_parameters(self) -> None:
        yaml = """
                    host: myhost2
                    port: 123
                    buffer_size: 1
                """
        result: DriverConfig = ConfigDecoder.decode_from_yaml(DriverConfig, yaml)
        self.assertIsInstance(result, DriverConfig)

    def test_yaml_ok_mandatory(self) -> None:
        yaml = """
            host: myhost2
            port: 123
        """
        result: DriverConfig = ConfigDecoder.decode_from_yaml(DriverConfig, yaml)
        self.assertIsInstance(result, DriverConfig)

    def test_yaml_different_type(self) -> None:
        yaml = """
            host: 2
            port: 123
        """
        with self.assertRaises(TypeError):
            ConfigDecoder.decode_from_yaml(DriverConfig, yaml)

    def test_yaml_complex(self) -> None:
        yaml = """
                    sub_driver_config:
                        host: myhost2
                        port: 123
                    buffer_size: 1
                    servers:
                        - 
                            host: h1
                            port: 1
                        -
                            host: h2
                            port: 2
                    names:
                        - name1
                        - name2
                """
        result: ComplexDriverConfig = ConfigDecoder.decode_from_yaml(ComplexDriverConfig, yaml)
        self.assertIsInstance(result, ComplexDriverConfig)

    def test_yaml_complex_mandatory(self) -> None:
        yaml = """
                sub_driver_config:
                    host: myhost2
                    port: 123
                buffer_size: 1
                servers:
                    - 
                        host: h1
                        port: 1
                    -
                        host: h2
                        port: 2
                names: []
            """
        result: ComplexDriverConfig = ConfigDecoder.decode_from_yaml(ComplexDriverConfig, yaml)
        self.assertIsInstance(result, ComplexDriverConfig)
