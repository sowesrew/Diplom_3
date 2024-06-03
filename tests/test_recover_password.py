from pages.base_page import BasePageBurger
from pages.login_page import LoginPageBurger
from pages.forgot_page import ForgotPageBurger
from pages.reset_password_page import ResetPasswordPageBurger
from pages.base_page import BasePageBurger
from conftest import driver
import allure
from data import DataUrl
from locators.reset_password_page_locators import ResetPasswordPageLocators
from locators.forgot_page_locators import ForgotPageLocators
from selenium.webdriver.support import expected_conditions
import time


class TestRecoverPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password(self, driver):
        seach_button_login = LoginPageBurger(driver)

        seach_button_login.open_page(DataUrl.LOGIN_URL)
        seach_button_login.click_recover_password()

        assert driver.current_url == DataUrl.FORGOT_PASS

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_go_to_reset_password(self, driver):
        seach_button_login = LoginPageBurger(driver)
        seach_button_forgot = ForgotPageBurger(driver)
        seach_button_reset = ResetPasswordPageBurger(driver)

        seach_button_login.open_page(DataUrl.LOGIN_URL)
        seach_button_login.click_recover_password()
        seach_button_forgot.entering_password_recovery_email()
        seach_button_reset.wait_element(ResetPasswordPageLocators.EYE_BUTTON)

        assert driver.current_url == DataUrl.RESET_PASS

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_click_eye_button(self, driver):
        seach_button_login = LoginPageBurger(driver)
        seach_button_forgot = ForgotPageBurger(driver)
        seach_button_reset = ResetPasswordPageBurger(driver)

        seach_button_login.open_page(DataUrl.LOGIN_URL)
        seach_button_login.click_recover_password()
        seach_button_forgot.entering_password_recovery_email()
        seach_button_reset.wait_element(ResetPasswordPageLocators.EYE_BUTTON)
        seach_button_reset.click_eye_button()
        active = seach_button_reset.active_input()

        assert active.is_displayed() == True
