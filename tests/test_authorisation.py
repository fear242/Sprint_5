from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from user_data_gen import UserData
from elements_locators import Locators


class TestAuthorisation:

    def test_authorisation_button_enter_main(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ENTER_MAIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_MAKE_ORDER)))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed() == True

    def test_authorisation_button_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_MAKE_ORDER)))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed() == True

    def test_authorisation_from_reg_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_MAKE_ORDER)))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed() == True

    def test_authorisation_from_forgot_password_form(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_MAKE_ORDER)))
        assert driver.find_element(*Locators.BUTTON_MAKE_ORDER).is_displayed() == True
