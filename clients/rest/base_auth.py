from clients.rest.base_http import send_request
from storage.urls import AuthUrls
from storage.credentials import UserTest12345


def get_entities_auth_headers(creds=UserTest12345.CREDS):
    """
    Функция возвращает авторизационный токен для entities
    """
    headers = {"Content-Type": "application/json"}
    token = send_request(
        "POST", AuthUrls.LOGIN_URL, data=creds, headers=headers
    ).json()["token"]
    return {"Authorization": f"Bearer {token}"}
