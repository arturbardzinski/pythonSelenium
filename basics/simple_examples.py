names_list = ["Shirek", "Artur", "Robert"]

names_list.reverse()
names_list.sort()
print(names_list[1])
print(names_list.pop(0))
for name in names_list:
    print(name)

print(names_list.count("Artur"))
print(len(names_list))

print("tuple, krotki")
# niezmienna, niemutowalna
names_tuple = ("Shirek", "Artur", "Robert")
person = ("Artur", "Bardzinski", 32)
print(person.count("Artur"))

print("set, zbiory")
# nie mogą być duplikaty, nie są uporzątkowane, nie są mutowalne, czyli nie mozna zmienic elementu w secie
names_set = {"Artur", "Shirek", "Artur", "Robert"}
print(names_set)
# tworzenie set
names_set1 = set()
names_set1.add("Sasia")
names_set1.remove("Sasia")
names_set1.discard("Sasia")  # tu mozemy usunac cos czego nie ma bez bledu

names_set2 = {"kot", "pies", "ptak"}
names_set3 = {"kot", "krolik", "ptak"}
# bierzemy elementty z pierwszego setu i usuwamy z niego elementy znalezione w drugim
names_difrence = names_set2.difference(names_set3)
for name in names_difrence:
    print(name)
# names_set2.clear()
names_inter = names_set2.intersection(names_set3)
for name in names_inter:
    print("elementy wspolne " + name)


# za pomoca extend do listy mozna doodac set
names_list.extend(names_set2)
print(names_list)
print("dictionary, slownik")

country_and_capitals = {"Poland": "Warsaw", "German": "Berlin"}
country_and_capitals["Czechia"] = "Prague"
print(country_and_capitals)

for key in country_and_capitals:
    print(key)

for k, v in country_and_capitals.items():
    print(k, v)

print(country_and_capitals["Poland"]) # blad jak by nie bylo polski
print(country_and_capitals.get("Poland")) # zwracany jest None jak nie ma

print(country_and_capitals.setdefault("USA", "Washington DC")) # jak nie ma usa do wstawia i dodaje
