import allure
from pages.base_page import BasePageBurger
from locators.login_page_locators import LoginPageLocators


class LoginPageBurger(BasePageBurger):
    # клик по ссылке "Восстановить пароль"
    def click_recover_password(self):
        self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD).click()

    def login_user(self):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys('ulyankinasveta7_131@yandex.ru')
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys('qwerty123')
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
