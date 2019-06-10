numbers = [1, 5, 345, 713]
friends = ["isabelle", "glen", "Nancy", "benji"]
things_in_nyc = [5, "apple", 'goldman Sachs', "people", 27.3
]
print(friends) #prints whole list
print(numbers[3]) #prints fourth item
print("glen" in friends) #prints true
print("7" in "713") # true

for person in friends:#prints whole list one at a time
    print(person)

word= "magic"
if ("m" in word):
    print("yes")
else:
    print("no")

print(len(friends))
#prints 4

for i in range(len(friends)): #prints friends
    print(friends[i])

for i in range(1): #prints 1
    print(numbers[i])

lists = [friends, numbers, things_in_nyc]
for item in lists:
    print(item) #lists the lists
