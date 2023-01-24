from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, browser, url, timeout=10) -> None:
        self.browser = browser
        self.browser.implicitly_wait = timeout
        self.url = url

    def open(self) -> None:
        self.browser.get(self.url)

    def is_element_present(self, condition_search: str, selector_search: str) -> bool:
        try:
            self.browser.find_element(condition_search, selector_search)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, condition_search, selector_search, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout).\
                until(EC.presence_of_element_located((condition_search, selector_search)))
        except TimeoutException:
            return True
        return False

    def is_not_disappeared(self, condition_search, selector_search, timeout=4) -> bool:
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((condition_search, selector_search)))
        except TimeoutException:
            return False
        return True

    # def get_element(self, condition_search, selector_search):
    #     try:
    #         element = self.browser.find_element(condition_search, selector_search)
    #     except NoSuchElementException:
    #         return None
    #     return element

    def get_text(self, condition_search, selector_search) -> str:
        try:
            element = self.browser.find_element(condition_search, selector_search)
        except NoSuchElementException:
            return ''
        return element.text
