#Filename: Shah_Valay_QuizNum3.py
#Author: Valay Shah
#Date Created: December 1, 2019
#Description: The program asks for the user's first and last name and outputs
#the number of letters in the full name as well as what letters it begins and 
#ends with along with what the initials are.

#Header Output
print ("X*75")
print ("Filename: Shah_Valay_QuizNum1.py")
print ("Author: Valay Shah")
print ("Date Created: December 1, 2011")
print ("""Description: The program asks for the user's first and last name and 
outputs the number of letters in the full name as well as what letters it begins 
and ends with along with what the initials are.""")
print ("X*75")

#Input:
firstname = input("What is your first name?")
lastname = input ("What is your last name?")

#Processing
fullname = firstname+lastname
letter = len(fullname)
first = fullname[0]
last = fullname[-1]
initial = firstname[0]
initial2 = lastname[0]

#Output
print (fullname,", your name is ", letter, "letters long.\n","The first letter is" ,)
print (first, ", and the last letter is ",last,".\n Your initials are, ",initial,)
print (initial2, ".")
