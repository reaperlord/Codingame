import math
import numpy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class player:
    
    def __init__(self, numplayer, signplayer):
        self.number  = int(numplayer)
        self.sign = signplayer
        self.opponents = []

class tournament:

    def __init__(self, playerList, noOfPlayers):
        self.playerList = playerList
        self.noOfPlayers = int(noOfPlayers)
        self.winner = None

    @staticmethod
    def fight(player1:player, player2:player, winnersList:list, winnerIndx):        

        if tournament.evaluate(player1.sign, player2.sign): #if true player1 won
            winner, loser = player1 ,player2
        elif tournament.evaluate(player2.sign, player1.sign): #if true player2 won
            winner, loser = player2 ,player1
        else: #its a draw, therefore evaluate number
            if player1.number < player2.number: #player1 won
                winner, loser = player1, player2
            else: #player2 won
               winner, loser = player2 ,player1 

        winner.opponents.append(loser)
        winnersList[winnerIndx]=winner

    @staticmethod
    def evaluate(sign1, sign2):
        if sign1 == "C": #scissor
            if sign2 == "P" or sign2 == "L": #scissor cuts paper and lizard
                return True
            else: return False
        elif sign1 == "R": #rock
            if sign2 == "C" or sign2 == "L": #rock crushes scissor and lizard
                return True
            else: return False
        elif sign1 == "P": #paper
            if sign2 == "R" or sign2 == "S": #paper kills rock or spock
                return True
            else: return False
        elif sign1 == "L": #lizard
            if sign2 == "P" or sign2 == "S": #lizard eats paper or spock
                return True
            else: return False
        elif sign1 == "S": #spock
            if sign2 == "R" or sign2 == "C": #spock destroys rock or scissors
                return True
            else: return False


    def playARound(self):
        winnersList = numpy.empty( int(self.noOfPlayers/2), player )
        winnerIndx = 0
        for i in range(0,len(self.playerList),2):
            self.fight(self.playerList[i], self.playerList[i+1], winnersList, winnerIndx)
            winnerIndx += 1

        self.playerList = winnersList #at end of round winnersList becomes new playerList
            
    def playTournament(self):
        while self.noOfPlayers > 1:
            self.playARound()
            self.noOfPlayers /= 2

        self.winner = self.playerList[0]


n = int(input())
t = tournament( numpy.empty(n, player), n)

for i in range(n):
    numplayer, signplayer = input().split()
    t.playerList[i] = player(numplayer, signplayer)

t.playTournament()

print(t.winner.number)
print(" ".join([str(o.number) for o in t.winner.opponents]))