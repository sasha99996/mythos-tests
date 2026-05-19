from clients.rest.base_http import send_request
from storage.urls import AuthUrls

def get_entities_auth_headers(username, password):
    """
    Функция возвращает авторизационный токен для entities
    """
    headers = {"Content-Type": "application/json", "accept": "application/json"}
    creds = {"username": username, "password": password}
    #token = send_request("POST", AuthUrls.LOGIN_URL, params=creds, headers=headers).json()["token"]
    token = send_request("POST", AuthUrls.LOGIN_URL, data=creds, headers=headers)
    return {"Authorization": f"Bearer {token.status_code}"}



print(get_entities_auth_headers("hercules_77", "secure_pass"))