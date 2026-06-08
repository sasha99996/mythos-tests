from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, get_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.base_validation import check_response_code


class TestMythology:
    def test_delete_mythology_id(self):
        auth = get_entities_auth_headers()

        response = create_mythology(auth)
        assert response.status_code == 201, "Сущность не создана"

        mythology_id = response.json()["id"]

        delete_response = delete_mythology_by_id(auth, mythology_id)
        assert delete_response.status_code == 204, "Сущность не удалена"

        find_response = get_mythology_by_id(mythology_id)
        assert find_response.status_code == 404, "Сущность найдена"


    def test_negative_delete_mythology_by_id(self):  #Удаление сущности без авторизации (негативный тест)
        auth = get_entities_auth_headers()
        response = create_mythology(auth)
        check_response_code(response, expected_code=201)
        mythology_id = response.json()["id"]
        delete_response = delete_mythology_by_id(None, mythology_id)
        check_response_code(delete_response, expected_code=401)


