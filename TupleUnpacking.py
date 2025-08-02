tup = (1, 2, 3, 4, 5)

a, *b, c = tup

print(a) 
print(b) 
print(c)

# Explanation:
# a gets the first item.
# c gets the last item.
# *b collects everything in between into a list.
