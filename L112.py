#Grace Anspach and Breanna Eafon
name_dict = {
    "Hoffman":"Rosemary",
    "Gallaway":"Gabby",
    "Bong":"Saerin",
    "Anspach":"Grace",
    "Berlage":"Bethany",
    "Busk":"Olivia",
    "Eafon":"Breanna",
    "Nixon":"Emily",
    "O'Roark":"Katherine",
    "Paradiso":"Vincenza",
    "Stephenson":"Sarah",
    "Dockery":"Krista"
}
freq_dict = {}

for first_name in name_dict.values():
    if first_name in freq_dict:
        freq_dict[first_name] += 1
    else:
        freq_dict[first_name] = 1

print(freq_dict)
