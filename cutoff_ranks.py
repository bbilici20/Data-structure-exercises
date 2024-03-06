def countLevelUpPlayers(cutOffRank, num, scores):
    meximum=max(scores)
    ranks=[0]*(meximum+1)
    for score in scores:
        ranks[meximum-score]+=1
    count=0
    counter=1
    for ranik in ranks:
        if counter<=cutOffRank and ranik!=0:
            count+=ranik
            counter+=ranik
    return count
