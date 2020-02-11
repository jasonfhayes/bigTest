# Dice - count totals in user-defined number of rounds

import random

class Bin():
    def __init__(self, binIdentifier):
        # This is called whenever you create a Bin object
        pass

    def reset(self):
        # This is called when you start or restart
        pass

    def increment(self):
        # Called when the roll total is the value of the binIdentifier
        pass

    def show(self, nRoundsDone):
        # Called at the end to show the contents of this bin
        pass


# Build a list of Bin objects            
binList = [ ]
# Here, you need to write a loop that runs 13 times (0 to 12)
    # In the loop create a Bin object, and store the object in the list
    # (We won't use bin[0] or bin[1])

    
while True:
    nRounds = input('How many rounds do you want to do? (or Enter to exit): ')
    if nRounds == '':
        break
    nRounds = int(nRounds)

    # Tell each bin to reset itself, and passin the number of rounds to do
    for bin in binList:
        bin.reset()
        
    # For each round (build a loop):
    #     roll two dice
    #     calculate the total
    #     and tell the appropriate bin to increment itself


    print()
    print('After', nRounds, 'rounds:')
    # Tell each bin to show itself
    for bin in binList:
        bin.show(nRounds)
    print()

print('OK bye')
