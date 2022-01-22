from game.card import Card

import random

class Director:
    """A person who directs the game
    The responsibility is to be a referee and control the game.

    Attributes:
        card: A list of Card instances
        is_playing (boolean): If the gamer decides to continue or not
        score (int): The score earn
        total_score (int): The final score
        guess_card: input high or low
    """

    def __init__(self):
        """Construct a new Director
        Arg:
            self (Director): an instance of Director"""

        self.card = []
        self.is_playing = True
        
        self.score =0
        self.total_score =0

        
        for i in range(1):
            card = card()
            self.card.append(card)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
        self (Director): an instance of Director.

        """
        while self.is_playing:
            self.display_card()
            self.get_input()
            self.get_guessing()
            self.get_inputs_play()
            self.updates()
            self.do_outputs()

    def display_card(self):
        """the firsr random 
         Args:
        self (Director): an instance of Director
        """
        flip=self.flip()
        print("The playing card is {flip}")


    def get_input(self):
        """Ask the user if it's higher or low.

        Args:
            self (Director): An instance of Director.
        """
        user_guess = input("Higher or lower? [y/n]: ")
    
    def get_guessing(self):
        user_guess=""
        if self.flip > user_guess:
            self.value

    def get_inputs_play(self):
        """Ask the user if they want to roll.

        Args:
        self (Director): An instance of Director.
        """
        user_play = input("Play again? [y/n]: ")
        self.is_playing = (user_play == "y")

    def updates(self):
        """Updates the player's score"""

        if not self.is_playing:
            return 

        for i in range(len(self.card)):
            card = self.card[i]
            card.flip()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to follow. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        values = ""
        for i in range(len(self.card)):
            card = self.card[i]
            values += f"{card.value} "

        print(f"The playing card is: {values}")
        

