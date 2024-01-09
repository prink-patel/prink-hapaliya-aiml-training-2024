# 16. Find the elements of the given list which are exactly 
# the same as the entire product of the list except itself.

# A = [1, 5, 1, 10, 50]
# Ans = 50
# A = [1, 2, 4, 8, 1]
# Ans = 8
def prid(a,product):
    for i in a:
        if i==int(product/i):
            return i
    return "not possible"
a = [1, 2, 4, 8, 1]

product = 1

for num in a:
    product = product * num
print(prid(a,product))
