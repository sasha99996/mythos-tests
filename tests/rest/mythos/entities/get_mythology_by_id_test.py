from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.mythos_sandbox.entities import get_mythology_by_id, create_mythology


class TestMythology:
    def test_get_mythology_id(self):
        auth = get_entities_auth_headers()

        new_myth = create_mythology(auth)
        assert new_myth.status_code == 201

        mythology_id = new_myth.json()["id"]

        response = get_mythology_by_id(mythology_id)

        assert response.status_code == 200, "Сущность не найдена"
