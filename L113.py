#Grace Anspach and Breanna Eafon
name_list = ["Hoffman","Rosemary","Gallaway","Gabby","Bong","Saerin","Anspach","Grace","Berlage","Bethany","Busk","Olivia","Eafon","Breanna","Nixon","Emily","O'Roark","Katherine","Paradiso","Vincenza","Stephenson","Sarah","Dockery","Krista"]

last_name=name_list[::2]
# print(last_name)

freq_dict = {}

for last_name in name_list.values():
    if last_name in freq_dict:
        freq_dict[last_name] += 1
    else:
        freq_dict[last_name] = 1


def invert_dict(freq_dict):
    inverse=dict()
    for key in freq_dict:
        val=freq_dict[key]
        if val not in inverse:
            inverse[val]=[key]
        else:
            inverse[val].append(key)
    return inverse


print(invert_dict)
