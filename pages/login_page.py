from pages.base_page import BasePageBurger
from locators.login_page_locators import LoginPageLocators
from data import DataAuthorization


class LoginPageBurger(BasePageBurger):
    # клик по ссылке "Восстановить пароль"
    def click_recover_password(self):
        element = self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD)
        self.driver_setup(element)

    def login_user(self):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys(DataAuthorization.LOGIN)
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys(DataAuthorization.PASS)
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        self.driver_setup(element)

    def click_go_to_constructor(self):
        element = self.driver.find_element(*LoginPageLocators.P_KONSTRUCTOR)
        self.driver_setup(element)
