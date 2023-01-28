from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.profile_page import ProfilePage, DeleteProfilePage

from .pages.locators import ProductPageLocators, LoginPageLocators, ProfilePageLocators

import pytest
import time


PRODUCT_PAGE_URL = ProductPageLocators.URL


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
@pytest.mark.in_guest
class TestGuestAddToBasketFromProductPage:
    @pytest.mark.need_review
    @pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', \
        pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
    def test_guest_can_add_product_to_basket(self, browser: object, promo_offer_code: str) -> None:
        url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_product_added()
        
    @pytest.mark.skip
    @pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser: object, promo_offer_code: str) -> None:
        url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_not_success_message_present()


    @pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    def test_guest_cant_see_success_message(self, browser: object, promo_offer_code: str) -> None:
        url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
        product_page = ProductPage(browser, url)
        product_page.open()
        product_page.is_not_success_message_present()


    @pytest.mark.skip
    @pytest.mark.parametrize('promo_offer_code', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    def test_message_disappeared_after_adding_product_to_basket(self, browser: object, promo_offer_code: str) -> None:
        url: str = PRODUCT_PAGE_URL[:-1] + promo_offer_code
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
@pytest.mark.in_user
class TestUserAddToBasketFromProductPage:
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
        print("test user created")
        
        yield True

        # delete test user
        profile_page = ProfilePage(browser, ProfilePageLocators.URL)
        profile_page.open()
        profile_page.should_be_profile_page()
        profile_page.start_delete_user()

        profile_delete_page = DeleteProfilePage(browser, browser.current_url)
        profile_delete_page.should_be_delete_profile_page()
        profile_delete_page.delete_user(psw)

        main_page = MainPage(browser, browser.current_url)
        main_page.should_be_delete_user_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser: object) -> None:
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
        product_page.open()
        product_page.should_be_product_page()
        product_page.add_product_to_basket()
        product_page.solve_quiz_and_get_code()
        product_page.is_product_added()

    def test_user_cant_see_success_message(self, browser: object) -> None:
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0")
        product_page.open()
        product_page.is_not_success_message_present()