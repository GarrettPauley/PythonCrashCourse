from random import randint

class Die: 

    def __init__(self, num_sides = 6): 
        """Initialize a 6 sided die"""
        self.num_sides = num_sides

    
    def roll(self): 
        """Return a random number between 1, and the number of sides (default of 6)"""
        return randint(1, self.num_sides)