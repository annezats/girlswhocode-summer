import skyscrapers
from textblob import TextBlob
import matplotlib.pyplot as plt
sky = skyscrapers.get_skyscrapers()
from wordcloud import WordCloud
from PIL import Image


rep = ["steel/concrete", "concrete/steel"]
list = ["steel", "concrete", "composite", "masonry", "precast"] #"SteelConcrete"
sort= {
    "steel" : " ",
    #"SteelConcrete": " ",
    "composite": " ",
    "concrete": " ",
    "masonry": " ",
    "precast": " "
}
count={
    "steel" : " ",
    #"SteelConcrete": " ",
    "composite": " ",
    "concrete": " ",
    "masonry": " ",
    "precast": " "
}


for item in list:
    for building in sky:
        loc = building["location"]["city"]
        location = loc.replace(" ", "")
        material = building["material"]
        if item == material:
            if location == "NewYorkCity":
                sort[item] = sort[item] + " NYC"
            else:
                sort[item] = sort[item] + " " + location

    '''    if material in rep:
            if location == "NewYorkCity":
                sort["SteelConcrete"] = sort["SteelConcrete"] + " NYC"
            else:
                sort["SteelConcrete"] = sort["SteelConcrete"] + " " + location'''
    steelcloud = WordCloud(width = 1000, height = 500).generate(sort[item])

    plt.figure(figsize=(15,8))
    plt.imshow(steelcloud)
    plt.axis("off")
    plt.savefig(item+".png", bbox_inches='tight')
    plt.close()
    img=Image.open(item + ".png")
    img.show()

    anotherheckinlist= []
    wordstring=sort[item]
    wordlist=wordstring.split()
    wordfreq=[]
    for w in wordlist:
        wordfreq.append(wordlist.count(w))
    for i in range(len(wordlist)):
        anothervariable= wordlist[i], wordfreq[i]
        if anothervariable not in anotherheckinlist:
            anotherheckinlist.append(anothervariable)
    print(item)
    print(anotherheckinlist)
