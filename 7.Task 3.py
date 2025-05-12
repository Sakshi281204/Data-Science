sentence1="i am piyush"
sentence2="hello" 
sentence3="what are you doing"
#task is to convert the fist letter of each sentence or the word in the upper case
space1=sentence1.find(" ") # here we have find a space from sentence1
word1=sentence1[0:space1]  #In this step we have seprated the words from each other etc.i
print(word1)                # in this line i have print the word 1 which is takent out from the sentence 1 which is i
space2=sentence1.find(" ",space1+1) #in this line i have found the second space from the sentence1 for thati have also added the name of first space which i have already found in the  spcae1 and +1 to tell the python that you have to find the second space
word2=sentence1[space1+1:space2]  # from this step i am  going to  repeat the procedure same as word 1
print(word2)
word3=sentence1[space2+1: ]
print(word3)
word1=word1[0].upper()+word1[1: ]
print(word1)
word2=word2[0].upper()+word2[1: ]
print(word2)
word3=word3[0].upper()+word3[1: ]
print(word3)
sentence1=word1+" "+word2+" "+word3+" "
print(sentence1)
sentence2 = "hello"
sentence2_op=sentence2.capitalize() #  capitalze function is use to capital the first number of the string
print(sentence2_op)
sentence3="what are you doing"
sentence3=sentence3.title()   # title function is used to capitalize all the worrds in the string
print(sentence3)