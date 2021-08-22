import pytest
from selenium.webdriver.support.select import Select

from pageObjects.FormPage import FormPage
from utilities.BaseClass import BaseClass


class TestFormPage(BaseClass):

    def test_FormSanity(self, getData):
        expected_title = "ProtoCommerce"
        expected_name = getData[0]
        email_id = getData[1]
        password_id = getData[2]
        checkbox_expected = "Check me out if you Love IceCreams!"
        gender_selected = getData[3]

        log = self.getLogger()

        form_page = FormPage(self.driver)

        log.info("Home Page Log in test_FormSanity")
        actual_title = form_page.getFormPageTitle()
        assert expected_title == actual_title

        form_page.getNameField().send_keys(expected_name)
        name_entered = form_page.getActualNameEntered()
        assert expected_name == name_entered

        data_binding_text = form_page.getDataBindingFieldValue()
        assert expected_name == data_binding_text

        form_page.getEmailField().send_keys(email_id)
        form_page.getPasswordField().send_keys(password_id)

        assert not form_page.getIceCreamCheckBox().is_selected()
        form_page.getIceCreamCheckBox().click()
        assert form_page.getIceCreamCheckBox().is_selected()

        checkbox_label = form_page.getIceCreamCheckBoxLabel().text
        assert checkbox_label == checkbox_expected

        self.selectDropDownOptionByText(form_page.getGenderDropDown(), gender_selected)
        assert gender_selected == form_page.getGenderDropDownValue()

        assert not form_page.getEmploymentRadioBtn().is_selected()
        form_page.getEmploymentRadioBtn().click()
        assert form_page.getEmploymentRadioBtn().is_selected()

        form_page.getBirthDateField().send_keys('11251995')
        form_page.getFormSubmitButton().click()

        self.waitForElementPresence(form_page.getSuccessfulAlertLocator())

        success_text = form_page.getFormSubmitSuccessMsg().text
        assert "Success!" in success_text
        self.driver.refresh()

    @pytest.fixture(params=[("Arpita", "arpi@mail.com", "fuckarpi", "Female"), ("Lulu", "Ansari", "lulurape", "Male")])
    def getData(self, request):
        return request.param
