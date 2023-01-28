from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage, DeleteProfilePage

from .pages.locators import ProductPageLocators, LoginPageLocators, ProfilePageLocators

import pytest
import time


PRODUCT_PAGE_URL: str = ProductPageLocators.URL
PRODUCT_PROMO_OFFER_URL: str = PRODUCT_PAGE_URL + '?promo=offer0'


# test loading the login page from the product page for an unregistered user
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser: object) -> None:
    product_page = ProductPage(browser, PRODUCT_PAGE_URL)
    product_page.open()
    product_page.should_be_product_page()
    product_page.should_be_login_link()
    product_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

# test class to add to cart from product page for non logged user
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser: object) -> None:
        url: str = PRODUCT_PROMO_OFFER_URL
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_product_added()
        
    @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser: object) -> None:
        url: str = PRODUCT_PROMO_OFFER_URL
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_not_success_message_present()


    def test_guest_cant_see_success_message(self, browser: object) -> None:
        url: str = PRODUCT_PROMO_OFFER_URL
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.is_not_success_message_present()


    @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self, browser: object) -> None:
        url: str = PRODUCT_PROMO_OFFER_URL
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_not_success_message_disappeared()


    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser: object) -> None:
        product_page = ProductPage(browser, PRODUCT_PAGE_URL)
        product_page.open()
        product_page.should_be_basket_link()
        product_page.go_to_basket()

        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_basket_page()
        basket_page.no_items_in_the_basket()
        basket_page.is_basket_empty()


# test class to add to cart from product page for logged in user
class TestUserAddToBasketFromProductPage:
    # setup fixture
    # this setup create new user for test and delete it
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser: object) -> bool:
        str_for_test_user = str(time.time())
        email = str_for_test_user + '@fakemail.com'
        psw = str_for_test_user

        # register new test user and check authorization
        login_page = LoginPage(browser, LoginPageLocators.URL)
        login_page.open()
        login_page.should_be_login_page()
        login_page.register_new_user(email, psw)
        login_page.should_be_authorized_user()
        
        yield True

        # delete test user
        profile_page = ProfilePage(browser, ProfilePageLocators.URL)
        profile_page.open()
        profile_page.should_be_profile_page()
        profile_page.start_delete_user(psw)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: object) -> None:
        product_page = ProductPage(browser, PRODUCT_PAGE_URL)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.is_product_added()

    def test_user_cant_see_success_message(self, browser: object) -> None:
        product_page = ProductPage(browser, PRODUCT_PAGE_URL)
        product_page.open()
        product_page.is_not_success_message_present()