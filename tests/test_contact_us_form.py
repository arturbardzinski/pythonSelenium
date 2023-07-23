from pages.contact_us_page import ContactUsPage
from pages.main_page import MainPage


def test_fill_contact_us_form(driver):
    main_page = MainPage(driver)
    main_page.load()
    main_page.go_to_contact_us()

    contact_us_page = ContactUsPage(driver)
    contact_us_page.set_first_name('Artur')
    contact_us_page.set_last_name('B')
