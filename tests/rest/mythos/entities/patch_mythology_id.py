import allure
from clients.rest.mythos_sandbox.entities import partial_update_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers
from clients.rest.base_validation import check_response_code


@allure.feature("PATCH /api/mythology")
@allure.title("Частичное обновление сущности")
def test_patch_mythology_without_auth(mythology_id_by_user_tuco):
    response = partial_update_mythology_by_id(
        auth=get_entities_auth_headers(),
        mythology_id=mythology_id_by_user_tuco,
        name="Зевс")
    check_response_code(response, expected_code=201)


@allure.feature("PATCH /api/mythology")
@allure.title("Частичное обновление сущности (негативный тест)")
def test_patch_mythology_without_auth(mythology_id_by_user_tuco):
    response = partial_update_mythology_by_id(
        auth=None,
        mythology_id=mythology_id_by_user_tuco,
        name="Зевс"
    )

    check_response_code(response, expected_code=401)