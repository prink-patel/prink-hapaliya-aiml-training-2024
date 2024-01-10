# Write a regular expression to get only the part of the 
# email before the "@" sign and include the "@" sign
import re
s="""Write a regular prink121@gmail.com expression to search digits inside a string
Find the words with exactly 8 212letters from the paragraph using regex
Find the numbers starting with 2124 from a string.
Loop through the list and apply the 212 regex to each element so that only items ending with a semicolon (;) are matched
Write a regular expression to get only the part of the email before the "@" sign and include the "@" sign
Replace all special characters with space using regex
Replace the space character that occurs after a word ending with a or r with a newline character
Sample input: area, not a _a2_ roar""".split()
for str in s:
    arr=re.fullmatch(r"[\w.]+\@[\w.]+",str)
    
    if arr:
        print(str)
        arr1=re.split(r"@",str)
        print(arr1[0]+"@")