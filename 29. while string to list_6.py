sentense=input("Enter the string:-")
sentense_list=[]
length=len(sentense)
i=0
var=""
while i<len(sentense):
    if sentense[i]==" ":
        sentense_list.append(var)
        var=""
    elif sentense[i]!=" ":
        var=var+sentense[i]
    if i<=len(sentense):
        sentense_list.append(var)
print(sentense_list)