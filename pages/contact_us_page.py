from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContactUsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = '//*[@id="contact_form"]/input[1]'
        self.last_name_input = '//*[@id="contact_form"]/input[2]'

    def set_first_name(self, first_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.first_name_input))
        ).send_keys(first_name)

    def set_last_name(self, last_name):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.last_name_input))
        ).send_keys(last_name)
