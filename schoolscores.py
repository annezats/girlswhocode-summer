import school_scores as scores
scorelist= scores.get_all()

#for i in range(len(scorelist)):
    #print(scorelist[i]['Year'])

for item in scorelist:#opens each thing
    state= item["State"]#opens state in thing
    statename= state["Name"]#opens name in state
    year= item["Year"]
    print(statename,", ", year)
