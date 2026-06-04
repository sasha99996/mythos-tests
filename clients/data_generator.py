"""
Файл содержит функции-помощники для генерации тестовых данных
"""

import random
import string


def get_random_string(size=6, string_type="letters"):
    """Возвращает рандомную строку"""
    charsets = {"letters": string.ascii_letters, "digits": string.digits, "lowercase": string.ascii_lowercase}
    return "".join(random.choice(charsets[string_type]) for _ in range(size))
