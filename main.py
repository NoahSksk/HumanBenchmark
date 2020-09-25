# _________________________________________________
#|                                                 |
#|    Projet NSI : MAXIME BECK ; NOAH GOSCINIAK    |
#|_________________________________________________|
#

from player import *
from score import *
from reactionTime import *

p1 = Player("Max")
p2 = Player("Noah")
p3 = Player("Luc")



rtMax = ReactionTime(p1)
rtMax.game()
maxScore = Score(p1)
maxScore.upElo(rtMax.score)
maxScore.setName()
maxScore.writeScore("Reaction Time",rtMax.score)

rtNoah = ReactionTime(p2)
rtNoah.game()
noahScore = Score(p2)
noahScore.upElo(rtNoah.score)
noahScore.setName()
noahScore.writeScore("Reaction Time",rtNoah.score)

rt2Noah = ReactionTime(p2)
rt2Noah.game()
noahScore.writeScore("Test",rt2Noah.score)
