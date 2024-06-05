from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.login_page import LoginPageBurger
from pages.main_page import MainPageBurger
from pages.feed_page import FeedPageBurger
from pages.profile_page import ProfilePageBurger
from locators.feed_page_locators import FeedPageLocators
from conftest import driver
import allure
import pytest
from data import DataUrl


class TestOrderFeed:

    @allure.title("Eсли кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_details_order(self, driver):
        feed = FeedPageBurger(driver)

        feed.open_page_and_wait(DataUrl.FEED, FeedPageLocators.COUNTER_ALL_ORDERS)
        feed.click_order()
        feed.wait_element_and_clickable(FeedPageLocators.HEAD_STRUCTURE)
        structure = feed.window_order()

        assert structure.is_displayed() is True

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_user_in_feed_order(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)
        profile = ProfilePageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        login.wait_element_and_clickable(MainPageLocators.INGREDIENT_SAUSE)
        main.create_order()
        main.click_personal_account()
        profile.wait_to_be(DataUrl.PROFILE)
        profile.click_order_history()
        profile.wait_visibility_element(ProfilePageLocators.NUMBER_ORDER)
        number_order_main = profile.find_number_order()
        main.click_feed_order()
        profile.wait_visibility_element(FeedPageLocators.COUNTER_ALL_ORDERS)
        number_order_feed = feed.find_number_order()

        assert number_order_main in number_order_feed

    @allure.title("При создании нового заказа счётчик Выполнено за всё время/ Выполнено за сегодня увеличивается")
    @pytest.mark.parametrize(
        'locator',
        [
            FeedPageLocators.COUNTER_ALL_ORDERS,
            FeedPageLocators.COUNTER_TODAY_ORDERS
        ]
    )
    def test_counter_all_up_and_today(self, locator, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        login.wait_element_and_clickable(MainPageLocators.INGREDIENT_BUN)
        main.click_feed_order()
        feed.wait_element_and_clickable(FeedPageLocators.LIST_ORDER)
        first_count = feed.find_all_and_today_counter(locator)
        feed.click_constructor()
        main.create_order()
        main.click_feed_order()
        feed.wait_element_and_clickable(FeedPageLocators.LIST_ORDER)
        last_count = feed.find_all_and_today_counter(locator)

        assert last_count > first_count

    @allure.title("После оформления заказа его номер появляется в разделе В работе.")
    def test_order_in_work(self, driver):
        login = LoginPageBurger(driver)
        main = MainPageBurger(driver)
        feed = FeedPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.login_user()
        login.wait_element_and_clickable(MainPageLocators.INGREDIENT_BUN)
        main.drag_and_drop_bun()
        main.click_register_order()
        main.wait_visibility_element(MainPageLocators.IMG_LOADING)
        main.wait_invisibility(MainPageLocators.IMG_LOADING)
        number_order = main.find_number_order()
        main.close_window_order_succesfull()
        main.click_feed_order()
        feed.wait_displayed_element(FeedPageLocators.ORDER_IN_WORK)
        number_order_feed = feed.find_order_in_work()

        assert number_order == number_order_feed


