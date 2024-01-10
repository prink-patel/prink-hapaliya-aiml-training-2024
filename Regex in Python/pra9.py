#    9. Filter all elements that contain a sequence of lowercase alphabets followed by - 
# followed by digits. They can be optionally surrounded by {{ and }}. Any partial match 
# shouldn't be part of the output.

# Sample input: ['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
# Sample output: ['{{apple-150}}', 'grape-87'] #[^{{\b}}]
import re
s=['{{apple-150}}', '{{mango2-100}}', '{{cherry-200', 'grape-87']
out=[]
for string in s:
    arr=re.fullmatch(r"({{){1}[a-z]+-\d+(}}){1}|({{){0}[a-z]+-\d+(}}){0}",string)
    if arr:
        out.append(string)
print(out)