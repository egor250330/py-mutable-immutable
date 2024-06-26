from typing import Dict, List, Any

var1 = lucky_number = 777
var2 = pi = 3.14
var3 = one_is_a_prime_number = False
var4 = name = "Richard"
var5 = my_favourite_films = [
    "The Shawshank Redemption",
    "The Lord of the Rings: The Return of the King",
    "Pulp Fiction",
    "The Good, the Bad and the Ugly",
    "The Matrix",
]
var6 = profile_info = ("michel", "michel@gmail.com", "12345678")
var7 = marks = {
    "John": 4,
    "Sergio": 3,
}
var8 = collection_of_coins = {1, 2, 25}

sorted_variables: Dict[str, List[Any]] = {
    "mutable": [],
    "immutable": []
}


def is_mutable(obj: Any) -> bool:
    mutable_types = (list, dict, set)
    return isinstance(obj, mutable_types)


variables = [var1, var2, var3, var4, var5, var6, var7, var8]

for data_item in variables:
    if is_mutable(data_item):
        sorted_variables["mutable"].append(data_item)
    else:
        sorted_variables["immutable"].append(data_item)


print(sorted_variables)
