from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.mythos_sandbox.entities import get_mythology_by_id, create_mythology
from clients.data_generator import get_random_string
from clients.rest.base_validation import check_response_code
import pytest
import allure

@pytest.mark.get_mythology_id
@allure.feature("GET /api/mythology/id")
class TestMythology:
    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Получение сущности по ID")
    def test_get_mythology_id(self):
        with allure.step("Шаг: авторизация"):
            auth = get_entities_auth_headers()
        with allure.step("Шаг: создать сущность"):
            new_myth = create_mythology(auth)
        with allure.step("Проверка: код ответа = 201"):
            assert new_myth.status_code == 201
        with allure.step("Шаг: получаем ID сущности"):
            mythology_id = new_myth.json()["id"]
        with allure.step("Шаг: присваиваем значение переменной response"):
            response = get_mythology_by_id(mythology_id)
        with allure.step("Проверка: код ответа = 200"):
            assert response.status_code == 200, "Сущность не найдена"


    def test_get_mythology_id_with_fixture(self, mythology_id_by_user_tuco):
        with allure.step("Шаг: авторизация пользователем tuco с фикстурой"):
            response = get_mythology_by_id(mythology_id_by_user_tuco)
        with allure.step("Проверка: код ответа = 200"):
            assert response.status_code == 200, "Сущность не найдена"

    @pytest.mark.skip("Припросе сущности с ID из 50 знаков возвращается код 500")
    def test_get_mythology_with_long_id(self):
        with allure.step("Шаг: вызываем команду получения рандоного числа размером 50"):
            long_mythology_id = get_random_string(size=50, string_type="digits")
        with allure.step("Шаг: присваиваем значение переменной response"):
            response = get_mythology_by_id(long_mythology_id)
        with allure.step("Проверка: код ответа = 200"):
            check_response_code(response, expected_code=200)


    def test_negative_get_mythology_id(self):  #Негативный автотест при введении букв в поле для ID
        with allure.step("Шаг: вызываем команду получения рандоных букв размером 10"):
            negative_mythology_id = get_random_string(size=10, string_type="letters")
        with allure.step("Шаг: присваиваем значение переменной response"):
            response = get_mythology_by_id(negative_mythology_id)
        with allure.step("Проверка: код ответа = 200"):
            check_response_code(response, expected_code=400)
