import time

from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.profile_page import ProfilePageBurger
from conftest import driver
import allure
from data import DataUrl
from locators.main_page_locators import MainPageLocators


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_personal_account(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_personal_account()

        assert driver.current_url == DataUrl.LOGIN_URL

    @allure.title("Переход в раздел «История заказов»")
    def test_go_to_order_history(self, driver):
        main = MainPageBurger(driver)
        login = LoginPageBurger(driver)
        profile = ProfilePageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_personal_account()
        login.login_user()
        login.wait_element(MainPageLocators.ELEMENT_BUN)
        main.click_personal_account()
        profile.click_order_history()

        assert driver.current_url == DataUrl.ORDER_HISTORY

    @allure.title("Выход из аккаунта")
    def test_go_to_exit(self, driver):
        main = MainPageBurger(driver)
        login = LoginPageBurger(driver)
        profile = ProfilePageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_personal_account()
        login.login_user()
        login.wait_element(MainPageLocators.ELEMENT_BUN)
        main.click_personal_account()
        profile.click_exit()

        assert driver.current_url == DataUrl.LOGIN_URL
