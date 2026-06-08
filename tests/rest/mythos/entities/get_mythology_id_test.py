from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.mythos_sandbox.entities import get_mythology_by_id, create_mythology
from clients.data_generator import get_random_string
from clients.rest.base_validation import check_response_code
import pytest
import allure

@pytest.mark.get_mythology_id
@allure.feature("GET /api/mythology/id")
class TestMythology:
    @allure.title("Получение сущности по ID")
    def test_get_mythology_id(self):
        auth = get_entities_auth_headers()

        new_myth = create_mythology(auth)
        assert new_myth.status_code == 201

        mythology_id = new_myth.json()["id"]

        response = get_mythology_by_id(mythology_id)

        assert response.status_code == 200, "Сущность не найдена"


    def test_get_mythology_id_with_fixture(self, mythology_id_by_user_tuco):
        response = get_mythology_by_id(mythology_id_by_user_tuco)

        assert response.status_code == 200, "Сущность не найдена"

    @pytest.mark.skip("Припросе сущности с ID из 50 знаков возвращается код 500")
    def test_get_mythology_with_long_id(self):
        long_mythology_id = get_random_string(size=50, string_type="digits")
        response = get_mythology_by_id(long_mythology_id)
        check_response_code(response, expected_code=200)


    def test_negative_get_mythology_id(self):  #Негативный автотест при введении букв в поле для ID
        negative_mythology_id = get_random_string(size=10, string_type="letters")
        response = get_mythology_by_id(negative_mythology_id)
        check_response_code(response, expected_code=400)
