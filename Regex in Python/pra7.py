# # Replace the space character that occurs after a word ending with a or r with a newline character
# Sample input: area, not a _a2_ roar took 22
# Sample output: 
# area
# not a    #([ar])\s
# _a2_ roar
# took 22
import re
s="area noat a _a2_ roar took 22"
arr=re.sub(r"([ar])\s",r"\1\n",s)
print(arr)