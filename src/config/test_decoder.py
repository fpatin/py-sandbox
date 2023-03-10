from src.config.complex_driver_config import ComplexDriverConfig
from src.config.config_decoder import ConfigDecoder

from src.config.driver_config import DriverConfig


def simple_example():
    print('JSON')
    json_ok_all_parameters = """{"host":"myhost","port":123,"buffer_size":1}"""
    print(f'\tjson_ok_all_parameters={json_ok_all_parameters}')
    result_json_ok_1: DriverConfig = ConfigDecoder.decode_from_json(DriverConfig, json_ok_all_parameters)
    print(f'\t\t{result_json_ok_1}')
    if isinstance(result_json_ok_1, DriverConfig):
        print(f'\t\tTest (json_ok_all_parameters) Success')
        print()
    else:
        raise Exception('Test (json_ok_all_parameters) failed')

    json_ok_mandatory = """{"host":"myhost","port":123}"""
    print(f'\tjson_ok_mandatory={json_ok_mandatory}')
    result_json_ok_2: DriverConfig = ConfigDecoder.decode_from_json(DriverConfig, json_ok_mandatory)
    print(f'\t\t{result_json_ok_2}')
    if isinstance(result_json_ok_2, DriverConfig):
        print(f'\t\tTest (json_ok_mandatory) Success')
        print()
    else:
        raise Exception('Test (json_ok_mandatory) failed')

    try:
        json_ko_different_type = """{"host":"myhost","port":"123","buffer_size":1}"""
        print(f'\tjson_ko_different_type={json_ko_different_type}')
        result_json_ko_different_type: DriverConfig = ConfigDecoder.decode_from_json(DriverConfig,
                                                                                     json_ko_different_type)
        print(f'\t\t{result_json_ko_different_type}')
        print(f'\t\tresult json_ko_different_type={isinstance(result_json_ko_different_type, DriverConfig)}')
        raise Exception('Test (json_ko_different_type) failed')
    except Exception as e:
        print(e)
        print(f'\t\tTest (json_ko_different_type) Success')

    print()
    print('YAML')
    yaml_ok_all_parameters = """
                host: myhost2
                port: 123
                buffer_size: 1
            """
    print(f'\tyaml_ok_all_parameters={yaml_ok_all_parameters}')
    result_yaml_ok_all_parameters: DriverConfig = ConfigDecoder.decode_from_yaml(DriverConfig, yaml_ok_all_parameters)
    print(f'\t\t{result_yaml_ok_all_parameters}')
    if isinstance(result_yaml_ok_all_parameters, DriverConfig):
        print(f'\t\tTest (yaml_ok_all_parameters) Success')
        print()
    else:
        raise Exception('Test (yaml_ok_all_parameters) failed')

    yaml_ok_mandatory = """
                    host: myhost2
                    port: 123
                """
    print(f'\tyaml_ok_mandatory={yaml_ok_mandatory}')
    result_yaml_ok_mandatory: DriverConfig = ConfigDecoder.decode_from_yaml(DriverConfig, yaml_ok_mandatory)
    print(f'\t\t{result_yaml_ok_mandatory}')
    if isinstance(result_yaml_ok_mandatory, DriverConfig):
        print(f'\t\tTest (yaml_ok_mandatory) Success')
        print()
    else:
        raise Exception('Test (yaml_ok_mandatory) failed')

    try:
        yaml_different_type = """
                host: 2
                port: 123
            """
        print(f'yaml_different_type={yaml_different_type}')
        result_yaml_different_type: DriverConfig = ConfigDecoder.decode_from_yaml(DriverConfig, yaml_different_type)
        print(f'\t\t{result_yaml_different_type}')
        print(f'result yaml_different_type={isinstance(result_yaml_different_type, DriverConfig)}')
        raise Exception('Test (yaml_different_type) failed')
    except Exception as e:
        print(e)
        print(f'\t\tTest (yaml_different_type) Success')
        print()


def complex_example():
    print('Complex object')
    yaml_complex_ok_all_parameters = """
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
    print(f'yaml_different_type={yaml_complex_ok_all_parameters}')
    result_yaml_complex_ok_all_parameters: ComplexDriverConfig = ConfigDecoder.decode_from_yaml(ComplexDriverConfig,
                                                                                                yaml_complex_ok_all_parameters)
    print(f'\t\t{result_yaml_complex_ok_all_parameters}')
    if isinstance(result_yaml_complex_ok_all_parameters, ComplexDriverConfig):
        print(f'\t\tTest (yaml_complex_ok_all_parameters) Success')
    else:
        raise Exception('Test (yaml_complex_ok_all_parameters) failed')


if __name__ == '__main__':
    simple_example()
    complex_example()
