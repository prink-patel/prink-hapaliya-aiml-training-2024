t = int(input())

while t != 0:
    n = int(input())
    d = list(map(int, input().split()))
    t-=1
    a=set(d)
    print(len(a))