# 2. Count the occurrence of each element from a list

# Sample: [11, 45, 8, 11, 23, 45, 23, 45, 89]

# Result: {11: 2, 45: 3, 8: 1, 23: 2, 89: 1}

a=[11, 45, 8, 11, 23, 45, 23, 45, 89]
result={}
for i in a:
    result[i]=a.count(i)
print(result)