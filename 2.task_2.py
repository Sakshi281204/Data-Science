string2 = "P. R. Dhyani"
print(string2)
first_space_index = string2.find(" ")
print(first_space_index)
first_name = string2[0:first_space_index]
print(first_name)
trim_str = string2.strip(first_name + " ")
print(trim_str)
second_space_index = trim_str.find(" ")
print(second_space_index)
middle_name = trim_str[0:second_space_index]
print(middle_name)
trim_str2 = trim_str.strip(middle_name + " ")
print(trim_str2)