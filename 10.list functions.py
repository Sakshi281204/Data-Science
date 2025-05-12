#Examples of list functions
#append()
thislist=["apple", "banana","cherry"]
thislist.append("orange")
print(thislist)
print(len(thislist))
print(type(thislist))
thislist.insert(2,"watermelon")
print(thislist)
tropical=["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)
thislist.remove("banana")
print(thislist)

thislist.pop()
print(thislist)

thislist.sort()

print(thislist)
mylist=thislist.copy()
print(mylist)

x=thislist.count("mango")
print(x)

thislist.clear()
print(thislist)