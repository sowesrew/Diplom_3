import allure
from pages.base_page import BasePageBurger
from locators.forgot_page_locators import ForgotPageLocators


class ForgotPageBurger(BasePageBurger):
    # ввод значения почты и нажатие на кнопку "Восстановить"
    def input_email(self):
        self.driver.find_element(*ForgotPageLocators.RECOVER_EMAIL_INPUT).send_keys('ulyankinasveta7_131@yandex.ru')

    def click_button_forgot(self):
        element = self.driver.find_element(*ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    # шаг восстановления пароля
    def entering_password_recovery_email(self):
        self.input_email()
        self.click_button_forgot()