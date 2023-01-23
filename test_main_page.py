from .pages.main_page import MainPage
from .pages.login_page import LoginPage

MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_URL)

    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
