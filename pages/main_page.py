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

    