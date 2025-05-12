list=[5,3,0,1,2]
for i in list:
    list[0:len(list)]
    for j in list:
        if i==j+1:
            print(list)
        else i!=j+1:
            print(list)