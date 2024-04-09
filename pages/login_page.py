from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in login_url, "Нет личного кабинета"

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.SIGN_IN_FORM), "Форма 'Войти' отсутствует"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REG_FORM), "Форма 'Зарегистрироваться' отсутствует"