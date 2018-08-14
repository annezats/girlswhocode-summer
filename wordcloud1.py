import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import numpy
from wordcloud import WordCloud #NOT WORKING AAAAA

#Get the JSON data
tweetFile = open("twitter.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!
listpol= []#lsit of polarities
listsub= []
listtweet=[]#list of all the tweet words
# Textblob sample:
for tweet in tweetData:
    texttweet= (tweet ["text"])#makes the text of a tweet the variable
    tb = TextBlob(texttweet)#makes it a textblob
    #print(tb.polarity)
    listpol.append(tb.polarity)#puts polarities ina  list
    listsub.append(tb.subjectivity)
    listtweet.append(texttweet)#puts all texts in a list
print("avg polarity:  ",numpy.mean(listpol))
print("avg subjectivity:  ",numpy.mean(listsub))

#plt.hist(listpol, bins=[-1,0,1])
#plt.xticks([-1,0,1])
plt.hist(listpol, color= "green", bins=[-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])
plt.xticks([-1,-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1])#changes the label
plt.show()

plt.hist(listsub, color= "blue", bins=[0,0.2,0.4,0.6,0.8,1])
plt.xticks([0,0.2,0.4,0.6,0.8,1])#changes the label
plt.show()





waffles= ' '.join(listtweet)#makes list of tweets one string
wordblob=TextBlob(waffles)
filteredwords = ["if", "and", "or", "automation"]
diction= { }
#word_list = waffles.split()#makes it a list
filter1= False
for word in wordblob.words:
    for badword in filteredwords:
        if (word == badword):
            filter= True
            break
        else:
            filter= False
    if filter == False:# if the word is not a filtered word
#        for key in diction:
#            if (word == key):
#                filter1 = True
#                break
#            else:
#                filter1 = False
#        if (filter1 == True): #    NOT WORKING AAA
#            diction[word] +=1
#        else:
        diction[word]= 0
#print(diction)


diction[word.lower()]= wordblob.word_counts[word.lower()]
wordcloud= WordCloud().generate_from_frequencies(diction)
plt.imshow(wordcloud)
plt.show()
