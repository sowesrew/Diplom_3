import pytest
from selenium import webdriver
from data import DataUrl


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
        browser.fullscreen_window()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()
        browser.fullscreen_window()
    yield browser
    browser.quit()
