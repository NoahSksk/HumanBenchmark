from random import *
from time import *
import random

class ReactionTime:
    """ Constructeur """
    def __init__(self,player):
        self.player=player
        self.score=0

    def game(self):
        start = input("Press enter to start ") 
        sleep(randint(2,6))
        t1 = time()
        end = input("! Press !")
        t2 = time()
        t3 = round((t2-t1)*1000,1)
        print(f"Your reaction time is : {t3}ms")
        self.score=t3       
