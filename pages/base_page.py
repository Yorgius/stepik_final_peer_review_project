from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .locators import BasePageLocators

class BasePage:
    def __init__(self, browser, url, timeout=15) -> None:
        self.browser = browser
        self.browser.implicitly_wait = timeout
        self.url = url

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, condition_search: str, selector_search: str, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((condition_search, selector_search)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, condition_search: str, selector_search: str, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((condition_search, selector_search)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, condition_search: str, selector_search: str, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((condition_search, selector_search)))
        except TimeoutException:
            return False
        return True

    def get_text(self, condition_search: str, selector_search: str) -> str:
        try:
            element = self.browser.find_element(condition_search, selector_search)
        except NoSuchElementException:
            return ''
        return element.text

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"