#list=[1,2,3,4]
# a=len(list)
# print(a)                    

# def Len(num,num1,num2,num3):   
#     num.append(num1)
#     num.append(num2)             
#     num.append(num3)               

# Len(list,5,6,7)
# b=len(list)
# print(a,b)    
# *********************************************************                 

# Len=([1,2,3],"apple",[2,3],[7,3,3],"apple")
# def Len(*apple):
#     # a=[1,2]
#     result=[]
#     for i in apple:
#        if type (i)==type(result):
#           result.append(len(i))
#        else:
#           result.append(None)
#     return
#***************************************************************

# print(Len([1,2,3],"apple",[2,3],[7,3,3],"apple"))
# try:
#     a=[1,2,3]
#     b=[]
#     c=''
#     if type (a)==type(b) or type(a)==type(c):
#         def Reverse (paramters):
#             par=par.reverse()
#         Reverse(a)
#     else:
#         raise Exception("Only list and string datatype are allowed")
# except Exception as e:
#     print(e)

# #*REVERSE*******************
# try:
#     a=(1,2,3)
#     if isinstance(a,list) or isinstance(a,str):
#         def Reverse (par):
#             par=par.reverse()
#         Reverse(a)
#         print(a)
#     else:
#         raise Exception("Only list and string datatype are allowed")
# except Exception as e:
#     print(e)


    
# #***** EXTEND*****
# try:
#     a=[1,2,3]
#     b=[4,5,6]
#     def Extend(par1,par2):
#         if type (a)!= type(b):
#             raise Exception("Arguments have different datatype")
#         par1.extend(par2)
#     Extend(a,b)
#     print(a)
# except Exception as e:
#     print("Error",e)
# finally:
#   print("Thank youu")


# # # *****INDEX*****
# try:
#     a =[1,2,3,4]
#     b= "abcd"
#     if isinstance(a,(list,str)) or isinstance(b,(list,str)):
#         def Index(a):
#             return a.index(4)
#         result_list= Index(a)
#         def Index(b):
#             return b.index("c")
#         result_string= Index(b)
#         print("Index of list:", result_list)
#         print("Index of string:",result_string) 
#     else:
#         raise Exception("Only list and string datatype are allowed")
# except Exception as e:
#     print("Error:", e)
# finally:
#         print("thank you:")

#************* Other Logic*************************

try:
    a = [1,2,3,4]
    b = 3

    def Index(val1,val2):
        if isinstance(val1,str) and isinstance(val2,str)==False:
            raise Exception("string datatype can allow")
            
        if  isinstance(val1,list) :
            if not isinstance(val2,str) and not isinstance(val2,int):
                raise Exception("enter the value of 2 is str or int")
        return val1.index(val2)

    print(Index(a, b))

except Exception as e:
    print("Error", e)