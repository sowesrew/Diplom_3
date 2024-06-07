from pages.base_page import BasePageBurger
from locators.forgot_page_locators import ForgotPageLocators
from data import DataAuthorization


class ForgotPageBurger(BasePageBurger):
    # ввод значения почты и нажатие на кнопку "Восстановить"
    def input_email(self):
        self.driver.find_element(*ForgotPageLocators.RECOVER_EMAIL_INPUT).send_keys(DataAuthorization.LOGIN)

    def click_button_forgot(self):
        element = self.driver.find_element(*ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        self.driver_setup(element)

    # шаг восстановления пароля
    def entering_password_recovery_email(self):
        self.input_email()
        self.click_button_forgot()
