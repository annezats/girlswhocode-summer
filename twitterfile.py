import json
tweetfile= open("twitter.json", "r")
tweetdata= json.load(tweetfile)
tweetfile.close()
print(tweetdata[0]["text"])

#print text of first tweetdec
for tweet in tweetdata:
    print("text id: ", tweet["text"])
