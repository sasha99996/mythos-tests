from clients.rest.base_http import send_request
from storage.urls import MythosUrls


def register_user(username: str, password: str):
    """Функция для регистрации пользователя"""
    body = {"username": username, "password": password}
    return send_request(method="POST", resource_url=MythosUrls.REGISTER_URL, json=body)


def create_mythology(
    auth, name="Посейдон", category="gods", desc="Бог морей", img="https://images.com/"
):
    """Функция для создания сущности"""
    body = {"name": name, "category": category, "desc": desc, "img": img}
    return send_request("POST", MythosUrls.MYTHOLOGE_URL, json=body, headers=auth)


def delete_mythology_by_id(auth, id):
    """Функция удаления сущности по ID"""
    return send_request("DELETE", f"{MythosUrls.MYTHOLOGE_URL}/{id}", headers=auth)


def get_all_mythology(params=None):
    """Функция получения списка всех сущностей"""
    return send_request(
        method="GET", resource_url=f"{MythosUrls.MYTHOLOGE_URL}", params=params
    )


def get_mythology_by_id(id):
    """Функция получения сущности по ID"""
    return send_request(method="GET", resource_url=f"{MythosUrls.MYTHOLOGE_URL}/{id}")


def fully_update_mythology_by_id(
    auth,
    mythology_id,
    name="Посейдон",
    category="gods",
    desc="Бог морей",
    img="https://images.com/",
):
    body = {"name": name, "category": category, "desc": desc, "img": img}
    """Функция полного обновления сущности по ID"""
    return send_request(
        method="PUT",
        resource_url=f"{MythosUrls.MYTHOLOGE_URL}/{mythology_id}",
        headers=auth,
        json=body,
    )


def partial_update_mythology_by_id(auth, mythology_id, **kwargs):
    """Функция частичного обновления сущности по ID"""
    return send_request(
        method="PATCH",
        resource_url=f"{MythosUrls.MYTHOLOGE_URL}/{mythology_id}",
        headers=auth,
        json=kwargs,
    )
