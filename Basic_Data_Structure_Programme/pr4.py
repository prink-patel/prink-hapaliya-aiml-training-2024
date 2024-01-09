# 4. Find the intersection (common) of two sets and remove those elements from the first set.

# Sample: {23, 42, 65, 57, 78, 83, 29} 
# {57, 83, 29, 67, 73, 43, 48}
# Result: {57, 83, 29}, {65, 42, 78, 23}
a={23, 42, 65, 57, 78, 83, 29} 
b={57, 83, 29, 67, 73, 43, 48}
c=a.intersection(b) 
d=a-b
print(c,d)