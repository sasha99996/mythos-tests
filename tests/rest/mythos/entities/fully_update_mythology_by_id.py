from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, find_mythology_by_id, fully_update_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from storage.urls import MythosUrls


class TestMythology:
    def test_f_update_mythology_by_id(self):
        auth = get_entities_auth_headers()

        response = create_mythology(auth)
        assert response.status_code == 201, "Сущность не создана"

        mythology_id = response.json()["id"]

        update_response = fully_update_mythology_by_id(auth, mythology_id)
        assert update_response.status_code in [200, 204], "Персонаж не обновлен"

        delete_response = delete_mythology_by_id(auth, mythology_id)
        assert delete_response.status_code in [200, 204], "Персонаж не удален"