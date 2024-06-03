import allure
import time
from pages.base_page import BasePageBurger
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop
from locators.reset_password_page_locators import ResetPasswordPageLocators


class MainPageBurger(BasePageBurger):
    def click_personal_account(self):
        self.driver.find_element(*MainPageLocators.BUTTON_PROFILE).click()

    def click_feed_order(self):
        self.driver.find_element(*MainPageLocators.ORDER_FFED).click()

    def click_ingredient(self):
        self.driver.find_element(*MainPageLocators.COUNTER_INGREDIENT).click()

    def open_window_ingredient(self):
        element = self.driver.find_element(*MainPageLocators.HEAD_DETAIL_ING)
        return element

    def close_window_ingredient(self):
        self.driver.find_element(*MainPageLocators.CLOSE_BUTTON).click()

    def drag_and_drop_souse(self):
        souse = self.driver.find_element(*MainPageLocators.INGREDIENT_SAUSE)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, souse, bun_cons)

    def up_counter(self):
        element = self.driver.find_element(*MainPageLocators.COUNTER_INGREDIENT)
        return element

    def click_register_order(self):
        self.driver.find_element(*MainPageLocators.BUTTON_REGISTER_ORDER).click()

    def drag_and_drop_bun(self):
        bun = self.driver.find_element(*MainPageLocators.INGREDIENT_BUN)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, bun, bun_cons)

    def order_is_made(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER_HEAD)
        return element

    def close_window_order_succesfull(self):
        self.driver.find_element(*MainPageLocators.CLOSE_BUTTON).click()

    def find_number_order(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER)
        return f'0{element.text}'
