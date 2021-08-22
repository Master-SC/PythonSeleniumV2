from selenium.webdriver.common.by import By

from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    __total_price = (By.CSS_SELECTOR, "td.text-right h3 strong")
    __checkout_btn = (By.CSS_SELECTOR, "button.btn.btn-success")
    __individual_product_cost = (By.CSS_SELECTOR, "table tbody tr td:nth-child(4) strong")

    __table_header_locator = "table thead tr th:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def getTotalPriceField(self):
        return self.driver.find_element(*CheckoutPage.__total_price)

    def getCheckOutBtn(self):
        return self.driver.find_element(*CheckoutPage.__checkout_btn)

    def getActualTotalCost(self):
        return float(str(CheckoutPage.getTotalPriceField(self).text).split(" ")[1].strip())

    def getTableHeaderElement(self):
        return self.__table_header_locator

    def calculateTotalCost(self):
        price_list = self.driver.find_elements(*CheckoutPage.__individual_product_cost)
        total_price = 0
        for price in price_list:
            item_price = str(price.text)
            total_price += float(item_price.split(" ")[1].strip())
        return total_price

    def clickCheckOutBtn(self):
        CheckoutPage.getCheckOutBtn(self).click()
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page
