# 9. Find the max sum of subarray

# Ex L = [-2, -3, 4, -1, -2, 1, 5, -3]
# Output = 7
a=[-2, -3, 4, -1, -2, 1, 5, -3]
max=max(a)
for i in range(len(a)-1):
    for j in range(1+i,len(a)):
        if sum(a[i:j])>max:
            max=sum(a[i:j])
print(max)