from clients.web.mythos_sandbox.auth import Auth
import pytest
import allure


@pytest.mark.UI_auth
@allure.feature("Authorization")
class TestMythology:
    @allure.testcase("https://app.qase.io/case/MSA-22")
    @allure.title("Авторизация пользователя")
    def test_auth_by_user(self, browser):
        with allure.step("Шаг: Нажать на кнопку 'Войти' в шапке веб-страницы"):
            Auth().click_to_auth_widget_enter_btn(browser)
        with allure.step("Шаг: ввести данные в поля"):
            Auth().write_in_auth_widget_form_fields(browser)
        with allure.step("Шаг: Нажать на кнопку отправить данные"):
            Auth().click_to_auth_widget_submit_btn(browser)
        with allure.step("Шаг: проверить, что появилась иконка 'Выйти'"):
            Auth().check_log_out_btn_is_visible(browser)
