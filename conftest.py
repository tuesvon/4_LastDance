import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OptGC
from selenium.webdriver.firefox.options import Options as OptFF

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose language: ru, en, es, fr...etc...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_name = request.config.getoption("language")

    if browser_name == "chrome":
        optionsGC = OptGC()
        optionsGC.add_experimental_option('prefs', {'intl.accept_languages': language_name})
        print(f"\nЗапуск теста с помощью {browser_name}. Язык интерфейса: {language_name}")
        browser = webdriver.Chrome(options=optionsGC)
    elif browser_name == "firefox":
        optionsFF = OptFF()
        optionsFF.set_preference("intl.accept_languages", language_name)
        print(f"\nЗапуск теста с помощью {browser_name}. Язык интерфейса: {language_name}")
        browser = webdriver.Firefox(options=optionsFF)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nЗавершение теста")
    browser.quit()






