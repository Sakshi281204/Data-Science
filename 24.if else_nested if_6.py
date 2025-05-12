a=input("Enter The Letter Type:")
letter_type=["formal","informal"]
if letter_type[0]==a:
    print("Processed for formaal letter:")
    c= input("Enter Your first Name:" ) 
    d = input("Enter Your Middle Name:")                          
    e = input("Enter Your Last Name:") 
    name = c+" "+d+" "+e

    print("Welcome to the application")

    f = input("To\n Respected sir")   
    print(f)
    print("S.G.BAGUL\n Head Of Deartment\n")                                  
    g = input("subject:")    
    print(g,"Application for bonafite Certficate")                                                               
    h = input()
    p=input("Enter Your Formating Type:")
    format_list=["justify","nonjustify"]
    str="Respected sir,\nI request bonafite for ooficail use plz approve my request give me bonfite as soon as possible  "
    if format_list[0]==p:
        print(str)     
        half_index= str.find(" ",len(str)//2)
        first_half= str[:half_index]
        second_half=str[half_index+1:]
        print(first_half)
        print(second_half)  
    elif format_list[1]==p:
        print(str)                                                            
    i= input("thank you,") 
    print(i,name) 

elif letter_type[1]==a:                                     
    print("processed for informal letter:\n""Welcome to application")     # Ask the format of letter and give the msg welcome to application          
    j=input("Enter Your Name:")                                           # take input (name, address, city,pincode,date)                                        
    k=input("Enter Your Address:")
    l=input("Enter Your City:")
    m=input("Enter Your Pincode:")
    n=input("Enter The Date:")
    greeting=input("Enter You Grreting You Want To Write:")             # write the greeting as per chioce
    body=input("As Per Subject Enter The Body")                         # write the subject as per subject
    print(j)                                                            # then print input as per format
    print(k)
    print(l+" "+m)
    print(n)
    print(greeting,)
    p=input("Enter your formating type:")                              # Ask the formating type means justify or nonjustify 
    format_list=["justify","nonjustify"]                               # As per choice select any one condition
    if format_list[0]==p:                                              #according to that condtion are satisfied
        print(body)                                                    # select the if condtion justify the content trim the body in equal parts  
        half_index= body.find(" ",len(body)//2)                        #in else part not trim the body print as it is without any formating
        first_half= body[:half_index]
        second_half=body[half_index+1:]
        print(first_half)
        print(second_half)  
    elif format_list[1]==p:
         print(body)    
    print("Take Care,\n bye...")
    print(j)