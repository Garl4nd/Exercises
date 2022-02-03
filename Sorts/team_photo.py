import itertools as it
def photographable(team1,team2):
    sorted_players=sorted((height,team) for height,team in it.chain(zip(team1,[1]*len(team1)),zip(team2,[2]*len(team2)))) 
    left=0
    trial_teams=1,2
    for trial_team in trial_teams:
        for height, team in sorted_players:
            if team==trial_team:
                left+=1
            else:
                left-=1
            if left<0:
                break
        else:
            return True,trial_team
    return False,0

def photographable2(team1,team2):
    sorted_teams=sorted(team1),sorted(team2)
    res=all(player1<player2 for player1,player2 in zip(*sorted_teams))
    if res:
        return True,1
    

    res=all(player2<player1 for player1,player2 in zip(*sorted_teams))
    if res:
        return True,2
    
    return False,0


print(photographable2([150,160,190],[170,190,200]))