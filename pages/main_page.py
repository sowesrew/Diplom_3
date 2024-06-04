from pages.base_page import BasePageBurger
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop


class MainPageBurger(BasePageBurger):
    def click_personal_account(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_PROFILE)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def click_feed_order(self):
        element = self.driver.find_element(*MainPageLocators.ORDER_FEED)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def click_ingredient(self):
        element = self.driver.find_element(*MainPageLocators.COUNTER_INGREDIENT_NULL)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def open_window_ingredient(self):
        element = self.driver.find_element(*MainPageLocators.IMG_INGREDIENT)
        return element

    def visible_price(self):
        element = self.driver.find_element(*MainPageLocators.PRICE_INGREDIENT)
        return element

    def close_window_ingredient(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_BUTTON)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def drag_and_drop_souse(self):
        souse = self.driver.find_element(*MainPageLocators.INGREDIENT_SAUSE)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, souse, bun_cons)

    def up_counter(self):
        element = self.driver.find_element(*MainPageLocators.COUNTER_INGREDIENT)
        return element

    def click_register_order(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_REGISTER_ORDER)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def drag_and_drop_bun(self):
        bun = self.driver.find_element(*MainPageLocators.INGREDIENT_BUN)
        bun_cons = self.driver.find_element(*MainPageLocators.BUN_CONSTRUCTOR)
        drag_and_drop(self.driver, bun, bun_cons)

    def order_is_made(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER_WINDOW)
        return element

    def close_window_order_succesfull(self):
        element = self.driver.find_element(*MainPageLocators.CLOSE_BUTTON_ORDER)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def find_number_order(self):
        element = self.driver.find_element(*MainPageLocators.NUMBER_ORDER)
        return f'0{element.text}'

    # шаг заказ
    def create_order(self):
        self.drag_and_drop_bun()
        self.click_register_order()
        self.wait_visibility_element(MainPageLocators.CLOSE_BUTTON_ORDER)
        self.close_window_order_succesfull()
