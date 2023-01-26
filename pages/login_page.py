from selenium.webdriver.common.by import By

from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login'), 'It is not the login url!'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), 'login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), 'register form is not present'

    # регистрация пользователя
    def register_new_user(self, email, psw):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL_INPUT)
        email_input.send_keys(email)

        psw_input_1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PSW_IMPUT_1)
        psw_input_1.send_keys(psw)

        psw_input_2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PSW_IMPUT_2)
        psw_input_2.send_keys(psw)

        registration_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        registration_submit.click()
