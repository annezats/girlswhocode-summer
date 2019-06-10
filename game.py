# Update this text to match your story.
start = '''
You are walking down main street of magicville, and see a fairy in distress. Do you go up to her? '''

while True:
    print(start)
    print("Type yes or no to answer")
    user_input = input()
    if user_input == "no":#restart sequence
        print("Well, there's nothing else to do in magicville today, let's see what tomororw brings. do you want to play again/")
        while True:
            user_input= input()
            if user_input ==("no" or "yes"): #if no or if yes, then break
                break
            else:
                print("whoops that's not a yes or no")
                continue
        if user_input == "no":
            print ("game over")
            break
        elif user_input == "yes":
            print ("okay, restarting")
            continue
    elif user_input == "yes": #to continue the game
        print("You walk up to the fairy and she tells you about her missing pet. Do you help find it?")
        user_input= input()
        if user_input == "no":
            print("Well, there's nothing else to do in magicville today, let's see what tomororw brings. do you want to play again?")
            while True:
                user_input= input()
                if user_input ==("no" or "yes"): #if no or if yes, then break
                    break
                else:
                    print("whoops that's not a yes or no")
                    continue
            if user_input == "no":
                print ("game over")
                break
            elif user_input == "yes":
                print ("okay, restarting")
                continue #restart sequence
        elif user_input == "yes":
            print ("congrats youre a good person")
            break
    else: #for the first question of the game
        print("whoops that's not a yes or no")
        continue
    # Continue code to finish story.


while True: #basic loop
    user_input= input()
    if user_input == "no":
        print ("game over")

    elif user_input == "yes":
        print ("moving on")
    else:
        print("whoops that's not a yes or no")
        continue
