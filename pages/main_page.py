from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get('https://webdriveruniversity.com')

    def go_to_contact_us(self):
        contact_us_link = self.driver.find_element(By.ID, 'contact-us').get_attribute('href')
        self.driver.get(contact_us_link)

    def go_to_date_picker(self):
        date_picker_link = self.driver.find_element(By.ID, 'datepicker').get_attribute('href')
        self.driver.get(date_picker_link)
