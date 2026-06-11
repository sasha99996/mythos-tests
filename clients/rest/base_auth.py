from clients.rest.base_http import send_request
from storage.urls import MythosUrls
from storage.credentials import UserTuco


def get_entities_auth_headers(creds=UserTuco.CREDS):
    """
    Функция возвращает авторизационный токен для entities
    """
    headers = {"Content-Type": "application/json"}
    token = send_request(
        "POST", MythosUrls.LOGIN_URL, data=creds, headers=headers
    ).json()["token"]
    return {"Authorization": f"Bearer {token}"}
