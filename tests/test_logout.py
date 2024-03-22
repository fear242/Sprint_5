from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from user_data_gen import UserData
from elements_locators import Locators


class TestLogout:

    def test_logout_from_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.BUTTON_ENTER_MAIN).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(UserData.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(UserData.password)
        driver.find_element(*Locators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_ACCOUNT)))
        driver.find_element(*Locators.BUTTON_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_LOGOUT)))
        driver.find_element(*Locators.BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((Locators.BUTTON_LOGIN)))
        assert driver.find_element(*Locators.BUTTON_LOGIN).is_displayed() == True