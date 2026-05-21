from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers

class TestMythology:
    def test_create_mythology(self):
        auth = get_entities_auth_headers()
        response = create_mythology(auth)
        assert response.status_code == 201, "Сущность не создана"
        mythology_id = response.json()["id"]
        delete_mythology_by_id(auth, mythology_id)