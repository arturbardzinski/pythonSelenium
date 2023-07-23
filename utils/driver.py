from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="module")
def driver():
    # ścieżka do webdrivera
    webdriver_path = '/Users/arturbardzinski/Selenium/chromedriver'

    # Tworzymy opcje dla przeglądarki Chrome
    options = Options()

    # Ścieżka do przeglądarki Chrome
    # W zależności od twojego systemu, prawdziwa ścieżka do Chrome może być inna
    chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

    # Dodajemy ścieżkę do przeglądarki Chrome do naszych opcji
    options.binary_location = chrome_path

    # Utwórz instancję webdrivera Chrome
    driver = webdriver.Chrome(service=Service(webdriver_path), options=options)

    yield driver
    driver.quit()
