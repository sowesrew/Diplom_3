from pages.base_page import BasePageBurger
from locators.profile_page_locators import ProfilePageLocators


class ProfilePageBurger(BasePageBurger):
    def click_order_history(self):
        element = self.driver.find_element(*ProfilePageLocators.BUTTON_ORDER_HISTORY)
        self.driver_setup(element)

    def click_exit(self, url):
        element = self.driver.find_element(*ProfilePageLocators.BUTTON_EXIT)
        self.driver_setup(element)
        self.wait_to_be(url)

    def find_number_order(self):
        element = self.driver.find_element(*ProfilePageLocators.NUMBER_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element.text
