def checkVowel(list1):
    li=[]
    vow="aeiouAEIOU"
    for i in list1:
        if i[0] in vow:
            print(i)
list1 = ["prink","hello","i","apple","hehe"]
checkVowel(list1)
