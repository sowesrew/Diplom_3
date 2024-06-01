import pytest
from selenium import webdriver
from data import DataUrl


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/login')
    yield browser
    browser.quit()
