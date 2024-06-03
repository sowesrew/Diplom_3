import allure
from pages.base_page import BasePageBurger
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators


class ProfilePageBurger(BasePageBurger):
    def click_order_history(self):
        self.driver.find_element(*ProfilePageLocators.BUTTON_ORDER_HISTORY).click()

    def click_exit(self):
        self.driver.find_element(*ProfilePageLocators.BUTTON_EXIT).click()