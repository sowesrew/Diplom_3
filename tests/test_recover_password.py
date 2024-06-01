from pages.base_page import BasePageBurger
from pages.login_page import LoginPageBurger
from pages.forgot_page import ForgotPageBurger
from pages.reset_password_page import ResetPasswordPageBurger
from conftest import driver
import allure
from data import DataUrl


class TestRecoverPassword:

    @allure.title("Проверка клика на значок глаза")
    def test_click_eye_button(self, driver):
        seach_button_login = LoginPageBurger(driver)
        seach_button_forgot = ForgotPageBurger(driver)
        seach_button_reset = ResetPasswordPageBurger(driver)
        seach_button_login.click_recover_password()
        seach_button_forgot.entering_password_recovery_email()
        not_activ = seach_button_reset.not_active_input()
        seach_button_reset.click_eye_button()
        activ = seach_button_reset.active_input()
        print(activ)
        print(not_activ)
        assert (not_activ is False and activ is True)
