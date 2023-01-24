from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGES_BLOCK = (By.ID, 'messages')
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) strong')
    SUCCESS_MESSAGE_CART_AMOUNT = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) strong')