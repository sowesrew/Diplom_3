import time

from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.feed_page import FeedPageBurger
from pages.profile_page import ProfilePageBurger
from locators.feed_page_locators import FeedPageLocators
from conftest import driver
import allure
from data import DataUrl


class TestOrderFeed:

    @allure.title("Eсли кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_details_order(self, driver):
        feed = FeedPageBurger(driver)

        feed.open_page(DataUrl.FEED)
        feed.click_order()
        structure = feed.window_order()

        assert structure.is_displayed() == True

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_user_in_feed_order(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)
        profile = ProfilePageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        main.drag_and_drop_bun()
        main.click_register_order()
        main.close_window_order_succesfull()
        main.click_personal_account()
        profile.click_order_history()
        number_order_main = profile.find_number_order().text
        main.click_feed_order()
        number_order_feed = feed.find_number_order()

        assert number_order_main in number_order_feed

    @allure.title("При создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_counter_all_up(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        main.click_feed_order()
        first_count = feed.find_all_counter()
        feed.click_constructor()
        main.drag_and_drop_bun()
        main.click_register_order()
        main.close_window_order_succesfull()
        main.click_feed_order()
        last_count = feed.find_all_counter()

        assert last_count>first_count

    @allure.title("При создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_counter_all_up(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        main.click_feed_order()
        first_count = feed.find_today_counter()
        feed.click_constructor()
        main.drag_and_drop_bun()
        main.click_register_order()
        main.close_window_order_succesfull()
        main.click_feed_order()
        last_count = feed.find_today_counter()

        assert last_count>first_count

    @allure.title("После оформления заказа его номер появляется в разделе В работе.")
    def test_order_in_work(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        main.drag_and_drop_bun()
        main.click_register_order()
        number_order = main.find_number_order()
        main.close_window_order_succesfull()
        main.click_feed_order()
        feed.wait_displayed_element(FeedPageLocators.ORDER_IN_WORK)
        number_order_feed = feed.find_order_in_work()

        assert number_order == number_order_feed


