string1="Kayalvizhi"
string2="Thiyagarajan"
maxlength=len(string1)+len(string2)
res=""
print("Length of string is",len(string1),len(string2),maxlength)
for i in range(maxlength):
    if i <len(string1):
        res+=string1[i]
    if i < len(string2):
        res+=string2[i]
print(res)

print("Concatenate",string1 +" " + string2)
print("String reverse", string1[::-1])
list1=list(string1.lower())
Vowels=['a','e','i','o','u']
print("vowels",list1,Vowels)
output=[]
for i in range(len(Vowels)):
    for l in range(len(string1)):
        if Vowels[i] in string1[l]:
            print("position & its character",Vowels[i],l)
            output.append(l)
            output.append(Vowels[i])
print("The END", output)

