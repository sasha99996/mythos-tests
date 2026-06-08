import pytest
import allure
from clients.rest.base_http import send_request
from storage.urls import MythosUrls
from clients.rest.mythos_sandbox.entities import get_all_mythology, get_mythology_by_id
from clients.rest.base_validation import check_response_code, check_value_in_dicts, check_dicts_are_sorted_by_key


@pytest.mark.get_all_mythology
@allure.feature("GET /api/mythology")
class TestMythology:
    @allure.title("Получение списка всех сущностей")
    def test_get_mythology_list(self):
        response = send_request("GET", MythosUrls.MYTHOLOGE_URL)
        assert response.status_code == 200


    @pytest.mark.parametrize("category", ["gods", "heroes", "creatures"])
    @allure.title("Получение списка всех сущностей с параметризацией категории")
    def test_get_mythology_list_with_category_filter(self, category):
        with allure.step("Шаг: получаем список героев и присваиваем значение переменной response"):
            response = get_all_mythology(params={"category": category})
        with allure.step("Шаг: проверка код ответа = 200"):
            check_response_code(response, expected_code=200)
        with allure.step("Шаг: проверка что значение по ключу в каждом словаре совпадает с выбранным условием"):
            check_value_in_dicts(response.json(), key="category", value=category)


    @pytest.mark.parametrize("sort, reverse", [("asc", False), ("desc", True)])
    @allure.title("Получение списка всех сущностей с параметризацией сортировки")
    def test_get_mythology_list_with_category_filter_1(self, sort, reverse):
        with allure.step("Шаг: получаем список героев и присваиваем значение переменной response"):
            response = get_all_mythology(params={"category": "creatures", "sort": sort})
        with allure.step("Шаг: проверка код ответа = 200"):
            check_response_code(response, 200)
        with allure.step("Шаг: проверка что список словарей items отсортирован по указанному ключу key"):
            check_dicts_are_sorted_by_key(response.json(), key="name", reverse=reverse)
