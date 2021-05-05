import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: es or fr")

@pytest.fixture(scope="function")
def option_lang(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser():
    try:
        browser = webdriver.Chrome()
    except:
        raise pytest.UsageError("Error during open the browser")
    yield browser
    print("\nquit browser..")
    browser.quit()
