import pytest
import allure

from storage.urls import AutomateNow
from clients.web.automate_now.form_fields import FormFields


@pytest.mark.automate_now_form_fields
@allure.feature("Form_Fields")
class TestAutomateNowFormFields:
    @allure.testcase("https://app.qase.io/case/AN-12")
    @allure.title("Заполнение обязательных полей Form Fields")
    def test_fill_in_fields(self, browser):
        with allure.step("Шаг: открываем  страницу Form Fields"):
            browser.get(AutomateNow.FORM_FIELDS_URL)
        with allure.step("Шаг: Заполняем поле 'Name'"):
            FormFields().fill_in_name_field(browser)
        with allure.step("Шаг: Заполняем поле 'Password'"):
            FormFields().fill_in_password_field(browser)
        with allure.step(
            "Выбираем чек-бокс 'Milk' для поля 'What is your favorite drink?'"
        ):
            FormFields().choose_favorite_drink(browser)
        with allure.step("Шаг: Выбираем 'Yellow' в опроснике 'Favorite Color"):
            FormFields().choose_favorite_color(browser)
        with allure.step("Шаг: Выбираем 'Yes' в опроснике 'Do you like automation?'"):
            FormFields().choose_automation_answer(browser)
        with allure.step("Шаг: Вводим email 'ivan@gmail.com' в поле 'Email'"):
            FormFields().fill_in_email(browser)
        with allure.step("Шаг: Вводим сообщение 'ыыы ааа' в поле 'Message'"):
            FormFields().fill_in_message(browser)
        with allure.step("Шаг: Нажимаем кнопку 'Submit' на веб-странице"):
            FormFields().click_btn_submit(browser)
        with allure.step("Шаг: Проверяем сообщение об успешной отправке"):
            success_message = FormFields().get_success_message(browser)
            assert success_message == "Message received!"


    @pytest.mark.parametrize("answer_param", ["Yes", "No", "Undecided"])
    @allure.testcase("https://app.qase.io/case/AN-15")
    @allure.title("Автотест с параметризацией в опроснике 'Do you like automation?'")
    def test_automation_with_param (self, answer_param, browser):
        with allure.step("Шаг: открываем  страницу Form Fields"):
            browser.get(AutomateNow.FORM_FIELDS_URL)
        with allure.step("Шаг: Заполняем поле 'Name'"):
            FormFields().fill_in_name_field(browser)
        with allure.step("Шаг: Выбираем один из 3 вариантов ответа в опроснике 'Do you like automation?'"):
            FormFields().choose_automation_answer(browser, answer=answer_param)
        with allure.step("Шаг: Нажимаем кнопку 'Submit' на веб-странице"):
            FormFields().click_btn_submit(browser)
        with allure.step("Шаг: Проверяем сообщение об успешной отправке"):
            success_message = FormFields().get_success_message(browser)
            assert success_message == "Message received!"


    @pytest.mark.parametrize("answer_favorite_drink", ["Milk", "Water", "Coffee"])
    @allure.testcase("https://app.qase.io/case/AN-17")
    @allure.title("Автотест с параметризацией в чек-боксе 'What's your favorite drink?'")
    def test_favorite_drink_with_param (self, answer_favorite_drink, browser):
        with allure.step("Шаг: открываем  страницу Form Fields"):
            browser.get(AutomateNow.FORM_FIELDS_URL)
        with allure.step("Шаг: Заполняем поле 'Name'"):
            FormFields().fill_in_name_field(browser)
        with allure.step("Шаг: Выбираем один из 3 вариантов ответа в чек-боксе 'What's your favorite drink?'"):
            FormFields().choose_automation_answer(browser, answer=answer_favorite_drink)
        with allure.step("Шаг: Нажимаем кнопку 'Submit' на веб-странице"):
            FormFields().click_btn_submit(browser)
        with allure.step("Шаг: Проверяем сообщение об успешной отправке"):
            success_message = FormFields().get_success_message(browser)
            assert success_message == "Message received!"


    @pytest.mark.parametrize("answer_favorite_color", ["Red", "Blue", "Yellow", "Green", "#FFC0CB"])
    @allure.testcase("https://app.qase.io/case/AN-16")
    @allure.title("Автотест с параметризацией 'Whats your favorite color?'")
    def test_favorite_color_with_param (self, answer_favorite_color, browser):
        with allure.step("Шаг:открываем страницу Form Fields"):
            browser.get(AutomateNow.FORM_FIELDS_URL)
        with allure.step("Шаг: заполняем поле 'Name'"):
            FormFields().fill_in_name_field(browser)
        with allure.step("Шаг: Выбираем значение {answer_favorite_color} для поля 'What's your favorite color?'"):
            FormFields().choose_favorite_color(browser,answer_favorite_color)
        with allure.step("Шаг: Нажимаем кнопку 'Submit'"):
            FormFields().click_btn_submit(browser)
        with allure.step("Шаг: Проверяем сообщение об успешной проверке"):
            success_message = FormFields().get_success_message(browser)
            assert success_message == "Message received!"