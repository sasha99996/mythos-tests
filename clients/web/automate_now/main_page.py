from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from clients.web.base_page import BasePage


class MainPage(BasePage):
    BLOG_BTN = (
        By.CSS_SELECTOR,
        "button#nav_toggle.nav-btn",
        "Кнопка 'Blog' на главной странице",
    )

    SOFT_AUT_BTN = (
        By.XPATH,
        "//a[normalize-space()='software automated testing']",
        "Кнопка 'Software Automated Testing' на главной странице",
    )


    def click_btn_blog(self, browser):
        """Нажимает кнопку 'Blog' на веб-странице."""
        blog_button = self.find_element(browser, *self.BLOG_BTN, time_wait=20)


    def click_btn_soft_aut(self, browser):
        """Нажимает кнопку 'Software Automated Testing' на веб-странице."""
        soft_aut_button = self.find_element(browser, *self.SOFT_AUT_BTN, time_wait=20)
