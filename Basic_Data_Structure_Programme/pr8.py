# Count the subsequence “AG” in the given string.

# Ex. S = "BCAHGBNAJKGTYUALKWG"
# Output: 6
S = "BCAHGBNAJKTYUALKWGG"
count=0
val=0
for i in S:
    if i=='A':
        count+=1
    if i=='G':
        val+=count
print(val)