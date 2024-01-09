# 18. Find the majority element of the given list.

# Majority element: count of the element > N/2

# N = length of list

# A = [5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
# Ans = 5

a=[5, 2, 3, 5, 1, 5, 1, 2, 5, 5, 5]
max=0
val=0
for i in a:
    if max<a.count(i):
        max=a.count(i)
        val=i
print(val)