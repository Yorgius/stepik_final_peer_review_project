from selenium.common.exceptions import NoAlertPresentException

import math

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.product_name: str = self.get_text(*ProductPageLocators.PRODUCT_NAME)
        self.product_price: str = self.get_text(*ProductPageLocators.PRODUCT_PRICE)[:4]
        self.add_to_cart_btn: bool = self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON)
        assert self.product_name and self.product_price and self.add_to_cart_btn, 'this is not product page!'

    def add_product_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()
        
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_added_product(self):
        success_priduct_name: str = self.get_text(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME)
        success_cart_price: str = self.get_text(*ProductPageLocators.SUCCESS_MESSAGE_CART_AMOUNT)[:4]
        checking: bool = self.product_name == success_priduct_name and self.product_price == success_cart_price
        assert checking, 'added the wrong product'

    def is_not_success_message_present(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_NAME) \
            and self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_CART_AMOUNT), \
            'success message is present'

    def is_not_success_message_disappeared(self):
        assert self.is_not_disappeared(*ProductPageLocators.SUCCESS_MESSAGES_BLOCK) \
            and self.is_not_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_CART_AMOUNT), \
            'is not disappeared wrong result'