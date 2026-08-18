from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from clients.web.base_page import BasePage


class FormFields(BasePage):
    NAME_FIELD = (
        By.CSS_SELECTOR,
        "input#name-input",
        "Поле 'Name' на веб-странице")

    PASSWORD_FIELD = (
        By.CSS_SELECTOR,
        "input[type='password']",
        "Поле 'Password' на веб-странице")

    FAVORITE_DRINK_MILK = (
        By.CSS_SELECTOR,
        "#drink2",
        "Чек-бокс 'Milk' для поля 'What is your favorite drink?'")

    FAVORITE_DRINK_WATER = (
        By.CSS_SELECTOR,
        "#drink1",
        "Чек-бокс 'Water' для поля 'What is your favorite drink?'")

    FAVORITE_DRINK_COFFEE = (
        By.CSS_SELECTOR,
        "#drink3",
        "Чек-бокс 'Coffee' для поля 'What is your favorite drink?'")

    FAVORITE_COLOR_YELLOW = (
        By.CSS_SELECTOR,
        "#color3",
        "Чек-бокс 'Yellow' для поля 'Favorite Color'")

    FAVORITE_COLOR_RED = (
        By.CSS_SELECTOR,
        "#color1",
        "Чек-бокс 'Red' для поля 'Favorite Color'")

    FAVORITE_COLOR_BLUE = (
        By.CSS_SELECTOR,
        "#color2",
        "Чек-бокс 'Blue' для поля 'Favorite Color'")

    FAVORITE_COLOR_GREEN = (
        By.CSS_SELECTOR,
        "#color4",
        "Чек-бокс 'Green' для поля 'Favorite Color'")

    FAVORITE_COLOR_FFC0CB = (
        By.CSS_SELECTOR,
        "#color5",
        "Чек-бокс '#FFC0CB' для поля 'Favorite Color'")

    AUTOMATION_FIELD = (
        By.CSS_SELECTOR,
        "#automation",
        "Выпадающий список 'Do you like automation?'")

    AUTOMATION_FIELD_YES = (
        By.CSS_SELECTOR,
        "#automation option[data-testid='automation-yes']",
        "Option 'Yes' для поля 'Do you like automation?'")

    AUTOMATION_FIELD_NO = (
        By.CSS_SELECTOR,
        "#automation option[data-testid='automation-no']",
        "Option 'No' для поля 'Do you like automation?'")

    AUTOMATION_FIELD_UNDECIDED = (
        By.CSS_SELECTOR,
        "#automation option[data-testid='automation-undecided']",
        "Option 'Undecided' для поля 'Do you like automation?'")

    EMAIL_FIELD = (
        By.CSS_SELECTOR,
        "#email",
        "Поле 'Email' на веб-странице")

    MESSAGE_FIELD = (
        By.CSS_SELECTOR,
        "#message",
        "Поле 'Message' на веб-странице")

    BTN_SUBMIT = (
        By.CSS_SELECTOR,
        "#submit-btn",
        "Кнопка 'Submit' на веб-странице")

    def fill_in_name_field(self, browser, name="Ivan"):
        """Заполняет поле 'Name' на веб-странице."""
        name_field = self.find_element(
            browser, *self.NAME_FIELD, time_wait=20
        )
        name_field.click()
        name_field.send_keys(name)

    def fill_in_password_field(self, browser, password="test123"):
        """Заполняет поле 'Password' на веб-странице."""
        password_field = self.find_element(
            browser, *self.PASSWORD_FIELD, time_wait=20
        )
        password_field.click()
        password_field.send_keys(password)

    def choose_favorite_drink(self, browser, favorite_drink="Milk"):
        """Выбирает любимый напиток на веб-странице."""
        drinks = {
            "Milk": self.FAVORITE_DRINK_MILK,
            "Water": self.FAVORITE_DRINK_WATER,
            "Coffee": self.FAVORITE_DRINK_COFFEE,
        }
        favorite_drink_field = self.find_element(
            browser, *drinks[favorite_drink], time_wait=20
        )
        favorite_drink_field.click()

    def choose_favorite_color(self, browser, favorite_color="Yellow"):
        """Выбирает любимый цвет на веб-странице."""
        colors = {
            "Red": self.FAVORITE_COLOR_RED,
            "Blue": self.FAVORITE_COLOR_BLUE,
            "Yellow": self.FAVORITE_COLOR_YELLOW,
            "Green": self.FAVORITE_COLOR_GREEN,
            "#FFC0CB": self.FAVORITE_COLOR_FFC0CB,
        }
        favorite_color_field = self.find_element(
            browser, *colors[favorite_color], time_wait=20
        )
        self.scroll_and_click(browser, favorite_color_field)

    def choose_automation_answer(self, browser, answer="Yes"):
        """Выбирает вариант ответа для поля 'Do you like automation?'."""
        answers = {
            "Yes": self.AUTOMATION_FIELD_YES,
            "No": self.AUTOMATION_FIELD_NO,
            "Undecided": self.AUTOMATION_FIELD_UNDECIDED,
        }
        automation_answer = self.find_element(
            browser, *answers[answer], time_wait=20, check_visibility=False
        )
        automation_field = self.find_element(
            browser, *self.AUTOMATION_FIELD, time_wait=20
        )
        Select(automation_field).select_by_value(
            automation_answer.get_attribute("value")
        )

    def fill_in_email(self, browser, email="ivan@gmail.com"):
        """Заполняет поле 'Email' на веб-странице."""
        email_field = self.find_element(
            browser, *self.EMAIL_FIELD, time_wait=20
        )
        self.scroll_to_element(browser, email_field)
        email_field.send_keys(email)

    def fill_in_message(self, browser, message="ыыы ааа"):
        """Заполняет поле 'Message' на веб-странице."""
        message_field = self.find_element(
            browser, *self.MESSAGE_FIELD, time_wait=20
        )
        self.scroll_to_element(browser, message_field)
        message_field.send_keys(message)

    def click_btn_submit(self, browser):
        """Нажимает кнопку 'Submit' на веб-странице."""
        submit_button = self.find_element(
            browser, *self.BTN_SUBMIT, time_wait=20
        )
        self.scroll_and_click(browser, submit_button)

    def get_success_message(self, browser):
        """Возвращает сообщение об успешной отправке формы."""
        alert = browser.switch_to.alert
        message = alert.text
        alert.accept()
        return message
