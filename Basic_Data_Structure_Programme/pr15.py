# 15. Calculate the sum of the major and minor diagonals of the given matrix.

# A = [ [2, 0, 7],[4, 1, 9],[8, 1, -1]]
# ans = 2, 16
a=[ [2, 0, 7],[4, 1, 9],[8, 1, -1]]
b=len(a)
a1=0
b1=0
for i in range(b):
    for j in range(b):
        if i==j:
            a1=a1+a[i][j]
        if ((i+j+1)%b)==0:
            b1=b1+a[i][j]
print(a1,b1)