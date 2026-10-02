import pytest
import allure

from storage.urls import AutomateNow
from clients.web.automate_now.main_page import MainPage



@pytest.mark.automate_now_main_page
@allure.feature("Blog_Test")
class TestAutomateNowFormFields:
    @allure.testcase("https://app.qase.io/case/AN-13")
    @allure.title("Открытие страницы Blog")
    def test_fill_in_fields(self, browser):
        with allure.step("Шаг: открываем  страницу 'Practice Automation'"):
            browser.get(AutomateNow.BASE_URL)
        with allure.step("Шаг: нажимаем на кнопку 'Blog'"):
            MainPage().click_btn_blog(browser)
        with allure.step("Шаг: проверить что прошел редирект по url 'https://automatenow.io/'"):
            MainPage().check_url_changes(browser, AutomateNow.BLOG_URL)