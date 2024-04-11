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

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_field.send_keys(email)
        password1_field = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        password1_field.send_keys(password)
        password2_field = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        password2_field.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        registration_button.click()