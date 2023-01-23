from .pages.product_page import ProductPage

import pytest
import time


PRODUCT_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"


@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', \
    pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_add_to_cart_product2(browser, promo_offer_code):
    url: str = PRODUCT_URL + promo_offer_code
    product_page = ProductPage(browser, url)
    
    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_product()
    
@pytest.mark.skip
@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo_offer_code):
    url: str = PRODUCT_URL + promo_offer_code
    product_page = ProductPage(browser, url)

    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.is_not_success_message_present()


@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_guest_cant_see_success_message(browser, promo_offer_code):
    url: str = PRODUCT_URL + promo_offer_code
    product_page = ProductPage(browser, url)

    product_page.open()
    product_page.is_not_success_message_present()


@pytest.mark.skip
@pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_message_disappeared_after_adding_product_to_basket(browser, promo_offer_code):
    url: str = PRODUCT_URL + promo_offer_code
    product_page = ProductPage(browser, url)

    product_page.open()
    product_page.should_be_product_page()
    product_page.add_product_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.is_not_success_message_disappeared()