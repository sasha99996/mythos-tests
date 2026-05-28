import pytest
from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id


@pytest.fixture(scope="function")
def auth_user_tuco():
    """Возвращает авторизационный токен для пользователя Tuco"""
    return get_entities_auth_headers()


@pytest.fixture(scope="function")
def mythology_id_by_user_tuco(auth_user_tuco):
    """Возвращает ID персонажа, созданного пользователем Tuco"""
    mythology_id = create_mythology(auth_user_tuco).json()["id"]
    yield mythology_id
    delete_mythology_by_id(auth_user_tuco, mythology_id)
