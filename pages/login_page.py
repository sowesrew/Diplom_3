import allure
from pages.base_page import BasePageBurger
from locators.login_page_locators import LoginPageLocators


class LoginPageBurger(BasePageBurger):
    # клик по ссылке "Восстановить пароль"
    def click_recover_password(self):
        self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD).click()
