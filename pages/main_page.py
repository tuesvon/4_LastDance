from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.REG_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(*MainPageLocators.REG_LINK), "login link is not presented"

