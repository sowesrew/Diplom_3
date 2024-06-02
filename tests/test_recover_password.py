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

    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_go_to_forgot_password(self, driver):
        seach_button_login = LoginPageBurger(driver)

        seach_button_login.open_page(DataUrl.LOGIN_URL)
        seach_button_login.click_recover_password()
        seach_button_login.wait_element(*ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        assert driver.current_url == DataUrl.FORGOT_PASS


    @allure.title("Проверка клика на значок глаза")
    def test_click_eye_button(self, driver):
        seach_button_login = LoginPageBurger(driver)
        seach_button_forgot = ForgotPageBurger(driver)
        seach_button_reset = ResetPasswordPageBurger(driver)

        seach_button_login.click_recover_password()
        seach_button_forgot.entering_password_recovery_email()
        seach_button_base = BasePageBurger(driver)
        seach_button_base.wait_element(ResetPasswordPageLocators.EYE_BUTTON)
        not_activ = seach_button_reset.not_active_input()
        seach_button_reset.click_eye_button()
        activ = seach_button_reset.active_input()
        is_hl = seach_button_reset.is_highlighted_input()
        print(activ)
        print(not_activ)
        print(is_hl)
        assert (expected_conditions.visibility_of_element_located(activ)
                and expected_conditions.visibility_of_element_located(is_hl))
