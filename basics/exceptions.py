country_and_capitals = {"Poland": "Warsaw", "German": "Berlin"}

try:
    print(2/0)
    print(country_and_capitals['USA'])  # ten kod ktory moze rzucic wyjatek
except KeyError:
    print("Klucz nie znaleziony")
except ZeroDivisionError:
    print("Nie dziel przez zero")
finally:
    print("To wykona sie zawsze")