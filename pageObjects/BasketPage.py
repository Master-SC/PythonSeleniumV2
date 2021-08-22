from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class BasketPage:

    __basket_page_header = (By.CSS_SELECTOR, "nav[class*=navbar-expand-lg] a.navbar-brand")
    __basket_page_checkout_btn = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")
    __basket_product_card = (By.CSS_SELECTOR, "div.card.h-100")
    __basket_page_mobile_title = (By.CSS_SELECTOR, "h4.card-title")
    __basket_page_mobile_add_cart = (By.CSS_SELECTOR, "div.card-footer button")

    __basket_page_header_element = "nav[class*=navbar-expand-lg] a.navbar-brand"

    def __init__(self, driver):
        self.driver = driver

    def getBasketPageHeader(self):
        return self.driver.find_element(*BasketPage.__basket_page_header)

    def getBasketPageCheckoutBtn(self):
        return self.driver.find_element(*BasketPage.__basket_page_checkout_btn)

    def getBasketPageHeaderElement(self):
        return self.__basket_page_header_element

    def selectDesiredMobile(self, mobile_name):
        list_mobile = self.driver.find_elements(*BasketPage.__basket_product_card)
        for mobile in list_mobile:
            if mobile_name in mobile.find_element(*BasketPage.__basket_page_mobile_title).text:
                mobile.find_element(*BasketPage.__basket_page_mobile_add_cart).click()
                break

    def clickOnBasketPageCheckoutBtn(self):
        self.driver.execute_script("arguments[0].click()", BasketPage.getBasketPageCheckoutBtn(self))
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
