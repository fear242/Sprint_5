from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from user_data_gen import UserData
from elements_locators import Locators

class TestConstructorAccess:

    def test_acces_to_constructor_by_button(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ENTER_MAIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_CONSTRUCTOR)))
        driver.find_element(*Locators.BUTTON_CONSTRUCTOR).click()
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed() == True

    def test_acces_to_constructor_by_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ENTER_MAIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.HEADER_LOGO)))
        driver.find_element(*Locators.HEADER_LOGO).click()
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed() == True