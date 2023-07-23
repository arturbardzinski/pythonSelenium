from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DatePickerPage:
    def __init__(self, driver):
        self.driver = driver

    # Tutaj dodajesz metody do interakcji ze stroną date_picker.
