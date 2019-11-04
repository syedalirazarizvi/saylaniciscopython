#PROGRAM FOR REVERSING THE INPUT TEXT

print("""Hello,
    You know what\'s wrong with me?
    I actually see everything in REVERSE.
            """)

userInputFirst=input("Don\'t believe? Let me have your first name? ")
userInputSecond=input("Now enter your last name please? ")

userFullName = userInputFirst + " " + userInputSecond # Producing full name with space

#print(userFullName)

stringlength=len(userFullName) # calculate length of the list
slicedString=userFullName[stringlength::-1] # slicing 
print (slicedString) # print the reversed string
