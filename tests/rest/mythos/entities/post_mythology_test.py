from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, get_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
import pytest
import allure


@pytest.mark.post_mythology
@allure.feature("POST /api/mythology/id")
class TestMythology:
    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Создание сущности")
    def test_create_mythology(self):
        with allure.step("Шаг: авторизация"):
            auth = get_entities_auth_headers()
        with allure.step("Шаг: создание mythology и присваивание значения переменной response"):
            response = create_mythology(auth)
        with allure.step("Шаг: проверка код ответа = 201"):
            assert response.status_code == 201, "Сущность не создана"
        with allure.step("Шаг: получение ID сущности"):
            mythology_id = response.json()["id"]
        with allure.step("Шаг: удаление сущности по ID"):
            delete_mythology_by_id(auth, mythology_id)
        with allure.step("Шаг: поиск удаленной сущности"):
            response = get_mythology_by_id(mythology_id) #Добавлена проверку после удаления сущности
        with allure.step("Шаг: проверка код ответа = 404"):
            assert response.status_code == 404, "Сущность найдена"