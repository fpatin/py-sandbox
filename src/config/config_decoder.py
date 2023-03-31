import json
from inspect import Parameter, signature
from typing import TypeVar, Type, Sequence, List, Dict

import yaml

Dest = TypeVar('Dest')
Value = TypeVar('Value')


class ConfigDecoder:

    @staticmethod
    def __is_not_self(p: Parameter) -> bool:
        return not p.name == 'self'

    @staticmethod
    def __handle_simple_type(clazz: Type[Dest], value: Value) -> Dest:
        if clazz != type(value):
            raise TypeError(f'value "{value}" is not of the right type.Expects "{clazz}", found "{type(value)}"')
        return clazz(value)

    @staticmethod
    def __is_simple_type(t: type) -> bool:
        return t == str or t == int or t == float or t == bool

    @staticmethod
    def __process_dict_elem(param: Parameter, _dict: dict):
        if param.default == Parameter.empty and param.name not in _dict:
            raise KeyError(f'Missing mandatory key ({param.name})')
        elif param.name not in _dict:
            return param.default
        else:
            return ConfigDecoder.__handle(param.annotation, _dict[param.name])

    @staticmethod
    def __handle_object(clazz: Type[Dest], value: dict) -> Dest:
        constructor = signature(clazz.__init__)
        params = [ConfigDecoder.__process_dict_elem(param, value)
                  for param in constructor.parameters.values()
                  if ConfigDecoder.__is_not_self(param)]
        return clazz(*params)

    @staticmethod
    def __is_list(clazz: type) -> bool:
        try:
            return issubclass(clazz.__origin__, Sequence)
        except:
            return False

    @staticmethod
    def __is_dict(clazz: type) -> bool:
        try:
            return issubclass(clazz.__origin__, Dict)
        except:
            return False

    @staticmethod
    def __handle_list(clazz: Type[List[Dest]], value: list) -> List[Dest]:
        return [ConfigDecoder.__handle(clazz.__args__[0], el) for el in value]

    @staticmethod
    def __handle_dict(clazz: Type[Dict[str, Dest]], value: dict) -> Dict[str, Dest]:
        if clazz.__args__[0] != str:
            raise TypeError(f'class {clazz} must as str keys')

        keys = set([type(k) for k in value.keys()])
        if len(keys) != 1 or list(keys)[0] != str:
            raise TypeError("Keys must be str")
        else:
            return {k: ConfigDecoder.__handle(clazz.__args__[1], v) for (k, v) in value.items()}

    @staticmethod
    def __handle(clazz: Type[Dest], value: Value) -> Dest:
        if ConfigDecoder.__is_simple_type(clazz):
            return ConfigDecoder.__handle_simple_type(clazz, value)
        elif ConfigDecoder.__is_list(clazz):
            return ConfigDecoder.__handle_list(clazz, value)
        elif ConfigDecoder.__is_dict(clazz):
            return ConfigDecoder.__handle_dict(clazz, value)
        else:
            return ConfigDecoder.__handle_object(clazz, value)

    @staticmethod
    def decode(clazz: Type[Dest]):
        def curried(value: Value) -> Dest:
            return ConfigDecoder.__handle(clazz, value)

        return curried

    @staticmethod
    def decode_from_json(clazz: Type[Dest], stream: str | bytes | bytearray) -> Dest:
        return ConfigDecoder.decode(clazz)(json.loads(stream))

    @staticmethod
    def decode_from_yaml(clazz: Type[Dest], stream: str | bytes | bytearray) -> Dest:
        return ConfigDecoder.decode(clazz)(yaml.safe_load(stream))
