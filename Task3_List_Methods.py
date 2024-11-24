# List Methods
# Python provides several methods to manipulate lists. Here’s the list:

# 1. index(item, [start], [end]) – Returns the index of the first occurrence of the element.

list1=[1,2,3,4,5,6,7,8,9]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
print(list1.index(2))
print(list2.index("Isha"))

# 2. count(item) – Returns the count of the element in the list.

list1=[1,2,3,4,5,6,7,8,9]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
print(list1.count(2))
print(list2.count("Nitisha"))

# 3. sort(key=None, reverse=False) – Sorts the list in place.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
list1.sort()  
print("Sorted list1:", list1) 

list2.sort(reverse=True)  
print("Sorted list2:", list2)

# 4. append(element) - Adds an element to the end of the list.

list1=[1,2,3,4,5,6,7,8,9]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
list1.append(15)
print("After appending to list1:", list1)

list2.append("Riya")
print("After appending to list2:", list2)

# 5. append(element) - Adds an element to the end of the list.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
list1.extend([20, 25])
print("After extending list1:", list1)

list2.extend(["Pooja", "Megha"])
print("After extending list2:", list2)

# 6. insert(index, element) - Inserts an element at a specific index.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
list1.insert(2, 99)
print("After inserting into list1:", list1)

list2.insert(3, "Shreya")
print("After inserting into list2:", list2)

# 7. remove(element) - Removes the first occurrence of the specified element.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
list1.remove(8)
print("After removing from list1:", list1)

list2.remove("Nidhi")
print("After removing from list2:", list2)

# 8. pop(index) - Removes and returns the element at the specified index. If no index is provided, it removes the last element.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
popped_element1 = list1.pop(3)
print("After popping from list1:", list1)
print("Popped element:", popped_element1)

popped_element2 = list2.pop()
print("After popping from list2:", list2)
print("Popped element:", popped_element2)

# 9. clear() - Removes all elements from the list.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
temp_list1 = list1.copy()  
temp_list1.clear()
print("After clearing temp_list1:", temp_list1)

temp_list2 = list2.copy()
temp_list2.clear()
print("After clearing temp_list2:", temp_list2)

# 10. reverse() - Reverses the list in place.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
list1.reverse()
print("Reversed list1:", list1)

list2.reverse()
print("Reversed list2:", list2)

# 11. copy() - Returns a shallow copy of the list.

list1=[1,2,3,4,5,6,7,8,12,8,2,9,10]
list2=["Nitisha","Nidhi","Isha","Leetika","Swara"]
copy_list1 = list1.copy()
print("Copied list1:", copy_list1)

copy_list2 = list2.copy()
print("Copied list2:", copy_list2)



