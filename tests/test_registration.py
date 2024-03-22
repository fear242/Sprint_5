from user_data_gen import UserData
from elements_locators import Locators


class TestRegistration:
    def test_registration_correct_password(self, driver):
        user = UserData()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.INPUT_NAME).send_keys('Flugengeheimen')
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(user.new_email())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user.new_password_correct())
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.BUTTON_LOGIN).is_displayed() == True

    def test_registration_incorrect_password(self, driver):
        user = UserData()
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.find_element(*Locators.INPUT_NAME).send_keys('Flugengeheimen')
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(user.new_email())
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(user.new_password_incorrect())
        driver.find_element(*Locators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*Locators.INCORRECT_PASSWORD).is_displayed() == True
