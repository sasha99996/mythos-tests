"""
Файл с константами логинов, паролей. Данные тестовых учетных записей хранятся в переменных ci-сборки
или локальном evn-файле
"""


class UserTest12345:
    USERNAME = "test12345"
    PASS = "test12345"
    CREDS = f"""
        {{
            "username": "{USERNAME}",
            "password": "{PASS}"
        }}
        """
