import hashlib
import string
from random import choice


def random_string(length: int=8) -> str:
    options = string.ascii_letters + string.digits

    return ''.join(choice(options) for _ in range(length))


def sha1(content: str, encoding: str='utf-8') -> str:
    return hashlib.sha1(
        content.encode(encoding)
    ).hexdigest()
