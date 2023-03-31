import json
from inspect import Parameter, signature
from typing import TypeVar, Type

import yaml

Dest = TypeVar('Dest')
Value = TypeVar('Value')
 
class ConfigDecoder:

    def __is_not_self(p: Parameter) -> bool:
        return not p.name == 'self'

    def __handle_simple_type(clazz: Type[Dest], value: Value) -> Dest:
        if clazz != type(value):
            raise TypeError(f'value "{value}" is not of the right type.Expects "{clazz}", found "{type(value)}"')
        return clazz(value)
    
    def __is_simple_type(t: type) -> bool:
        return t == str or t == int or t == float or t == bool or t == dict

    def __process_dict_elem(param: Parameter, _dict: dict):
        if param.default == Parameter.empty and param.name not in _dict:
            raise KeyError(f'Missing mandatory key ({param.name})')
        # Bug : oublié pour upper lvl (valeurs par défaut KO)
        elif param.name not in _dict:
            return param.default
        else:
            return ConfigDecoder.__handle(param.annotation, _dict[param.name])

    def __handle_dict(clazz: Type[Dest], value: dict) -> Dest: 
        constructor = signature(clazz.__init__)
        params = [ConfigDecoder.__process_dict_elem(param, value) 
                  for param in constructor.parameters.values() 
                  if ConfigDecoder.__is_not_self(param)]
        return clazz(*params)

    def __is_list(clazz: type) -> bool:
        try:    
            return issubclass(clazz.__origin__, Sequence)
        except:
            return False
        
    # Bug : ne tient pas compte du type paramétré de la liste
    def __handle_list(clazz: Type[List[Dest]], value: list) -> List[Dest]:
            return [ConfigDecoder.__handle(clazz.__args__[0], el) for el in value]
   
    def __handle(clazz: Type[Dest], value: Value) -> Dest:
        if ConfigDecoder.__is_simple_type(clazz):
            return ConfigDecoder.__handle_simple_type(clazz, value)
        elif ConfigDecoder.__is_list(clazz):
            return ConfigDecoder.__handle_list(clazz, value)
        else:
            return ConfigDecoder.__handle_dict(clazz, value)
            
    @staticmethod
    def decode(clazz: Type[Dest]):
        def curried(value: Value) -> Dest:
            return ConfigDecoder.__handle(clazz, value)
        return curried

    # Bug : ne prends pas en charge les dict->class nestées (ex: {"a": 1, "b": {"c": "foo"}})
    @staticmethod
    def decode_from_json(clazz: Type[Dest], stream: str | bytes | bytearray) -> Dest:
        return ConfigDecoder.decode(clazz)(json.loads(stream))

    # Pas testé
    @staticmethod
    def decode_from_yaml(clazz: Type[U], stream: str | bytes | bytearray) -> U:
        return ConfigDecoder.__decode(clazz)(yaml.safe_load(stream))
