a = "banana" # We have taken a string here 
letter_count = {} # in this variable we have declare a empty list in which we are going to get a letter and number of repetition 
for letter in a: #here i have taken a for loop in the place of i letter variable is taken which will go through the string
    if letter in letter_count:  # here if letter is already in the dictionary it will increase the count by 1
        letter_count[letter] += 1 # here the candion will increasing count by +1
    else:    # else condtion is applied
        letter_count[letter] = 1 #if the letter i not present in the dictionry it will add the letter in dictionary and give the count 1
    print(letter_count) #here it will print dictionary


list=[] # now we have taken a empty list in which we have to add the elments in the dictionary
for i in letter_count: #in this line we will go throgh all the elemnts in the dictionary
    print(i,letter_count[i]) # here we will print key and value with each other
    list.append(i*letter_count[i])# in this line key and value pair are get multiplied from this we will gwt a string
print(list)#printing the finaal list with number od timeds key is repeating


a=list # in this line we have taken a input as a list which we have to sort
for i in range(len(a)):#in this for will go through all the elements in the  list
    mvi=i #here we have inimum value index as i as the i changes mvi also going to change
    for j in range(i+1,len(a)): #here is a for loop which will go through the list again by comparing the value of i
        if len(a[mvi])>=len(a[j]): #in this line we have compared the length of the string which is present in the list
            mvi=j #here we have stored the value of the minimum value index j if we are getting miminum value it is getting stored in j
    temp=a[mvi] #from this line the swapping is taking palce which value we have to swap we are storing it into the  temp variable 
    a[mvi]=a[i] #now we have changed the value minimum value will go to the value of i and and greater value will go forward at the place of minimum value 
    a[i]=temp # in this line we will change the greater value with the value which is stored in  temporary  variable
    print("Sorted List:",a) # in this line we are printing the sorted list