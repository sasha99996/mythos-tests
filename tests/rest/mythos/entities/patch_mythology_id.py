import allure
from clients.rest.mythos_sandbox.entities import partial_update_mythology_by_id, get_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.base_validation import check_response_code
import pytest
import allure


@pytest.mark.patch_mythology
@allure.feature("PATCH /api/mythology/id")
@allure.testcase("https://app.qase.io/case/MSA-22")
@allure.title("Частичное обновление сущности")
def test_patch_mythology_with_auth(auth_user_tuco, mythology_id_by_user_tuco):
    response = partial_update_mythology_by_id(
        auth=auth_user_tuco,
        mythology_id=mythology_id_by_user_tuco,
        name="Зевс")
    check_response_code(response, expected_code=200)
    get_response = get_mythology_by_id(mythology_id_by_user_tuco)
    check_response_code(get_response, 200)
    assert get_response.json()["name"] == "Зевс"


@allure.feature("PATCH /api/mythology")
@allure.title("Частичное обновление сущности (негативный тест)")
def test_patch_mythology_without_auth(mythology_id_by_user_tuco):
    with allure.step("Шаг: авторизация юзером tuco с помощью фикстуры и присваивание значения переменной response"):
        response = partial_update_mythology_by_id(
        auth=None,
        mythology_id=mythology_id_by_user_tuco,
        name="Зевс"
    )
    with allure.step("Шаг: проверка код ответа = 401"):
        check_response_code(response, expected_code=401)
