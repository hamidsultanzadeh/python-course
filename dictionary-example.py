my_dict = {
    "name": "Hamid",
    "surname": "Sultanzadeh"
}

print(my_dict)

print(my_dict["name"], my_dict["surname"])

print(my_dict.get("n","Key does not exist"))

print(len(my_dict))

print("Keys",my_dict.keys())
print("Values",my_dict.values())

for i in my_dict.items():
    print(i)

my_dict["place"] = "azerbaijan"

# my_dict.pop("name")
# my_dict.popitem()
print(my_dict)
