import pytest

from pageObjects.FormPage import FormPage
from testData.HomePageTestData import HomePageTestData
from utilities.BaseClass import BaseClass


class TestFormFillUp(BaseClass):

    def test_FormSmoke(self, getData):
        expected_title = getData["title"]
        expected_name = getData["name"]
        email_id = getData["email"]
        password_id = getData["pwd"]
        checkbox_expected = "Check me out if you Love IceCreams!"
        gender_selected = getData["gender"]
        date_of_birth = getData["DOB"]

        log = self.getLogger()

        form_page = FormPage(self.driver)

        log.info("Validating Form Page Title")
        actual_title = form_page.getFormPageTitle()
        assert expected_title == actual_title
        log.info("Form Page Title Validation is successful")

        log.info("Entering text to the Name Field")
        form_page.getNameField().send_keys(expected_name)
        name_entered = form_page.getActualNameEntered()
        assert expected_name == name_entered
        log.info("Name is SuccessFully Entered in the Text Field")

        data_binding_text = form_page.getDataBindingFieldValue()
        assert expected_name == data_binding_text
        log.info("Data-Binding Validation Successful")

        log.info("Entering Text to Email Field")
        form_page.getEmailField().send_keys(email_id)
        log.info("Entering Text to PWD Field")
        form_page.getPasswordField().send_keys(password_id)

        log.info("Validating ice-cream checkbox is not selected")
        assert not form_page.getIceCreamCheckBox().is_selected()
        log.info("Clicking on  ice-cream checkbox")
        form_page.getIceCreamCheckBox().click()
        log.info("Validating ice-cream checkbox is selected")
        assert form_page.getIceCreamCheckBox().is_selected()
        log.info("ice-cream checkbox validation is successful")

        log.info("Validating ice-cream checkbox text")
        checkbox_label = form_page.getIceCreamCheckBoxLabel().text
        log.info("ice-cream checkbox text is :: "+checkbox_label)
        assert checkbox_label == checkbox_expected
        log.info("ice-cream checkbox text Validation is successful")

        log.info("Select the :: "+gender_selected+" from the dropdown")
        self.selectDropDownOptionByText(form_page.getGenderDropDown(), gender_selected)
        assert gender_selected == form_page.getGenderDropDownValue()
        log.info("value selected from dropdown is successful")

        log.info("validate employee radio button is not selected")
        assert not form_page.getEmploymentRadioBtn().is_selected()
        log.info("click on  employee radio button")
        form_page.getEmploymentRadioBtn().click()
        assert form_page.getEmploymentRadioBtn().is_selected()
        log.info("validate employee radio button is selected")

        log.info("Enter date of birth")
        form_page.getBirthDateField().send_keys(date_of_birth)
        log.info("Click on Form Submit Button")
        form_page.getFormSubmitButton().click()
        log.info("Submit Button is clicked")

        self.waitForElementPresence(form_page.getSuccessfulAlertLocator())

        success_text = form_page.getFormSubmitSuccessMsg().text
        assert "Success!" in success_text
        log.info("Form is successfully Submitted")
        self.driver.refresh()

    @pytest.fixture(params=HomePageTestData.test_Form_FillUp_Data)
    def getData(self, request):
        return request.param
