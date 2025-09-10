import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("browser", action="store", default="chrome", help = "browser type from commandline")

@pytest.fexture
def browserInstance(request):
    browsername = request.config.getoption("browser")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
