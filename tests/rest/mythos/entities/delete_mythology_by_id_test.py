from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, get_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.base_validation import check_response_code
import pytest
import allure


@pytest.mark.delete_mythology_id
@allure.feature("DELETE /api/mythology/id")
class TestMythology:
    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Удаление сущности по ID")
    def test_delete_mythology_id(self, auth_user_tuco):
        with allure.step("Шаг: создать сущность"):
            response = create_mythology(auth_user_tuco)
        with allure.step("Проверка: код ответа = 201"):
            assert response.status_code == 201, "Сущность не создана"

            mythology_id = response.json()["id"]
        with allure.step("Шаг: удалить сущность"):
            delete_response = delete_mythology_by_id(auth_user_tuco, mythology_id)
        with allure.step("Проверка: код ответа = 204"):
            assert delete_response.status_code == 204, "Сущность не удалена"
        with allure.step("Шаг: найти сущность"):
            find_response = get_mythology_by_id(mythology_id)
        with allure.step("Проверка: код ответа = 404"):
            assert find_response.status_code == 404, "Сущность найдена"


    def test_negative_delete_mythology_by_id(self, auth_user_tuco):  #Удаление сущности без авторизации (негативный тест)
        with allure.step("Шаг: создать сущность"):
            response = create_mythology(auth_user_tuco)
        with allure.step("Проверка: код ответа = 201"):
            check_response_code(response, expected_code=201)
        with allure.step("Шаг: получаем ID сущности"):
            mythology_id = response.json()["id"]
        with allure.step("Шаг: удалить сущность"):
            delete_response = delete_mythology_by_id(None, mythology_id)
        with allure.step("Проверка: код ответа = 401"):
            check_response_code(delete_response, expected_code=401)


