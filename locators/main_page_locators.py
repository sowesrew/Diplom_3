from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_PROFILE = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # личный кабинет
    ELEMENT_BUN = [By.XPATH, ".//h2[text() = 'Булки']"] # заголовок "Булки
