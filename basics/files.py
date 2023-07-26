file = open("countries_and_capitals.txt", "w+") # w+ odczyt i zapis

country_and_capitals = {"Poland": "Warsaw", "German": "Berlin"}

for country, capital in country_and_capitals.items():
    file.write(country + "-" + capital +"\n")

file.close()

###

file = open("countries_and_capitals.txt")
for line in file.readlines():
    print(line.strip())

file.close()