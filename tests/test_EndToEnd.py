import time

from pageObjects.FormPage import FormPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        expected_title = "ProtoCommerce"
        expected_name = "Arpita"
        email_id = "arpi@mail.com"
        password_id = "fuckarpi"
        checkbox_expected = "Check me out if you Love IceCreams!"
        gender_selected = "Female"

    # ___________________ FORM PAGE _________________________________________________________________

        log = self.getLogger()
        form_page = FormPage(self.driver)
        log.info("End 2 End Test")

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

        basket_page = form_page.clickOnShopLink()

        self.driver.maximize_window()

    # ______________________________PHOTO COMMERCE APPLICATION___________________________________________________

    # ______________________________BASKET PAGE_________________________________________________________

        photo_commerce_header_text = "ProtoCommerce Home"

        # basket_page = BasketPage(self.driver)

        self.waitForVisibilityOfElementLocated(basket_page.getBasketPageHeaderElement(), 4)

        assert photo_commerce_header_text == basket_page.getBasketPageHeader().text

        # assert "0" in str(driver.execute_script("arguments[0].text",checkout_button))
        # select_mobile("Nokia")
        basket_page.selectDesiredMobile("Nokia")
        # assert str(1) in checkout_button.text
        basket_page.selectDesiredMobile("Note 8")
        basket_page.selectDesiredMobile("berry")

        checkout_page = basket_page.clickOnBasketPageCheckoutBtn()

    # ________________________________CHECKOUT PAGE_________________________________________________________

        # checkout_page = CheckoutPage(self.driver)

        self.waitForElementPresence(checkout_page.getTableHeaderElement())

        # assert total_cost() == checkout_page.getActualTotalCost()
        assert checkout_page.calculateTotalCost() == checkout_page.getActualTotalCost()
        confirmation_page = checkout_page.clickCheckOutBtn()

    # ________________________________CONFIRMATION PAGE_________________________________________________________

        # confirmation_page = ConfirmationPage(self.driver)

        confirmation_page.selectDesiredCountry()

        assert not confirmation_page.getTNCCheckBox().is_selected()

        confirmation_page.getTNCOption().click()
        time.sleep(2)

        assert "Terms And Conditions" == confirmation_page.getTNCAlertText().text
        confirmation_page.getTNCAlertConfBtn().click()
        assert confirmation_page.getTNCCheckBox().is_selected()

        confirmation_page.getPurchaseBtn().click()
        assert "Success!" in confirmation_page.getPurchaseSuccessAlert().text

        # self.driver.get_screenshot_as_file("test.png")
        # self.driver.quit()

