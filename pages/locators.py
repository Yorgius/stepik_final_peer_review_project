from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_LINK = (By.XPATH, "//a[text()='Посмотреть корзину']")
    DELETE_USER_SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")


class LoginPageLocators:
    URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')

    REGISTER_FORM_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_FORM_PSW_IMPUT_1 = (By.ID, "id_registration-password1")
    REGISTER_FORM_PSW_IMPUT_2 = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "#register_form .btn-primary")


class ProfilePageLocators:
    URL = "http://selenium1py.pythonanywhere.com/ru/accounts/profile/"
    PAGE_HEADER = (By.CLASS_NAME, "page-header")
    START_DELETE_PROFILE_SUBMIT = (By.ID, "delete_profile")
    DELETE_PROFILE_PASSWORD_INPUT = (By.ID, "id_password")
    DELETE_PROFILE_SUBMIT = (By.CLASS_NAME, "btn-danger")


class ProductPageLocators:
    URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main > p.price_color')
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'btn-add-to-basket')
    SUCCESS_MESSAGES_BLOCK = (By.ID, 'messages')
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, '#messages > .alert:nth-child(1) strong')
    SUCCESS_MESSAGE_CART_AMOUNT = (By.CSS_SELECTOR, '#messages > .alert:nth-child(3) strong')
    BASKET_LINK = (By.XPATH, "//a[text()='Посмотреть корзину']")

class BasketPageLocators:
    BASKET_ITEMS = (By.CLASS_NAME, 'basket-items')
    EMPTY_BASKET_LABEL = (By.CSS_SELECTOR, '#content_inner>p')