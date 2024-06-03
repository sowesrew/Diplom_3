from selenium.webdriver.common.by import By


class ProfilePageLocators:
    BUTTON_ORDER_HISTORY = [By.XPATH, ".//a[text() = 'История заказов']"] # История заказов
    BUTTON_EXIT = [By.XPATH, ".//button[text() = 'Выход']"] # кнопка "Выход"
