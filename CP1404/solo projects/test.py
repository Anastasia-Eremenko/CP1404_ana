def create_dictionary(keys,values):
    new_dict = {}
    items = list[zip(keys,values)]
    print(items)
    hh = sorted(items)
#     for item in items:
#         new_dict[item[0]] = item[1]
#     return new_dict
#
calories = [737,3939,22,44]
food = ["bahh", "brr","bob", "neh"]
#
foods = create_dictionary(food,calories)
# print(foods)