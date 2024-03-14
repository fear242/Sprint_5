from selenium.webdriver.common.by import By


class Locators:
    INPUT_NAME = By.XPATH, '//label[text()="Имя"]/following::input'
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following::input'
    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following::input'
    BUTTON_REGISTRATION = By.XPATH, '//*[text()="Зарегистрироваться"]'
    BUTTON_ENTER_MAIN = By.XPATH, '//*[text()="Войти в аккаунт"]'
    BUTTON_ACCOUNT = By.XPATH, '//*[@href="/account"]'
    BUTTON_LOGIN = By.XPATH, '//*[text()="Войти"]'
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[text()="Конструктор"]'
    BUTTON_MAKE_ORDER = By.XPATH, '//*[text()="Оформить заказ"]'
    HEADER_LOGO = By.XPATH, '//*[starts-with(@class,"AppHeader_header__logo")]'
    BUNS = By.XPATH, '//*[text()="Булки"]'
    SELECTED_BUNS = By.XPATH, '//*[text()="Булки" and contains(@class, "default")]'
    SAUCES = By.XPATH, '//*[text()="Соусы"]'
    SELECTED_SAUCES = By.XPATH, '//*[text()="Соусы" and contains(@class, "default")]'
    FILLERS = By.XPATH, '//*[text()="Начинки"]'
    SELECTED_FILLERS = By.XPATH, '//*[text()="Начинки" and contains(@class, "default")]'
    INCORRECT_PASSWORD = By.XPATH, '//*[text()="Некорректный пароль"]'
    ORDERS_HISTORY = By.XPATH, '//*[@href="/account/order-history"]'
    BUTTON_LOGOUT = By.XPATH, '//*[text()="Выход"]'
