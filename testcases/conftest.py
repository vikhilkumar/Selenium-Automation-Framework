#Session 48
import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope="class",autouse=True)   #use of this is.. to call this setup function inside test_searchflights class. scope='class' will applicable class level.
def setup(request,browser):           #request fixture is a special fixture providing  information of the requesting test function.
    driver = webdriver.Chrome()
    # if browser=='chrome':
    #     driver = webdriver.Chrome()
    # elif browser=='firefox':
    #     driver=webdriver.Firefox()
    # elif browser=='edge':
    #     driver=webdriver.Edge()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    request.cls.driver=driver
    # wait=WebDriverWait(driver,10)
    # request.cls.wait = wait
    yield              #Anything you put after yield is teardown method
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope='class',autouse=True)
def browser(request):
    return request.config.getoption("--browser")


def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.instance.driver
        screenshot_path = os.path.join(os.path.dirname(__file__), "screenshots")
        os.makedirs(screenshot_path, exist_ok=True)
        screenshot_file = os.path.join(screenshot_path, f"{report.nodeid.replace('::', '_')}.png")
        driver.save_screenshot(screenshot_file)

def pytest_html_report_title(report):
    report.title = "Automation Report"

