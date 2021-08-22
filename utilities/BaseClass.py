import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def waitForElementPresence(self, element_css, time_in_sec=5):
        wait = WebDriverWait(self.driver, time_in_sec)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, element_css)))

    def waitForVisibilityOfElementLocated(self, css_selector, time_in_sec=6):
        wait = WebDriverWait(self.driver, time_in_sec)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))

    def selectDropDownOptionByText(self, locator_by_css, value):
        select_gender = Select(locator_by_css)
        select_gender.select_by_visible_text(value)

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler("logging.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger
