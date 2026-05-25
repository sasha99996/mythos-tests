from clients.rest.base_http import send_request
from storage.urls import MythosUrls


def create_mythology(auth, name="Посейдон", category="gods", desc="Бог морей", img="https://images.com/"):
    body = {"name": name, "category": category, "desc": desc, "img": img}
    return send_request("POST",MythosUrls.MYTHOLOGE_URL, json=body, headers=auth)


def delete_mythology_by_id(auth, id):
    return send_request(
        "DELETE", f"{MythosUrls.MYTHOLOGE_URL}/{id}", headers=auth)


def find_mythology_by_id(auth, id):
    return send_request(
        method="GET", resource_url=f"{MythosUrls.MYTHOLOGE_URL}/{id}", headers=auth)


def fully_update_mythology_by_id(auth, mythology_id, name="Посейдон", category="gods", desc="Бог морей", img="https://images.com/"):
    body = {"name": name, "category": category, "desc": desc, "img": img}
    return send_request(
        method="PUT",resource_url=f"{MythosUrls.MYTHOLOGE_URL}/{mythology_id}",
        headers=auth,
        json=body
    )


