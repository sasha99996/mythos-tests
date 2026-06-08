import allure
import pytest

from clients.rest.mythos_sandbox.entities import create_mythology, delete_mythology_by_id, fully_update_mythology_by_id, get_mythology_by_id
from clients.rest.base_auth import get_entities_auth_headers


@pytest.mark.put_mythology
@allure.feature("PUT /api/mythology/id")
class TestMythology:
    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Полное обновление сущности")
    def test_f_update_mythology_by_id(self):
        auth = get_entities_auth_headers()

        response = create_mythology(auth, name="Посейдон")
        assert response.status_code == 201, "Сущность не создана"

        mythology_id = response.json()["id"]

        update_response = fully_update_mythology_by_id(
            auth,
            mythology_id,
            name="stone"
        )
        assert update_response.status_code == 200, "Персонаж не обновлен"

        new_name = get_mythology_by_id(mythology_id).json()["name"]
        assert new_name == "stone", "Имя не изменено"

        delete_response = delete_mythology_by_id(auth, mythology_id)
        assert delete_response.status_code == 204, "Персонаж не удален"

    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Полное обновление сущности через фикстуру")
    def test_f_update_mythology_by_id_with_fixtures(self, auth_user_tuco, mythology_id_by_user_tuco):
        with allure.step("Шаг: Обновить сущность"):
            update_response = fully_update_mythology_by_id(
                auth_user_tuco,
                mythology_id_by_user_tuco,
                name="stone"
            )
        with allure.step("Проверка: Код ответа равен 200"):
            assert update_response.status_code == 200, "Персонаж не обновлен"
        with allure.step("Проверка: Имя обновлено"):
            new_name = get_mythology_by_id(mythology_id_by_user_tuco).json()["name"]
            assert new_name == "stone", "Имя не изменено"
