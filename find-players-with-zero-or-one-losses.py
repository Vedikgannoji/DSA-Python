#2225 find-players-with-zero-or-one-losses
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
def findWinnersAndLosers(matches):
    freq_loosers={}
    players=set()
    answer=[[],[]]
    for winner, looser in matches:
        players.add(winner)
        players.add(looser)
        freq_loosers[looser]=freq_loosers.get(looser,0)+1
    for player in players:
        if player not in freq_loosers:
            answer[0].append(player)
    for k,v in freq_loosers.items():
        if v==1:
            answer[1].append(k)

    # freq_winners={}
    # for i in matches:
    #     freq_loosers[i[1]]=freq_loosers.get(i[1],0)+1
    # for i in matches:
    #         freq_winners[i[0]]=freq_winners.get(i[0],0)+1
    # for k in freq_winners.keys():
    #      if k not in freq_loosers.keys():
    #           answer[0].append(k)
    # for k,v in freq_loosers.items():
    #     if v==1:
    #         answer[1].append(k)

    answer[0].sort()
    answer[1].sort()
    return answer
print(findWinnersAndLosers(matches))
    