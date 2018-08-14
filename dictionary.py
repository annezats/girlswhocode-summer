#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
password = input("Type in a trial password: ")

#Write logic to see if the password is in the dictionary file below here:
secure= False
for line in f:
    if line.strip() == password:
        secure= False
        break
    else:
        secure = True
        continue

if secure == False:
    print("nope thats bad")
if secure == True:
    #for letter in password:
        #if number
            #then good and break
        #else
            #print("You dont have any numbers")
    #NOTE PERHAPS better to first check for a number then the word?

    print("u good")
