countries_information = {}
countries_information["Polska"] = ("Warszawa", 38.9)
countries_information["Niemcy"] = ("Berlin", 83.9)
countries_information["Słowacja"] = ("Bratysława", 5.45)


def show_country_info(country):
    country_information = countries_information.get(country)
    print()
    print(country)
    print("-----")
    print("Stolica: " + country_information[0])
    print("Liczba: " + str(country_information[1]))


for country in countries_information.keys():
    print(country)

country = input("Jakie chcesz dane?")
show_country_info(country)


def calc_sum(a, b):
    return a + b


sum = calc_sum(2, 5)
print(sum)
