import json
from inspect import Parameter, signature
from typing import TypeVar, Type

import yaml

T = TypeVar('T')
U = TypeVar('U')


class ConfigDecoder:

    @staticmethod
    def __decode(clazz: Type[T]) -> T:

        def is_simple_type(t: type) -> bool:
            return t == str or t == int or t == float or t == bool

        def is_not_self(p: Parameter) -> bool:
            return not p.name == 'self'

        def check_same_type(_dict: dict, param: Parameter):
            if not (type(_dict[param.name]) == param.annotation):
                raise TypeError(
                    f'provided value for "{param.name}" ({_dict[param.name]} as {type(_dict[param.name])}) has not the right type {param.annotation}')

        def check_must_exist_in_dict(_dict: dict, param: Parameter):
            if param.default == Parameter.empty and param.name not in _dict:
                raise KeyError(f'Missing mandatory key ({param.name})')

        def process(_dict: dict, param: Parameter):
            if is_simple_type(param.annotation):
                check_must_exist_in_dict(_dict, param)
                return process_simple_type(_dict, param)
            elif type(_dict[param.name]) == list:
                return process_list(_dict, param)
            else:
                check_must_exist_in_dict(_dict, param)
                return process_object(_dict, param)

        def process_simple_type(_dict: dict, param: Parameter):
            if (param.name not in _dict) and (not param.default == Parameter.empty):
                return param.default
            else:
                check_same_type(_dict, param)
                return _dict[param.name]

        def process_list(_dict: dict, param: Parameter):
            if is_simple_type(param.annotation.__args__[0]):
                return [elem for elem in _dict[param.name]]
            else:
                return [ConfigDecoder.__decode(param.annotation.__args__[0])(elem) for elem in _dict[param.name]]

        def process_object(_dict: dict, param: Parameter):
            return ConfigDecoder.__decode(param.annotation)(_dict[param.name])

        def _decoder(_dict: dict):
            constructor = signature(clazz.__init__)
            params = [process(_dict, param) for param in constructor.parameters.values() if is_not_self(param)]
            return clazz(*params)

        return _decoder

    @staticmethod
    def decode_from_json(clazz: Type[U], stream: str | bytes | bytearray) -> U:
        return json.loads(stream, object_hook=ConfigDecoder.__decode(clazz))

    @staticmethod
    def decode_from_yaml(clazz: Type[U], stream: str | bytes | bytearray) -> U:
        return ConfigDecoder.__decode(clazz)(yaml.safe_load(stream))
