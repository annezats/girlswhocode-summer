# Some useful variables
maxfails = 7

from random import *
aRandomNumber = randint(0, 3)
listofwords = ["five", "girls", "program", "charm"]
word= [listofwords[aRandomNumber]] #picks a random word
dashes= [   ]
wrong= [ ]

print(word)

for letter in word: #breaks word into letters
    for i in range(len(letter)): #makes i the number of letters
        dashes.append("_") #inserts a dash for each letter

i=0
while i<8:
    i+=1
    print("you have seven tries. your current try number is:")
    print(i+1)

    print("Guess a letter")
    print(dashes)
    guess= input()

    for letter in word: #checks if letter is in the word
        if (guess in letter):
	    i-=1
            print ("yes u right")
            dashes.remove(dashes[letter.index(guess)]) #removes dash
            dashes.insert(letter.index(guess), guess) #puts in letter

        else:
            print("no try again")
            print("here are your wrong letters:")
            wrong.append(guess)
            print(wrong)

print("Sorry, game over!")


