#task 2
string="Piyush Ramkumar Dhyani"
print(string)
first_name_index=string.find(" ")
print(first_name_index)
first_name=string[0:first_name_index]
print(first_name)
trim_str=string.strip(first_name+" ")
print(trim_str)
second_name_index=trim_str.find(" ")
print(second_name_index)
second_name=trim_str[0:second_name_index]
print(second_name)
trim_str2=trim_str.strip(second_name+" ")
print(trim_str2)
third_name_index=trim_str2.find(" ")
print(third_name_index)
third_name=trim_str2[0:third_name_index]
print(third_name)
trim_str3=trim_str2.strip(third_name+" ")
