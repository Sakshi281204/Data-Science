a=int(input("enter the no:"))
# b=int(input("enter the no:"))
# c=a/b
# print(c)

# try:
#     a=int(input("enter the no:"))
#     b=int(input("enter the no:"))
#     c=a/b
#     print(c)
#     if b==0 or b==4 or b==7:
#         raise ValueError
#     else:
#         print(a/b)

#except ZeroDivisionError:
#     print("Number can't  divided by 0")
# finally:
#     print("Thank you")

# try:
#     a=int(input("enter the no:"))
#     b=int(input("enter the no:"))
#     c=a/b
#     print(c)
#     if b==0 or b==4 or b==7:
#         raise ValueError
#     else:
#         print(a/b)

# except ValueError:
#     print(f'[b] is not allowed')
# finally:
#     print("Thank you")


try:
    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    #c=a/b
    #print(c)
    if b==0 or b==4 or b==7:
        raise ValueError(" 7, 4, and 0 are Invalid Numbers")
    else:
        print(a/b)

except ValueError as e:
    print("error",e)
finally:
    print("Thank you")