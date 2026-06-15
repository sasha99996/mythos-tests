from clients.rest.mythos_sandbox.entities import register_user
from clients.data_generator import get_random_string
from clients.rest.base_validation import check_response_code
import allure
import pytest

@pytest.mark.post_register
@allure.feature("POST /api/register")
class TestMythology:
    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Регистрация нового пользователя")
    def test_register_success(self):
        with allure.step("Шаг: получаем набор рандомных букв в размере 6 для логина"):
            new_user = get_random_string(size=6, string_type="letters")
        with allure.step("Шаг: получаем набор рандомных букв в размере 6 для пароля"):
            new_password = get_random_string(size=6, string_type="letters")
        with allure.step("Шаг: регистрируемся, вводя полученные данные"):
            new_us = register_user(username=new_user, password=new_password)
        with allure.step("Шаг: проверка код ответ = 201"):
            check_response_code(new_us, 201)


