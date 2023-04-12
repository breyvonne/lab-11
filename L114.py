#Grace Anspach and Breanna Eafon
red_velvet={
    "oil":"2",
    "flour":"2.5",
    "sugar":"1.5",
    "baking_soda":"1",
    "eggs":"2",
    "red_color":"2"
}

lemon_cake={
    "flour":"1.5",
    "sugar":"1",
    "baking_soda":"1.5",
    "eggs":"2",
    "lemon_zest":"1"
}


shared=set(red_velvet.items()) & set(lemon_cake.items())
print(shared)
