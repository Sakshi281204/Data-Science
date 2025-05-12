fullname="Rahul Patiz"
fullname2="Sai jadhav"
index1=fullname.find(" ")
print(index1)
firstname=fullname[0:index1]
print(firstname)
last_name=fullname.strip(firstname+" ")
print(last_name)
length=len(fullname)
print(length)
print(firstname,last_name)
firstname=firstname.lower()
print(firstname)
last_name=last_name.lower()
print(last_name)
print(last_name+firstname+str(length) + "@gmail.com")
Gmail=last_name.lower()+firstname.lower()+str(len(fullname))+"@gmail.com"
print(Gmail)