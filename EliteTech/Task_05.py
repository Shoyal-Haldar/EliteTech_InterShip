    #  Dice Roll Simulator
from random import randint
def DiceRollSim():
        dice_roll = randint(1,6)
        return dice_roll
        
chance = int(input("\nTo Roll the Dice enter 1 , to exit enter 0: "))
while chance:
    print("\n\tYour roll Value is ",DiceRollSim())
    chance = int(input("\nTo Roll again enter 1 , to exit enter 0: "))
else:
    print("End")