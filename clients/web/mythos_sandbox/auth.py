from selenium.webdriver.common.by import By
from storage.credentials import UserTuco
from clients.web.base_page import BasePage


class Auth(BasePage):
    LOG_IN_BTN = (
        By.CSS_SELECTOR,
        "button[onclick*='openAuth()']",
        "Кнопка 'Войти' в шапке веб-страницы",
    )
    LOGIN_BTN = (By.CSS_SELECTOR, "#auth-user", "Поле 'Логин' на форме Авторизация")
    LOG_IN_BTN = (
        By.CSS_SELECTOR,
        "button[onclick*='openAuth()']",
        "Кнопка 'Войти' в шапке веб-страницы",
    )
    AUTH_WIDGET_LOGIN_FIELD = (
        By.CSS_SELECTOR,
        "#auth-user",
        "Поле 'Логин' на виджете авторизации",
    )
    AUTH_WIDGET_PASSWORD_FIELD = (
        By.CSS_SELECTOR,
        "#auth-pass",
        "Поле 'Пароль' на виджете авторизации",
    )
    AUTH_WIDGET_LOG_IN_BTN = (
        By.CSS_SELECTOR,
        "button[onclick*='login']",
        "Кнопка 'Войти' на виджете авторизации",
    )
    LOG_OUT_BTN = (
        By.CSS_SELECTOR,
        "button[onclick*='logout()']",
        "Кнопка 'Войти' в шапке веб-страницы",
    )

    def click_to_auth_widget_enter_btn(self, browser):
        """Нажимает на кнопку 'Войти' в шапке вэб-страницы"""
        auth_widget_enter_btn = self.find_element(
            browser, *self.LOG_IN_BTN, time_wait=20
        )
        auth_widget_enter_btn.click()

    def write_in_auth_widget_form_fields(
        self, browser, login=UserTuco.USER_NAME, password=UserTuco.PASSWORD
    ):
        """Заполняет поля 'Логин' и 'Пароль' на виджете авторизации"""
        auth_widget_login_field = self.find_element(
            browser, *self.AUTH_WIDGET_LOGIN_FIELD
        )
        auth_widget_login_field.send_keys(login)

        auth_widget_password_field = self.find_element(
            browser, *self.AUTH_WIDGET_PASSWORD_FIELD
        )
        auth_widget_password_field.send_keys(password)

    def click_to_auth_widget_submit_btn(self, browser):
        """Нажимает на кнопку 'Войти' на виджете авторизации"""
        auth_widget_submit_btn = self.find_element(
            browser, *self.AUTH_WIDGET_LOG_IN_BTN
        )
        auth_widget_submit_btn.click()

    def check_log_out_btn_is_visible(self, browser):
        """Проверяет появление иконки авторизованного пользователя"""
        return self.element_is_visible(browser, *self.LOG_OUT_BTN, displayed=True)
