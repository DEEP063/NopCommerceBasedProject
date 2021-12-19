from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    # driver=webdriver.Chrome(executable_path="C:\\ChromeDriver\\chromedriver.exe")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=".\\drivers\\ChromeDriver\\chromedriver.exe")
        print("Launching Chrome Browser......")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=".\\drivers\\FirefoxDriver\\geckodriver.exe")
        print("Launching Firefox Browser......")
    else:
        driver = webdriver.Chrome(executable_path=".\\drivers\\ChromeDriver\\chromedriver.exe")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
