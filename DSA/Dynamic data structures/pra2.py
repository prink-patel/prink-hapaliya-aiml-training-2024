t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    count=0
# Your code goes here
    for i in range(n):
        if (a[i]*2) >= b[i] and a[i] <= (b[i]*2):
            count+=1
    print(count)