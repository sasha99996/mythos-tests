from clients.web.automate_now.form_fields import FormFields
from selenium.webdriver.common.by import By
import pytest
import allure
from storage.urls import AutomateNow
from selenium import webdriver

@pytest.mark.automate_now_form_fields
@allure.feature("Form_Fields")
class TestAutomateNowFormFields:
    @allure.testcase("https://app.qase.io/case/AN-12")
    @allure.title("Заполнение обязательных полей Form Fields")
    def test_fill_in_fields(self, browser):
        with allure.step("Шаг: открываем главную страницу"):
            browser.get(AutomateNow.BASE_URL)
        with allure.step("Шаг: нажимаем кнопку  'Form Fields'"):
            browser.find_element(By.LINK_TEXT, "Form Fields").click()
        with allure.step("Шаг: Заполняем поле 'Name'"):
            FormFields().fill_in_name_field(browser)
        with allure.step("Шаг: Заполняем поле 'Password'"):
            FormFields().fill_in_password_field(browser)
        with allure.step("Шаг: Выбираем 'Milk' в опроснике 'Favorite Drink"):
            FormFields().choose_favorite_drink(browser)
        with allure.step("Шаг: Выбираем 'Yellow' в опроснике 'Favorite Color"):
            FormFields().choose_favorite_color(browser)
        with allure.step("Шаг: Выбираем 'Yes' в опроснике 'Do you like automation?'"):
            FormFields().choose_yes(browser)
        with allure.step("Шаг: Вводим email 'ivan@gmail.com' в поле 'Email'"):
            FormFields().fill_in_email(browser)
        with allure.step("Шаг: Вводим сообщение 'ыыы ааа' в поле 'Message'"):
            FormFields().fill_in_message(browser)
        with allure.step("Шаг: Нажать кнопку 'Submit' на веб-странице"):
            FormFields().click_btn_submit(browser)