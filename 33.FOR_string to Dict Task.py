a = "banana" # this is a string 
Dict = {} # I have taken a empty dictionary here in which i have to add the elments
for i in a: #here I have taken a for loop in which i eill check 'i' in string 'a'= "banana"
    if i in Dict: # here we have given a condition if. it checks if i is present in dictionary or not if it is present then add the count to +1
        Dict [i]+=1 # here If this condition satisfies then the in it will increase the count of value to +1
    else: # here I have use a else  condition if this condition satisfies the it means there is no same letter then it will add a new elment to the dictionary
        Dict [i]=1 #it is a new elment added to the dictionary
    print(Dict)
# a={'b':1,'a':3,'n':2}
list=[]
for i in Dict:
    print(i,Dict[i])
    list.append(i*Dict[i])
print(list)

list=[]
for i in Dict:
    print(i,Dict[i])
print(list)
# list=["b",'aaa','nn']
for i in range (len(list)):
    mvi=i
    for j in range(i+1,len(list)):
        if len(list[mvi])>=len(list[j]):
            mvi=j
    store=list[mvi]
    list[mvi]=list[i]
    list[i]=store
    print("Sorted List:",list)
    
