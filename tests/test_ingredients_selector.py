from elements_locators import Locators


class TestSelector:

    def test_fillers_selector(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.FILLERS).click()
        assert driver.find_element(*Locators.SELECTED_FILLERS).is_displayed() == True

    def test_sauces_selector(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.SAUCES).click()
        assert driver.find_element(*Locators.SELECTED_SAUCES).is_displayed() == True

    def test_buns_selector(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/')
        driver.find_element(*Locators.FILLERS).click()
        driver.find_element(*Locators.BUNS).click()
        assert driver.find_element(*Locators.SELECTED_BUNS).is_displayed() == True
