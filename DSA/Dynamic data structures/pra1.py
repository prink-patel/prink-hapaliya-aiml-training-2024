t = int(input())

while t > 0:
    n = int(input())
    d = list(map(int, input().split()))
    t -= 1
    a=-1
    for i in range(n-1):
        different = d[0]
        if (d[i+1] - d[i]) < 0 :
            a=0
            break
    if a==0:
        print("No")
    else:
        print("Yes")

