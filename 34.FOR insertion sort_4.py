# list=[5,3,0,1,2]
# a=len(list)
# for i in range(1,a):
# Define the list
# my_list = [5, 3, 0, 1, 2]
# for i in range(1, len(my_list)):
#     key = my_list[i]
#     pos = i
#     for j in range(i-1, -1, -1):
#         if my_list[j] > key:
#             my_list[j + 1] = my_list[j]
#             pos = j
#         else:
#             break
#     my_list[pos] = key
#print("Sorted list:", my_list)
# a=[5,3,0,1,2]
# store=a[0]
# a[0]=a[2]
# a[2]=store
# print(a)
a=[5,3,0,1,2]
for i in range (len(a)):
    mvi=i
    for j in range(i+1,len(a)):
        if a[mvi]>=a[j]:
            mvi=j
    store=a[mvi]
    a[mvi]=a[i]
    a[i]=store
    print("Sorted List: ",a)