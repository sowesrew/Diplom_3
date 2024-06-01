from selenium.webdriver.common.by import By


class LoginPageLocators:
    # страница логина
    RECOVER_PASSWORD = [By.XPATH, ".//a[text() = 'Восстановить пароль']"]
