"""
Файл с константами логинов, паролей. Данные тестовых учетных записей хранятся в переменных ci-сборки
или локальном evn-файле
"""

import os
from dotenv import load_dotenv

load_dotenv()


class UserTuco:
    USER_NAME = f"{os.getenv('TUCO_USER_NAME')}"
    PASSWORD = f"{os.getenv('TUCO_PASSWORD')}"
    CREDS = f"""
        {{
            "username": "{USER_NAME}",
            "password": "{PASSWORD}"
        }}
        """
