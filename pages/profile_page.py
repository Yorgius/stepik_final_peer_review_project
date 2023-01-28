from .base_page import BasePage
from .locators import ProfilePageLocators

class ProfilePage(BasePage):
    def should_be_profile_page(self):
        self.should_be_profile_url()
        self.should_be_profile_page_header()

    def should_be_profile_url(self):
        assert self.browser.current_url == ProfilePageLocators.URL

    def should_be_profile_page_header(self):
        assert self.is_element_present(*ProfilePageLocators.PAGE_HEADER)

    def start_delete_user(self, psw):
        delete_profile_submit = self.browser.find_element(*ProfilePageLocators.START_DELETE_PROFILE_SUBMIT)
        delete_profile_submit.click()

        profile_delete_page = DeleteProfilePage(self.browser, self.browser.current_url)
        profile_delete_page.should_be_delete_profile_page()
        profile_delete_page.delete_user(psw)


class DeleteProfilePage(BasePage):
    def should_be_delete_profile_page(self):
        self.should_be_delete_password_input()
        self.should_be_delete_profile_submit()
    
    def should_be_delete_password_input(self):
        assert self.is_element_present(*ProfilePageLocators.DELETE_PROFILE_PASSWORD_INPUT)

    def should_be_delete_profile_submit(self):
        assert self.is_element_present(*ProfilePageLocators.DELETE_PROFILE_SUBMIT)

    def delete_user(self, password):
        password_input = self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_PASSWORD_INPUT)
        password_input.send_keys(password)
        
        delete_submit = self.browser.find_element(*ProfilePageLocators.DELETE_PROFILE_SUBMIT)
        delete_submit.click()