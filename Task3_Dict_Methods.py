# 1. dict.clear() - Removes all items from the dictionary.

my_dict = {"name": "Nitisha", "age": 21, "city": "Pune"}
my_dict.clear()
print(my_dict)  


# 2. dict.copy() - Returns a shallow copy of the dictionary.

original_dict = {"name": "Nidhi", "age": 20}
copied_dict = original_dict.copy()
print(copied_dict)  

# 3. dict.fromkeys(iterable, value=None) - Creates a new dictionary with keys from the iterable and a default value.

keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  

# 4. dict.get(key, default=None) - Returns the value of the specified key. If the key doesn't exist, it returns the default value.

my_dict = {"name": "Isha", "age": 22}
value = my_dict.get("name")
print(value)

value_not_found = my_dict.get("address", "Not Found")
print(value_not_found)  

# 5. dict.items() - Returns a view object containing key-value pairs as tuples.

my_dict = {"name": "Swara", "age": 18}
items = my_dict.items()
print(items)  

# 6. dict.keys() - Returns a view object containing the dictionary's keys.

my_dict = {"name": "Leetika", "age": 25}
keys = my_dict.keys()
print(keys)  

# 7. dict.pop(key, default=None) - Removes and returns the value of the specified key. If the key doesn’t exist, it returns the default value.

my_dict = {"name": "Riya", "age": 24}
removed_value = my_dict.pop("name")
print(removed_value)  
print(my_dict)  

# 8. dict.popitem() - Removes and returns the last inserted key-value pair as a tuple. Raises KeyError if the dictionary is empty.

my_dict = {"name": "Nitisha", "age": 21}
last_item = my_dict.popitem()
print(last_item)  
print(my_dict)  

# 9. dict.update([other]) - Updates the dictionary with key-value pairs from another dictionary or iterable.

my_dict = {"name": "Nitisha", "age": 21}
my_dict.update({"city": "Pune", "country": "India"})
print(my_dict)  