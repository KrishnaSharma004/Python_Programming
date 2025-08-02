# Creating a Python list with different data types
a = [10, 20, "GfG", 40, True]
print(a)

# Accessing elements using indexing
print(a[0])  # 10
print(a[1])  # 20
print(a[2])  # "GfG"
print(a[3])  # 40
print(a[4])  # True

# Checking types of elements
print(type(a[2]))  # str
print(type(a[4]))  # bool

# From a tuple
b = list((1, 2, 3, 'apple', 4.5))  
print(b)

# Initialize an empty list
c = []

# Adding 10 to end of list
c.append(10)  
print("After append(10):", c)  

# Inserting 5 at index 0
c.insert(0, 5)
print("After insert(0, 5):", c) 

# Adding multiple elements  [15, 20, 25] at the end
c.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", c)

a1 = [10, 20, 30, 40, 50]

# Removes the first occurrence of 30
a1.remove(30)  
print("After remove(30):", a1)

# Removes the element at index 1 (20)
popped_val = a1.pop(1)  
print("Popped element:", popped_val)
print("After pop(1):", a1) 

# Deletes the first element (10)
del a1[0]  
print("After del a[0]:", a1)