from selenium.webdriver.common.by import By


class MainPageLocators:
    BUTTON_PROFILE = (By.XPATH, ".//p[text() = 'Личный Кабинет']") # личный кабинет
    ELEMENT_BUN = [By.XPATH, ".//h2[text() = 'Булки']"] # заголовок "Булки

    P_KONSTRUCTOR = [By.XPATH, ".//p[text() = 'Конструктор']"]  # ссылка "Конструктор"
    ORDER_FFED = [By.XPATH, ".//p[text() = 'Лента Заказов']"] # ссылка "Лента заказов"
    HEAD_DETAIL_ING = [By.XPATH, ".//h2[text() = 'Детали ингредиента']"] # заголовок "Детали ингредиента"
    CLOSE_BUTTON = [By.XPATH, ".//section[contains(@class,'Modal_modal_opened__3ISw4')]//button"] # кнопка "закрыть" у ингредиента
    COUNTER_INGREDIENT_NULL = [By.XPATH, ".//ul[2]/a[1]//p[@class = 'counter_counter__num__3nue1'][text() = '0']"] # нулевой каунтер третьего ингредиента
    INGREDIENT_BUN = [By.XPATH, "//img[@alt = 'Флюоресцентная булка R2-D3']"] # Булка :3
    COUNTER_INGREDIENT = [By.XPATH, ".//ul[2]/a[1]//p[@class = 'counter_counter__num__3nue1'][text() = '1']"] # ненулевой каунтер
    INGREDIENT_SAUSE = [By.XPATH, ".//img[@alt = 'Соус Spicy-X']"]
    BUN_CONSTRUCTOR = [By.XPATH, ".//span[text() = 'Перетяните булочку сюда (верх)']"] # конструктор булочки
    BUTTON_REGISTER_ORDER = [By.XPATH, ".//button[text() = 'Оформить заказ']"] # кнопка "оформить заказ"

    NUMBER_ORDER_HEAD = [By.XPATH, ".//p[text() = 'идентификатор заказа']"] #заголовок "идентификатор заказа"