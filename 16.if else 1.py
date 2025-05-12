age=input("Enter your Age:")
age=int(age)
if age<0:
    print("you are not born yet")
elif age>=110:
     print("rest in piece")
elif 18<age<=18:
    print("you cannot drive")
# elif age>18:
#     print("you are Eligible to drive and apply for license")
elif type(age)==type(str):
    print("This is string ,please enter the no")

if age>18 and age<110:
    print("you can move forward")

    license_type=input("Enter the license type:")
    print(license_type)
    license_type_list = ['none','learning','educated']
    if license_type_list[0]==license_type and age>18:
        print("you can't apply")
    elif license_type_list[1]==license_type and age>18:
        print("hope you get your license")
    elif license_type_list[2]==license and age>18:
        print("Don't drink drive")