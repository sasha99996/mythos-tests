from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, find_mythology_by_id, fully_update_mythology_by_id, find_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from storage.urls import MythosUrls


class TestMythology:
    def test_f_update_mythology_by_id(self):
        auth = get_entities_auth_headers()

        response = create_mythology(auth)
        assert response.status_code == 201, "Сущность не создана"

        data_before = response.json()
        mythology_id = data_before["id"]

        update_response = fully_update_mythology_by_id(
            auth,
            mythology_id,
            name="stone"
        )
        assert update_response.status_code == 200, "Персонаж не обновлен"

        get_response = find_mythology_by_id(auth, mythology_id)
        assert get_response.status_code == 200

        data_after = get_response.json()
        assert data_after["name"] == "stone"

        delete_response = delete_mythology_by_id(auth, mythology_id)
        assert delete_response.status_code == 204, "Персонаж не удален"