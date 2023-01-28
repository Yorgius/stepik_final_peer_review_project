from selenium.common.exceptions import NoSuchElementException

from .locators import MainPageLocators, BasePageLocators
from .base_page import BasePage


class MainPage(BasePage):
    def should_be_basket_link(self):
        assert self.is_element_present(*BasePageLocators.BASKET_LINK), 'This page does not contain basket link'

    def go_to_basket_page(self) -> None:
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def should_be_delete_user_success_message(self):
        assert self.is_element_present(*MainPageLocators.DELETE_USER_SUCCESS_MESSAGE), \
            'Success delete user message is not present'