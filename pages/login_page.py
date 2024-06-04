from pages.base_page import BasePageBurger
from locators.login_page_locators import LoginPageLocators


class LoginPageBurger(BasePageBurger):
    # клик по ссылке "Восстановить пароль"
    def click_recover_password(self):
        element = self.driver.find_element(*LoginPageLocators.RECOVER_PASSWORD)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def login_user(self):
        self.driver.find_element(*LoginPageLocators.INPUT_EMAIL).send_keys('ulyankinasveta7_131@yandex.ru')
        self.driver.find_element(*LoginPageLocators.INPUT_PASSWORD).send_keys('qwerty123')
        element = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def click_go_to_constructor(self):
        element = self.driver.find_element(*LoginPageLocators.P_KONSTRUCTOR)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()
