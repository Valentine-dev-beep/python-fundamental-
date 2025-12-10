box_office = {"avatar":2009, "titanic":1997,"star_wars":2015, "avengers":2012}
#get()
print(box_office.get("avatar"))

#keys()
keys_only = box_office.keys()
print(keys_only)

#values
keys_only = box_office.keys()

print(keys_only)

#values()
values_only = box_office.values()
print(values_only)

#items()
key_value_pair = box_office.items()
print(key_value_pair)

for key, value in key_value_pair:
    print(key, value)
