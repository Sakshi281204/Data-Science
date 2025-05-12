a=input("Enter the letter type:-") # taken input from the uswr if he want formal or informal letter
letter_type=["formal","Informal"] # here we have given a list of letter from which user will choose
if letter_type[0]==a: # here we have used a if fuction to compare user input and our list
    print("Proceed to Write Formal Letter;") #in this line we have checked he input and tell the useer that now you can proceed
    name=input("What is your First name:- ") #now in some line below we are taking inputs from the user for example nam and etc.
    mname=input("Your middle name:-")
    lname=input("Your last Name:-")
    subject=input("Add Your Subject here:- ")
    to_whom=input("name of The Person You want To Send application:-")
    reciever=input("Respected Principle,")
    body=input("Body Of the application:-")
    format=["Justify","Non justified"] # in this line we have give a list and given options like justified or non justified 
    format_input=input("If you want Justified or not Justified:-")# in this line we have ask user waht kind of format he want
    print("This Is Your Application") # form this we are started to rpinting the application by useing the user input and we haave also provided the some our tesxts  
    print("To") # this is the line which he dont want to write it will bw already there in the formaat of the fomal letter
    print("The Respected ,")
    print(reciever) # here we are printing the inputs of the user
    print(to_whom)
    print(reciever)
    print("Subject:- ",subject)
    print("Respected Principle,")
    if format[0]==format_input: # here we are excuting the code as per the user input  if user input is justified the this code will execute
        half_index=body.find(" ",len(body)//2)  # in this logic we have teken half index by measunring length of the body we have cutted body in two parts
        first_half=body[:half_index] # in ths we are saving value of first half until we find the half index
        second_half=body[half_index+1:] # in this it will save next remaninng part of the body
        print(first_half) 
        print(second_half)
    elif format[1]==format_input: # if user chooses no to format the give body will be printed as it is
        print(body)
    print("Your's Faithfully,")
    print("Name Of applicant:",lname+" "+name+" "+mname) # here we are add full name of the user
    print("Thank You......")

elif letter_type[1]==a: #  Now if user chooses the second letter type which is informal code will be excuted from this line
    print("Proceed to Write A informal letter;") # here we have tell user that you start writing your informal letter
    name=input("Enter your name:-") # from this line we are stated to taking inputs from the user
    address=input("Enter Your Address:-")
    city=input("Enter name of your City:-")
    state=input("Enter name of your State:-")
    pincode=input("Enter your pincode:-")
    date=input("Write A date you are writing this letter on:-")
    greeting=input("Write a greetings You want to give:-")
    body=input('Wrie A body of the letter:-')
    format=["Justify","Non justified"] #here we have give list of format of the bodt if formatted or not formatted
    format_input=input("If you want Justified or not Justified:-") # in this we have ask user the choce by using which we will execute our code
    print(name) # from this line we are started printing infomel letter for the user
    print(address)
    print(city+" "+state+" "+pincode)
    print(date)
    print("To My Dear")
    print(greeting)
    if format[0]==format_input: #if user want formatiing in their letter this code will be excuted 
        half_index=body.find(" ",len(body)//2)
        first_half=body[:half_index]
        second_half=body[half_index+1:]
        print(first_half)
        print(second_half)
    elif format[1]==format_input: # if user dont want formatting in teir letter this code will execuet
        print(body)
    print(first_half)
    print(second_half)
    print("Lots of Love")
    print("Take Care")
    print("see you soon")
    print(name)