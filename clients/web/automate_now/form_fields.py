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

    def fill_in_password_field(self, browser, name='test123'):
        """Заполняет поле 'Name' на веб-странице"""
        fill_in_password_field = self.find_element(browser, *self.PASSWORD_FIELD, time_wait=20)
        fill_in_password_field.click()
        fill_in_password_field.send_keys(name)

    def choose_favorite_drink(self, browser, name='Milk'):
        """Выбирает поле 'Favorite Drink' на веб-странице"""
        choose_favorite_drink = self.find_element(browser, *self.FAVORITE_DRINK_MILK, time_wait=20)
        choose_favorite_drink.click()
        choose_favorite_drink.send_keys(name)

    def choose_favorite_color(self, browser, name='Yellow'):
        """Выбирает поле 'Favorite Color' на веб-странице"""
        choose_favorite_color = self.find_element(browser, *self.FAVORITE_COLOR_YELLOW, time_wait=20)
        choose_favorite_color.click()
        choose_favorite_color.send_keys(name)

    def choose_yes(self, browser, name='Yes'):
        """Выбирает опцию 'Yes' на веб странице в опросе 'Do you like automation?'"""
        choose_yes = self.find_element(browser, *self.AUTOMATION_FIELD_YES, time_wait=20)
        choose_yes.click()
        choose_yes.send_keys(name)

    def fill_in_email(self, browser, name='ivan@gmail.com'):
        """Заполняет поле 'Email' на веб-странице"""
        fill_in_email = self.find_element(browser, *self.EMAIL_FIELD_IVAN, time_wait=20)
        fill_in_email.click()
        fill_in_email.send_keys(name)

    def fill_in_message(self, browser, name='ыыы ааа'):
        """Заполняет поле 'Message' на веб-странице"""
        fill_in_message = self.find_element(browser, *self.MESSAGE_FIELD, time_wait=20)
        fill_in_message.click()
        fill_in_message.send_keys(name)

    def click_btn_submit(self, browser, name='submit'):
        """Нажимает кнопку 'Submit' на веб-странице"""
        click_btn_submit = self.find_element(browser, *self.BTN_SUBMIT, time_wait=20)
        click_btn_submit.click()
        click_btn_submit.send_keys(name)

