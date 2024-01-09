# 17. Print reverse string using recursion.

# S = "helloworld"
# Ans = "dlrowolleh"
def rev(a):
    if len(a) == 0:
        return a
    else:
        return rev(a[1:]) + a[0]


a= "helloworld"
print(rev(a))
