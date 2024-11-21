# Use a dictionary with nested dictionaries for better organization
countries_information = {
    "Polska": {"capital": "Warszawa", "population": 38.9},
    "Niemcy": {"capital": "Berlin", "population": 83.9},
    "Słowacja": {"capital": "Bratysława", "population": 5.45}
}

def show_country_info(country):
    if country not in countries_information:
        print(f"Country '{country}' not found")
        return
    
    info = countries_information[country]
    print(f"\n{country}\n-----")
    print(f"Stolica: {info['capital']}")
    print(f"Liczba: {info['population']}")

# Use list comprehension for displaying countries
available_countries = "\n".join(countries_information.keys())
print(f"Available countries:\n{available_countries}")

country = input("Jakie chcesz dane? ")
show_country_info(country)



import operator

def calculate(a, b, operation="add"):
    operations = {
        "add": operator.add,
        "subtract": operator.sub
    }
    return operations.get(operation, operator.add)(a, b)


# Usage
print(calculate(2, 5))  # Addition (default)
print(calculate(2, 5, "subtract"))  # Subtraction
