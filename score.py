import os
import player
os.chdir("./score/")
class Score:
    def __init__(self,player):
        self.player = player
        self.elo = 0

    def upElo(self,amount):
        self.elo += amount

    def downElo(self,amount):
        self.elo -= amount
    
    def changeElo(self,amount):
        self.elo = amount

    def writeScore(self,game,score):
        fic = open(f"{self.player.display()} score.txt","a")
        fic.write("\n")
        fic.write(str(game) + " : " + str(score))
        fic.write("\n")
        fic.close()

    def setName(self):
        fic = open(f"{self.player.display()} score.txt","a")
        fic.write(str(self.player.display()))
