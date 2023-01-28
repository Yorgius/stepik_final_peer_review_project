import pytest

import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.locators import MainPageLocators

MAIN_PAGE_URL = MainPageLocators.URL

def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)

    main_page.open()
    main_page.should_be_login_link()
    main_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, MAIN_PAGE_URL)
    
    main_page.open()
    main_page.should_be_basket_link()
    main_page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.no_items_in_the_basket()
    basket_page.is_basket_empty()
