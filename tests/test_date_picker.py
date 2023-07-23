from pages.date_picker_page import DatePickerPage
from pages.main_page import MainPage


def test_date_picker(driver):
    main_page = MainPage(driver)
    main_page.load()
    main_page.go_to_date_picker()

    date_picker_page = DatePickerPage(driver)
    # Tutaj przeprowadzasz operacje i sprawdzenia na stronie date_picker.
