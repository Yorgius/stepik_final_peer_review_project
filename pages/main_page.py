from selenium.common.exceptions import NoSuchElementException

from .locators import MainPageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_login_page(self) -> None:
        login_link =  self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_basket_link(self):
        assert self.is_element_present(*MainPageLocators.BASKET_LINK), 'This page does not contain basket link'

    def go_to_basket_page(self) -> None:
        basket_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_delete_user_success_message(self):
        assert self.is_element_present(*MainPageLocators.DELETE_USER_SUCCESS_MESSAGE), \
            'Success delete user message is not present'

    def is_delete_success(self):
        self.should_be_delete_user_success_message()
        message_string = "Ваш профиль удален"
        assert self.browser.find_element(*MainPageLocators.DELETE_USER_SUCCESS_MESSAGE).text.__contains__(message_string), \
            f"success delete message is not contains <{message_string}>"

    