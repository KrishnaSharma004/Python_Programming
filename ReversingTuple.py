#using slicing :
t = (1, 2, 3, 4, 5) 
# Reverse the tuple using slicing with a step of -1
rev = t[::-1]

print(rev)

#using reversed() :
t1 = (1, 2, 3, 4, 5)  
# Reverse the tuple using the built-in reversed() function and convert it back to a tuple
rev1 = tuple(reversed(t1))
print(rev1)

#using loops :
t2 = (1, 2, 3, 4, 5)  
# Reverse the tuple by iterating through the indices in reverse order
rev2 = tuple(t2[i] for i in range(len(t2) - 1, -1, -1))
print(rev2)

#using collections.deque() :
from collections import deque  
t3 = (1, 2, 3, 4, 5)
deq = deque(t3)

# Reverse the deque in place
deq.reverse()

# Convert the reversed deque back to a tuple
rev3 = tuple(deq)

print(rev3)