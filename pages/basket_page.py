from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        basket_url = self.browser.current_url.strip('/').split('/')[-1]
        assert basket_url == 'basket', 'this page is not a basket page!'

    def no_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'Items are present in basket!'

    def is_basket_empty(self):
        empty_basket_label = self.get_text(*BasketPageLocators.EMPTY_BASKET_LABEL)
        assert 'ваша корзина пуста' in empty_basket_label.lower(), 'Basket is not empty!'