a = "banana" # this is a string 
Dict = {} # I have taken a empty dictionary here in which i have to add the elments
for i in a: #here I have taken a for loop in which i eill check 'i' in string 'a'= "banana"
    if i in Dict: # here we have given a condition if. it checks if i is present in dictionary or not if it is present then add the count to +1
        Dict [i]+=1 # here If this condition satisfies then the in it will increase the count of value to +1
    else: # here I have use a else  condition if this condition satisfies the it means there is no same letter then it will add a new elment to the dictionary
        Dict [i]=1 #it is a new elment added to the dictionary
    print(Dict)
a={'b':1,'a':3,'n':2}
list=[]
for i in a:
    print(i,a[i])
    list.append(i*a[i])
print(list)
