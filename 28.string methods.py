string="Piyush Dhyani piyush@gmail.com"
# str1="Ram Patil ram1223@heuristic.com"
# sp=string.find(" ")
# print(sp)
# print(string[0:sp])
# name=string[0:sp]
# print(name)
# at=string.strip(name+" ")
# print(at)
# pm=string.find(at)
# print(pm)

name_index=string.find(" ")
print(name_index)
name=string[0:name_index]
print(name)
trim_str=string.strip(name+" ")
print(trim_str)
surname_index=trim_str.find(" ")
print(surname_index)
surname=trim_str[0:surname_index]
print(surname)
email_index=trim_str.strip(surname+" ")
print(email_index)