from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, find_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from storage.urls import MythosUrls

class TestMythology:
    def test_delete_mythology_id(self):
        auth = get_entities_auth_headers()

        response = create_mythology(auth)
        assert response.status_code == 201, "Сущность не создана"

        mythology_id = response.json()["id"]

        delete_response = delete_mythology_by_id(auth, mythology_id)
        assert delete_response.status_code in [200, 204], "Персонаж не удален"

        find_response = find_mythology_by_id(auth, mythology_id)
        assert find_response.status_code == 404

