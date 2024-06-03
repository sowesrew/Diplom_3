from selenium.webdriver.common.by import By


class LoginPageLocators:
    # страница логина
    RECOVER_PASSWORD = [By.XPATH, ".//a[text() = 'Восстановить пароль']"]
    LOGIN_BUTTON = [By.XPATH, ".//button[text() = 'Войти']"]

    INPUT_EMAIL = [By.XPATH, ".//label[text() = 'Email']/../input"]
    INPUT_PASSWORD = [By.XPATH, ".//label[text() = 'Пароль']/../input"]
