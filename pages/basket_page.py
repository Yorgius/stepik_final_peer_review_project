from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_page(self):
        basket_url = self.browser.current_url.strip('/').split('/')[-1]
        assert basket_url == 'basket', 'this page is not a basket page!'

    def no_items_in_the_basket(self):
        ...

    def is_basket_empty(self):
        ...