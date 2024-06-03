import time

from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from conftest import driver
import allure
from data import DataUrl


class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        login = LoginPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.click_go_to_constructor()

        assert driver.current_url == DataUrl.CONSTRUCTOR

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_feed_order(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_feed_order()

        assert driver.current_url == DataUrl.FEED

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_open_ingredient(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_ingredient()
        window_head = main.open_window_ingredient()

        assert window_head.is_displayed() == True

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_closed_window_ingredient(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_ingredient()
        window_head = main.open_window_ingredient()
        main.close_window_ingredient()

        assert window_head.is_displayed() == False

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается")
    def test_add_ingredient_counter(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.drag_and_drop_souse()
        counter = main.up_counter()

        assert counter.text == '1'

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_user_login_register_order(self, driver):
        main = MainPageBurger(driver)
        login = LoginPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        main.drag_and_drop_bun()
        main.click_register_order()
        popup = main.order_is_made()

        assert popup.is_displayed() == True
