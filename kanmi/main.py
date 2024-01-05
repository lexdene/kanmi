from typing import Optional, Self

from .utils import random_string, sha1


class Kanmi:
    SPLITER = '#'
    SALT_LENGTH = 8

    def __init__(self, salt: str, hashed: str):
        self.salt = salt
        self.hashed = hashed

    @classmethod
    def hash(cls, source: str, salt: str) -> str:
        """
            you can subclass Kanmi and provide another hash function
        """
        return sha1(salt + cls.SPLITER + source)

    @classmethod
    def from_str(cls, s: str) -> Self:
        salt, hashed = s.split(cls.SPLITER)
        return cls(salt, hashed)

    def to_str(self) -> str:
        return self.salt + self.SPLITER + self.hashed

    @classmethod
    def create(cls, source: str, salt: Optional[str]=None) -> Self:
        if salt is None:
            salt = random_string(length=cls.SALT_LENGTH)

        hashed = cls.hash(source, salt)

        return cls(salt, hashed)

    def validate(self, other_source: str) -> bool:
        other_hashed = self.hash(other_source, self.salt)
        return self.hashed == other_hashed
