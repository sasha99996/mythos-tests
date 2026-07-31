from selenium.webdriver.common.by import By
from clients.web.base_page import BasePage

class FormFields(BasePage):
    NAME_FIELD = (
        By.CSS_SELECTOR,
        "input#name-input",
        "Поле 'Name' на веб-странице")

    PASSWORD_FIELD = (
        By.CSS_SELECTOR,
        "input[type='password'",
        "Поле 'Password' на веб-странице")

    FAVORITE_DRINK_MILK = (
        By.CSS_SELECTOR,
        "#drink2",
        "Выбрать  'Milk' в качестве любимого напитка")

    FAVORITE_COLOR_YELLOW = (
        By.CSS_SELECTOR,
        "#color3",
        "Выбрать 'Yellow' в качестве любимого цвета")

    AUTOMATION_FIELD_YES = (
        By.CSS_SELECTOR,
        "[data-testid='automation-yes']",
        "Выбрать 'Yes' в опроснике")

    EMAIL_FIELD_IVAN = (
        By.CSS_SELECTOR,
        "#email",
        "Ввести 'ivan@gmail.com' в поле email")

    MESSAGE_FIELD = (
        By.CSS_SELECTOR,
        "#message",
        "Ввести сообщение 'ыыы ааа'")

    BTN_SUBMIT = (
        By.CSS_SELECTOR,
        "#submit-btn",
        "Нажать кнопку 'Submit'")

    def fill_in_name_field(self, browser, name='Ivan'):
        """Заполняет поле 'Name' на веб-странице"""
        fill_in_name_field = self.find_element(browser, *self.NAME_FIELD, time_wait=20)
        fill_in_name_field.click()
        fill_in_name_field.send_keys(name)

    

