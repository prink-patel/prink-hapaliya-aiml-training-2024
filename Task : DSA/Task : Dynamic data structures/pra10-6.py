# Lapindrome is defined as a string which when split in the middle, gives two halves
# having the same characters and same frequency of each character. If there are odd
# number of characters in the string, we ignore the middle character and check for
# lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have
# the same characters with same frequency. Also, abccab, rotor and xyzxy are a few
#  examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain
#  the same characters but their frequencies do not match.
# input
# 6
# gaga
# abcde
# rotor
# xyzxy
# abbaab
# ababc

n=int(input())
lis=[]
for i in range(n):
    a=input()
    lis.append(a)
for i in lis:
    z=0
    l=int(len(i)/2)
    if i[::-1]==i:
        print("YES")
        break
    if len(i)%2==1:
        z=l+1
    else:
        z=l
    a=i[z:]
    b=i[:l]
    if a==b:
        print("YES")
    else:
        print("NO")

