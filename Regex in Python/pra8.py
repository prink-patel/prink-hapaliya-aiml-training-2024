# 8. Split the given input string on one or more repeated sequences of cat using regex

# Sample input: firecatlioncatcatcatbearcatcatparrot
# Sample output: ['fire', 'lion', 'bear', 'parrot']
import re
s="firecatlioncatcatcatbearcatcatparrot"
arr=re.sub("cat+"," ",s)
print(arr.split())