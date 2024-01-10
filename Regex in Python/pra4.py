# Loop through the list and apply the regex to each element so that only items 
# ending with a semicolon (;) are matched

import re
s=["fddsf Gfg;", "9;", "adfs is", "fasdf best;", "fssdf;"]
lis=[]
for str in s:
    arr=re.fullmatch(r'[\ \w \W]*;$',str)
    if arr:
        lis.append(str)
print(lis)
    