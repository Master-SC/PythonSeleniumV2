from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class ConfirmationPage:

    __tnc_checkbox = (By.CSS_SELECTOR, "input#checkbox2")
    __tnc_option = (By.XPATH, "//label[@for='checkbox2']/a")
    __tnc_alert = (By.CSS_SELECTOR, "div.nsm-dialog-animation-fade.nsm-dialog.nsm-dialog-open")
    __tnc_alert_confBtn = (By.CSS_SELECTOR, "button[class*=btn-info]")
    __tnc_h1_element = (By.CSS_SELECTOR, "h1")
    __purchase_Btn = (By.CSS_SELECTOR, "input[value='Purchase']")
    __purchase_success = (By.XPATH, "//div[contains(@class,'alert-success')]")
    __country_suggestion_dropdown_list = (By.CSS_SELECTOR, "div.suggestions ul li a")
    __country_input_element = (By.CSS_SELECTOR, "input#country")

    __country_suggestion = "div.suggestions"

    def __init__(self, driver):
        self.driver = driver

    def getTNCCheckBox(self):
        return self.driver.find_element(*ConfirmationPage.__tnc_checkbox)

    def getTNCOption(self):
        return self.driver.find_element(*ConfirmationPage.__tnc_option)

    def getTNCAlert(self):
        return self.driver.find_element(*ConfirmationPage.__tnc_alert)

    def getTNCAlertText(self):
        return ConfirmationPage.getTNCAlert(self).find_element(*ConfirmationPage.__tnc_h1_element)

    def getTNCAlertConfBtn(self):
        return ConfirmationPage.getTNCAlert(self).find_element(*ConfirmationPage.__tnc_alert_confBtn)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmationPage.__purchase_Btn)

    def selectDesiredCountry(self, country_suggestion="ind", country="India"):
        country_drop_down = self.driver.find_element(*ConfirmationPage.__country_input_element)
        country_drop_down.send_keys(country_suggestion)
        waited = WebDriverWait(self.driver, 8)
        waited.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "div.suggestions")))
        suggestion_options = self.driver.find_elements(*ConfirmationPage.__country_suggestion_dropdown_list)
        for suggestion in suggestion_options:
            if country in suggestion.text:
                suggestion.click()
                break
        assert country == country_drop_down.get_attribute("value")

    def getPurchaseSuccessAlert(self):
        return self.driver.find_element(*ConfirmationPage.__purchase_success)
