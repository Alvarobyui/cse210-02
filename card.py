import random

class Card:
    """A playing card that displays numbers.
    The responsibility of playing cards is to display numbers and judge if it is high or not.
    Track the point according to the guessing.

    Attributes:
        value (int): the number to the flip the card.
        points (int): the numbers of point earned if the user guess
    """
def __init__(self):
    """Constructs a new instance of playing cards with a value and points attribute.

    Args:
        self (card): An instance of playing card.
    """
    self.value = 0
    self.points =0

def flip(self):
    """Display the random numbers for gamer can guess the next card
        
    Args:
        self(card): An instance of card
    """
    self.value = random.randint(1,13)
    
            
            
            

    

        
