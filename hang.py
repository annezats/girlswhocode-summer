from random import *
aRandomNumber = randint(0, 3)
listofwords = ["five", "girls", "not", "charms"]
word= [listofwords[aRandomNumber]] #picks a random word
dashes= [   ]
wrong= [ ]
waffles=0
#print(word)

for letter in word: #breaks word into letters
    for i in range(len(letter)): #makes i the number of letters
        dashes.append("_") #inserts a dash for each letter
    number= len(letter) #this is number of letters in word
i=0
while i < 7: #seven total tries
    print("you get seven mistakes. your current number of mistakes is:")
    print(i)
    print("Guess a letter")
    print(dashes)
    guess= input()
    for letter in word: #checks if letter is in the word
        if (guess not in letter):
            i+=1
            if i<7:#stops it from printing try again on last try
                print("no try again")
            print("here are your wrong letters:")
            wrong.append(guess)
            print(wrong)
        else:
            print ("yes u right")
            dashes.remove(dashes[letter.index(guess)]) #removes dash
            dashes.insert(letter.index(guess), guess) #puts in letter
    j=0 #this whole thing is the win condition
    while j < number:
        #print(j) #the index of the letter it is testing
        testletter= dashes[j]
        j+=1
        #print(testletter) #thE letter it is testing
        if not testletter.isalpha(): #if dash
            #print("dash")
            break
        elif (j == number): #if last letter
            print ("YOU WON")
            waffles = 5
    if waffles == 5:
        break
print("game over!")
