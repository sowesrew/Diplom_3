from selenium.webdriver.common.by import By


class ForgotPageLocators:
    # страница ввода почты
    RECOVER_EMAIL_INPUT = [By.XPATH, ".//input[@name = 'name']"]
    RECOVER_PASSWORD_BUTTON = [By.XPATH, ".//button[text() = 'Восстановить']"]
