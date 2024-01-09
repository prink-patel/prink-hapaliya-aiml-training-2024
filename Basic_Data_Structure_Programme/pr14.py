# 14. Add 1 to given list elements. Do not use string conversion, number conversion.

# Ex. A = [1, 2, 3]
# Output = [1, 2, 4]
# A = [9, 9, 9]
# Output = [1, 0, 0, 0]
a= [1, 2, 3]
car=0
for i in range(len(a)-1,-1,-1):

    
    if a[i]==9:
        a[i]=0
        car=1
    elif car==1:
        a[i]=a[i]+1
        car=0
    else:
        a[i]=a[i]+1
        break
if car==1:
    a.insert(0,1)
print(a)