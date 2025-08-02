a = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a.remove(30)  
print("After remove(30):", a)

# Removes the element at index 1 (20)
popped_val = a.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a) 

# Deletes the first element (10)
del a[0]  
print("After del a[0]:", a)

# Accessing Tuple with Indexing
tup = tuple("Geeks")
print(tup[0])

# Accessing a range of elements using slicing
print(tup[1:4])  
print(tup[:3])

# Tuple unpacking
tup1 = ("Geeks", "For", "Geeks")

# This line unpack values of Tuple1
a1, b, c = tup1
print(a1)
print(b)
print(c)

tup2 = tuple('GEEKSFORGEEKS')

# Removing First element
print(tup2[1:])

# Reversing the Tuple
print(tup2[::-1])

# Printing elements of a Range
print(tup2[4:9])