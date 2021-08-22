from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.BasketPage import BasketPage


class FormPage:

    __name = (By.CSS_SELECTOR, "input[name=name]:nth-child(2)")
    __data_binding = (By.XPATH, "(//input[@name='name'])[2]")
    __email = (By.CSS_SELECTOR, "input[name='email']")
    __password = (By.CSS_SELECTOR, "input[placeholder='Password']")
    __checkbox_iceCream = (By.CSS_SELECTOR, "div.form-check input#exampleCheck1")
    __checkbox_label = (By.XPATH, "//div[@class='form-check']/label")
    __gender_dropdown = (By.CSS_SELECTOR, "select#exampleFormControlSelect1")
    __employment_radioBtn = (By.CSS_SELECTOR, "input#inlineRadio2")
    __dateOfBirth = (By.CSS_SELECTOR, "input[name='bday']")
    __form_submitBtn = (By.XPATH, "//input[@value='Submit']")
    __Form_Success_Msg = (By.CSS_SELECTOR, "div[class*='alert alert-success alert-dismissible']")
    __shop_link = (By.XPATH, "//a[contains(@href,'shop')]")

    __success_alert_msg_locator = "div[class*='alert alert-success alert-dismissible']"

    def __init__(self, driver):
        self.driver = driver

    def getNameField(self):
        return self.driver.find_element(*FormPage.__name)

    def getDataBindingField(self):
        return self.driver.find_element(*FormPage.__data_binding)

    def getEmailField(self):
        return self.driver.find_element(*FormPage.__email)

    def getPasswordField(self):
        return self.driver.find_element(*FormPage.__password)

    def getIceCreamCheckBox(self):
        return self.driver.find_element(*FormPage.__checkbox_iceCream)

    def getIceCreamCheckBoxLabel(self):
        return self.driver.find_element(*FormPage.__checkbox_label)

    def getGenderDropDown(self):
        return self.driver.find_element(*FormPage.__gender_dropdown)

    def getEmploymentRadioBtn(self):
        return self.driver.find_element(*FormPage.__employment_radioBtn)

    def getBirthDateField(self):
        return self.driver.find_element(*FormPage.__dateOfBirth)

    def getFormSubmitButton(self):
        return self.driver.find_element(*FormPage.__form_submitBtn)

    def getFormSubmitSuccessMsg(self):
        return self.driver.find_element(*FormPage.__Form_Success_Msg)

    def getShopLink(self):
        return self.driver.find_element(*FormPage.__shop_link)

    def getDataBindingFieldValue(self):
        return FormPage.getDataBindingField(self).get_attribute("value")

    def getGenderDropDownValue(self):
        return FormPage.getGenderDropDown(self).get_attribute("value")

    def getActualNameEntered(self):
        return self.driver.execute_script("return document.getElementsByName('name')[1].value;")

    def getFormPageTitle(self):
        return self.driver.title

    def getSuccessfulAlertLocator(self):
        return self.__success_alert_msg_locator

    def clickOnShopLink(self):
        FormPage.getShopLink(self).click()
        basket_page = BasketPage(self.driver)
        return basket_page


