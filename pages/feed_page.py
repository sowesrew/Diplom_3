import allure
from pages.base_page import BasePageBurger
from locators.feed_page_locators import FeedPageLocators


class FeedPageBurger(BasePageBurger):
    def click_order(self):
        element = self.driver.find_element(*FeedPageLocators.LIST_ORDER)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def window_order(self):
        element = self.driver.find_element(*FeedPageLocators.WINDOW_ORDER)
        return element

    def find_number_order(self):
        order_list = []
        elements = self.driver.find_elements(*FeedPageLocators.LIST_ORDER)
        for i in elements:
            order_list.append(i.text)
        return order_list

    def find_all_counter(self):
        elements = self.driver.find_element(*FeedPageLocators.COUNTER_ALL_ORDERS)
        return elements.text

    def click_constructor(self):
        element = self.driver.find_element(*FeedPageLocators.P_KONSTRUCTOR)
        if self.driver.name == 'firefox':
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    def find_today_counter(self):
        elements = self.driver.find_element(*FeedPageLocators.COUNTER_TODAY_ORDERS)
        return elements.text

    def find_order_in_work(self):
        elements = self.driver.find_element(*FeedPageLocators.ORDER_IN_WORK)
        return elements.text
