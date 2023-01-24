from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

import pytest
import time


PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"


@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', \
    pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_add_to_cart_product2(browser, promo_offer_code):
    url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
    product_page = ProductPage(browser, url)
    
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_product()
    
@pytest.mark.skip
@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo_offer_code):
    url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
    product_page = ProductPage(browser, url)

    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.is_not_success_message_present()


@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_guest_cant_see_success_message(browser, promo_offer_code):
    url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
    product_page = ProductPage(browser, url)

    product_page.open()
    product_page.is_not_success_message_present()


@pytest.mark.skip
@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_message_disappeared_after_adding_product_to_basket(browser, promo_offer_code):
    url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
    product_page = ProductPage(browser, url)

    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.is_not_success_message_disappeared()


@pytest.mark.from_product_to_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, PRODUCT_PAGE_URL)
    product_page.open()
    product_page.should_be_basket_link()
    product_page.go_to_basket()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.no_items_in_the_basket()
    basket_page.should_be_empty_basket_label()
    basket_page.empty_basket_label_is_not_disappeared()

