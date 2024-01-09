# 7. Return the sum of duplicates elements from the given List

# Ex. L = [3, 5, 6, 11, 12, 3, 5, 2]
# Output = 8

a=[3, 5, 6, 11, 12, 3, 5, 2]
val=0
for i in set(a):
    if a.count(i)>1:
        val=val+i
print(val)