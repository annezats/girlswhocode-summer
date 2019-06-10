# --- Define your functions below! ---
def starting():
    print("Greetings!I am a chatbot")
def processinpt(answer):
    if (answer == "hi" or answer == "hello"):
        print("hello to you too")
        name()
    else:
        print("That's cool!")
        name()
def name():
    askname= input("what's your name?  ")
    print ("wow, " + askname + ", thats a beautiful name!")
    joke(askname)

def joke(askname):
    print("hey, " + askname + ", do you want to hear a joke?yes or no")
    ansjk = input()
    if (ansjk == "yes"):
        print ("I hired a rabid dog as my tech support but i had to fire him because he took too many bytes :D")
    else:
        print("aw ok")
        main()
# --- Put your main program below! ---
def main():
    starting()
    while True:
      answer = input("(Please talk to me.) ")
      processinpt(answer)



#??
# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
