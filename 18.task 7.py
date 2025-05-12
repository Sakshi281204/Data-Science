elements=input("Enter number of Elements:-") #Take number of elements from the user
a=input("Enter Element number 1:-") #we have to take 5 inputs from the user so here are 5 inputs
b=input("Enter Element number 2:-")
c=input("Enter Element number 3:-")
d=input("Enter Element number 4:-")
e=input("Enter Element number 5:-")
Your_List=[] #here we have call a empty list in which we are going to add the elemets which are taken from the user
# Your_List.insert(0,a) #logic 1
# Your_List.insert(1,b)
# Your_List.insert(2,c)
# Your_List.insert(3,d)
# Your_List.insert(4,e)
str=(a+" "+b+" "+c+" "+d+" "+e) # Logic 2 in this we have added the lements which we are taken fron the user
Your_List=str.split() # Split function is used to add the elments in the list
print("Your_List_is:-",Your_List) # here we have printed our final list of elements