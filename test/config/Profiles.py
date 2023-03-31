from typing import Dict


class Profile:
    __slots__ = ("_suffixes", "_nb")

    def __init__(self, suffixes: list[str], nb: int):
        self._suffixes = suffixes
        self._nb = nb

    @property
    def suffixes(self) -> list[str]:
        return self._suffixes

    @property
    def nb(self) -> int:
        return self._nb


class MainConfig:
    __slots__ = ("_profiles")

    def __init__(self, profiles: Dict[str, Profile]):
        self._profiles = profiles

    @property
    def profiles(self) -> Dict[str, Profile]:
        return self._profiles
