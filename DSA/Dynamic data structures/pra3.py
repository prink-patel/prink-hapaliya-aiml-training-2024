t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
# Your code goes here
    a.sort()
    max1=a[-1]
    for i in range(len(a)-1,0,-1):
        if max1 != a[i]:
            max1+=a[i]
            break
    print(max1)
