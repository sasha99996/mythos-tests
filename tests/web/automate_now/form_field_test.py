from clients.web.automate_now.form_fields import FormFields
import pytest
import allure

@pytest.mark.automate_now_form_fields
@allure.feature("Form_Fields")
class TestAutomateNowFormFields:
    @allure.testcase("https://app.qase.io/case/AN-12")
    @allure.title("Заполнение обязательных полей Form Fields")
    def test_fill_in_fields(self, browser):
        with allure.step("Шаг: Заполняем поле 'Name'"):
            FormFields().fill_in_name_field(browser)
