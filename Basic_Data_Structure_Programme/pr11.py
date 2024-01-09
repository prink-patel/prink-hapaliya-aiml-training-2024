# . Return product of minimum of odd and maximum of even from a given list.

# Ex. A = [7, 5,  2, 3, 12, 9, 15, 24]
# Output = 72          #  (24 max even * 3 min odd)
A = [7, 5,  2, 3, 12, 9, 15, 24]
max=max([x for x in A if x%2==0])
min=min([x for x in A if x%2==1])

for i in A:
    if i>max and i%2==0:
        max=i
    elif i<min and i%2==1:
        min=i
print(max*min)