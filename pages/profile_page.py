from pages.base_page import BasePageBurger
from locators.profile_page_locators import ProfilePageLocators


class ProfilePageBurger(BasePageBurger):
    def click_order_history(self):
        element = self.driver.find_element(*ProfilePageLocators.BUTTON_ORDER_HISTORY)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def click_exit(self, url):
        element = self.driver.find_element(*ProfilePageLocators.BUTTON_EXIT)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()
        self.wait_to_be(url)

    def find_number_order(self):
        element = self.driver.find_element(*ProfilePageLocators.NUMBER_ORDER)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element.text
