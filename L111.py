#Grace Anspach and Breanna Eafon
dict = {
    "a":"1",
    "b":"2",
    "c":"3",
    "d":"4"
}

def my_get_method(dict,key,value):
    if key in dict:
        return dict[key]
    else:
        return value

print(my_get_method(dict,"a",0))
