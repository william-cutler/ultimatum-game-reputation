
#A strategy is one of:
hawk = "H"
dove = "D"
#and represents a strategy in extended form Hawk-Dove

# A Payoff is a List[Number, Number]
# and represents the payoffs to Player1 and Player2
h_h = [0,0]
h_d = [4, 1]
d_h = [1, 4]
d_d = [2, 2]

# A StrategySet is a List[Strategy, Strategy, Strategy]
# And represents the strategy if Player 1, strategy if P1 plays Hawk, and if P1 plays Dove
HHH = [hawk, hawk, hawk]
HHD = [hawk, hawk, dove]
HDH = [hawk, dove, hawk]
HDD = [hawk, dove, dove]
DHH = [dove, hawk, hawk]
DHD = [dove, hawk, dove]
DDH = [dove, dove, hawk]
DDD = [dove, dove, dove]

ALL = [HHH, HHD, HDH, HDD, DHH, DHD, DDH, DDD]

#cross_play : -> List[List[Number, Number]]
#creates list of list of all possible play combination payoffs

def cross_play():
    out = []
    for strat1 in ALL:
        for strat2 in ALL:
            out.append(play_game(strat1, strat2))
    return out;

# play_game : StrategySet, StrategySet -> List[Number, Number]
# Returns the average utility gained by each player

def play_game(ss1, ss2):
    if ss1[0] == hawk:
        if ss2[1] == hawk:
            g1 = h_h
        else:
            g1 = h_d
    else:
        if ss2[2] == hawk:
            g1 = d_h
        else:
            g1 = d_d
    if ss2[0] == hawk:
        if ss1[1] == hawk:
            g2 = h_h
        else:
            g2 = d_h
    else:
        if ss1[2] == hawk:
            g2 = h_d
        else:
            g2 = d_d
    return [(g1[0] + g2[0])/2, (g1[1] + g2[1])/2];

# formidable : StrategySet StrategySet -> Boolean
# Determines if the first strategy can resist invasion by the second

def formidable(ss1, ss2):
    if (play_game(ss1, ss1)[0] > play_game(ss1, ss2)[1]):
        return True;
    elif (play_game(ss1, ss1)[0] == play_game(ss1, ss2)[1]) and (play_game(ss1, ss2)[0] > play_game(ss2, ss2)[0]):
        return True;
    else:
        return False;

# ess : List[StrategySet ...] -> Display Output
# Determines which strategies are ESS in the list

def ess(loss):
    out = []
    for i in range(len(loss)):
        ess = True
        for j in range(0, i):
            if not(formidable(loss[i], loss[j])):
                ess = False;
        for j in range(i+1, len(loss)):
            if not(formidable(loss[i], loss[j])):
                ess = False;
        out.append(ess)
    return out;
