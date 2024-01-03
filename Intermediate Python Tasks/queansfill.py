qus=[]
ans=[]
qfile = open("questions.txt","r")
quelines=qfile.readlines()

afile = open("answer.txt","r")
anslies=afile.readlines()

for line in quelines:
    qus.append(line)
qus.sort()

for line in anslies:
    ans.append(line)
ans.sort()

o=open('output.txt','w+')

for i in range(len(qus)):
    o.writelines(qus[i])
    o.writelines(ans[i])