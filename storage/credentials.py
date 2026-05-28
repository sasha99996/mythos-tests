"""
Файл с константами логинов, паролей. Данные тестовых учетных записей хранятся в переменных ci-сборки
или локальном evn-файле
"""


class UserTuco:
    USERNAME = "Tuco"
    PASS = "JtRk_nw7{Wm"
    CREDS = f"""
        {{
            "username": "{USERNAME}",
            "password": "{PASS}"
        }}
        """
