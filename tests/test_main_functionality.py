from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from conftest import driver
import allure
from data import DataUrl


class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_go_to_constructor(self, driver):
        login = LoginPageBurger(driver)

        login.open_page_and_wait(DataUrl.LOGIN_URL, LoginPageLocators.LOGIN_BUTTON)
        login.click_go_to_constructor()

        assert driver.current_url == DataUrl.CONSTRUCTOR

    @allure.title("Переход по клику на «Лента заказов»")
    def test_go_to_feed_order(self, driver):
        main = MainPageBurger(driver)

        main.open_page_and_wait(DataUrl.BASE_URL, MainPageLocators.INGREDIENT_BUN)
        main.click_feed_order()

        assert driver.current_url == DataUrl.FEED

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_open_ingredient(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.wait_element_and_clickable(MainPageLocators.INGREDIENT_SAUSE)
        main.click_ingredient()
        window_head = main.open_window_ingredient()

        assert window_head.is_displayed() is True

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_closed_window_ingredient(self, driver):
        main = MainPageBurger(driver)

        main.open_page(DataUrl.BASE_URL)
        main.click_ingredient()
        price = main.visible_price()
        main.wait_visibility_element(MainPageLocators.IMG_INGREDIENT)
        main.close_window_ingredient()
        main.wait_visibility_element(MainPageLocators.PRICE_INGREDIENT)

        assert price.is_displayed() is True

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

        login.open_page_and_wait(DataUrl.LOGIN_URL, LoginPageLocators.LOGIN_BUTTON)
        login.login_user()
        login.wait_element_and_clickable(MainPageLocators.INGREDIENT_BUN)
        main.drag_and_drop_bun()
        main.wait_text(MainPageLocators.PRICE_INGREDIENT_2)
        main.click_register_order()
        main.wait_visibility_element(MainPageLocators.NUMBER_ORDER_HEAD)
        popup = main.order_is_made()

        assert popup.is_displayed() is True
