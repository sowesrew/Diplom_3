import allure
from pages.base_page import BasePageBurger
from locators.main_page_locators import MainPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators


class MainPageBurger(BasePageBurger):
    def click_personal_account(self):
        self.driver.find_element(*MainPageLocators.BUTTON_PROFILE).click()
