from locators.login_page_locators import LoginPageLocators
from pages.login_page import LoginPageBurger
from pages.forgot_page import ForgotPageBurger
from pages.reset_password_page import ResetPasswordPageBurger
from conftest import driver
import allure
from data import DataUrl
from locators.reset_password_page_locators import ResetPasswordPageLocators
from locators.forgot_page_locators import ForgotPageLocators


class TestRecoverPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_forgot_password(self, driver):
        login = LoginPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.click_recover_password()

        assert driver.current_url == DataUrl.FORGOT_PASS

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_go_to_reset_password(self, driver):
        login = LoginPageBurger(driver)
        forgot = ForgotPageBurger(driver)
        reset = ResetPasswordPageBurger(driver)

        login.open_page_and_wait(DataUrl.LOGIN_URL, LoginPageLocators.LOGIN_BUTTON)
        login.click_recover_password()
        login.wait_element_and_clickable(ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        forgot.entering_password_recovery_email()
        reset.wait_element_and_clickable(ResetPasswordPageLocators.EYE_BUTTON)

        assert driver.current_url == DataUrl.RESET_PASS

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.")
    def test_click_eye_button(self, driver):
        login = LoginPageBurger(driver)
        forgot = ForgotPageBurger(driver)
        reset = ResetPasswordPageBurger(driver)

        login.open_page(DataUrl.LOGIN_URL)
        login.click_recover_password()
        forgot.wait_element_and_clickable(ForgotPageLocators.RECOVER_PASSWORD_BUTTON)
        forgot.entering_password_recovery_email()
        reset.wait_element_and_clickable(ResetPasswordPageLocators.EYE_BUTTON)
        reset.click_eye_button()
        active = reset.active_input()

        assert active.is_displayed() == True
