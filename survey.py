import json
list= []
responses= ["name","age" ]
questions= ["What is your name?", "how old r u"]

while True:
    survey={}
    for i in range(len(questions)):
        survey[responses[i]]= input(questions[i])
    list.append(survey)
    ask = input("do you wanna play again?")
    if (ask == "no"):
        print("boo!")
        break
    if (ask == "yes"):
        print("kay!")
        continue

listToJSON = json.dumps(list)#not in amelias code
print(listToJSON)
file=open("dictionary.json","r")
olddata = json.load(file)
list.extend(olddata)
file.close()

file = open("dictionary.json","w")
file.write(listToJSON)
file.close()
