# 13. Return the array which contains the elements which are greater than the all elements from its right side.

# Ex. A = [5, 17, 2, 6, 3]
# Output = [17, 6, 3]
a= [5, 17, 2, 6, 3]
a1=[]
for i in range(len(a)):
    if len(a)-1==i:
        a1.append(a[i])
    elif a[i]>a[i+1]:
        a1.append(a[i])
print(a1)
