import pytest
from selenium import webdriver
from msedge.selenium_tools import EdgeOptions
import os

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
    parser.addoption(
        "--headless_mode", action="store", default="True"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    headless_mode = request.config.getoption("headless_mode")
    global driver
    print(os.path.abspath(os.curdir))

    if browser_name.lower() == "chrome":
        chrome_options = webdriver.ChromeOptions()
        if headless_mode.lower() == "true":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(executable_path="C:\\WorkspacePython\\PythonFramework_V2\\DriverManager"
                                                  "\\Chrome\\chromedriver.exe", options=chrome_options)

    elif browser_name.lower() == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        if headless_mode.lower() == "true":
            firefox_options.add_argument("--headless")
            firefox_options.add_argument("--disable-gpu")
        driver = webdriver.Firefox(executable_path="C:\\WorkspacePython\\PythonFramework_V2\\DriverManager"
                                                   "\\FireFox\\geckodriver.exe", options=firefox_options)

    elif browser_name.lower() == "edge":
        edge_options = EdgeOptions()
        edge_options.use_chromium = True
        if headless_mode.lower() == "true":
            edge_options.add_argument("--headless")
            edge_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path="C:\\WorkspacePython\\PythonFramework_V2\\DriverManager\\"
                                                  "Edge\\msedgedriver.exe", options=edge_options)

    else:
        chrome_options = webdriver.ChromeOptions()
        if headless_mode.lower() == "true":
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")

        driver = webdriver.Chrome(executable_path="C:\\WorkspacePython\\pythonProject\\chromedriver.exe",
                                  options=chrome_options)

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
