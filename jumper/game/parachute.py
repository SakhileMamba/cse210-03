from game.terminal_service import TerminalService
from game.letter import Letter
from game.player import Player

# This is our parachute class

class Parachute:
    """The displayed parachute. 
    
    The parachute will slowly disappear as the result of missed guesses of the word. 
    
    Attributes:
        _chute (list(str)) used to draw the parachute.
        -man (list(str)) used to draw the man

    """

    def __init__(self):
        """ Constructs a new parachute

        Args:
            self (parachute): An instance of parachute.
        """
        self._chute = ["  ___  ", " /___\ ", " \   / ", "  \ /  "] # The "_" before chute means it's private.
        self._man = ["   o   ", "  /|\  ", "  / \  ", "", "^^^^^^^"]
        
        """ Letter: word to guess.
        is_playing: determine whether the player wants o continue or not.
        terminal_service displays information on the screen.
        Player: One guessing the word."""
        self._is_playing = True
        self._terminal_service = TerminalService
        self._letter = Letter()
        self._player = Player()
    
    def start_game(self):
        """Starts the game"""
        while self.is_playing:
            self._get_input()
            self._do_updates()
            self._do_outputs()

    def get_input(self):
        """Player guesses letter"""
        new_letter = self._terminal_service.read_letter("\nEnter a letter: [a-z]")
        self._player.guess_letter(new_letter)

    def do_updates(self):
        """keeps track of what letter the player guessed"""
        self._letter.watch_letter(self._letter)

    def do_outputs(self):
        """Produces a hint"""
        hint = self.letter.get_hint()
        self._terminal_service.write_text(hint)
        if self._letter.is_found():
            self._is_playing = False
    def draw_chute(self):
        """METHOD will draw the chute
                
        Args:
            self (Parachute): An instance of Parachute.
        
        """
        for i in self._chute: # This loops through the list and prints the item in each index position.
            print(i)

    def draw_man(self):
        """METHOD will draw the man
                
        Args:
            self (Parachute): An instance of Parachute.
        
        """
        for i in self._man: # This loops through the list and prints the item in each index position.
            print(i)
    
    def erase_chute(self, answer): # will receive 'answer' data from the Word class                
        if answer == True:
            for i in self._chute:
                print(i)
            for i in self._man:
                print(i)
        
        if answer == False:
            self._chute.pop(0) # Removes the item at index position 0. Note, if you don't specify an index position, pop() removes the last item on the list.
            for i in self._chute:
                print(i)
            if len(self._chute) != 0: # This says, it the length of 'self._chute' does not (!) equal zero, loop through 'self._man' and print each index content.
                for i in self._man:
                    print(i)

        if len(self._chute) == 0:
            self._man[0] = "   x   " # if the length gets to zero, changes the content of index position [0] in 'self._man' to an 'x' to replace the head of our man.
            for i in self._man:
                print(i)
            end_game = print(f"You fell!\n") # the \n adds a new blank line after this is printed. It's for formatting purposes to make it look better in the terminal.
            return end_game # This 'return' statement takes effect only when this 'if' statement is reached and true. It ends the program.

    """ THIS IS THE FUNCTION I USED FOR TESTING. REMOVE EVERYTHING FROM HERE DOWN TO USE IN JUMPER PROGRAM """
    def erase_chute_test(self):
        valid_input = True
        while valid_input:
            answer = input("enter y or n: ")
            if answer == 'y' or answer == 'n':
                valid_input = True

                if answer == "y":
                    answer = True
                if answer == "n":
                    answer = False
                
                if answer == True:
                    for i in self._chute:
                        print(i)
                    for i in self._man:
                        print(i)
                
                if answer == False:
                    self._chute.pop(0) # Removes the item at index position 0. Note, if you don't specify an index position, pop() removes the last item on the list.
                    for i in self._chute:
                        print(i)
                    if len(self._chute) != 0: # This says, it the length of 'self._chute' does not (!) equal zero, loop through 'self._man' and print each index content.
                        for i in self._man:
                            print(i)

                if len(self._chute) == 0:
                    self._man[0] = "   x   " # if the length gets to zero, changes the content of index position [0] in 'self._man' to an 'x' to replace the head of our man.
                    for i in self._man:
                        print(i)
                    print(f"You fell!\n") # the \n adds a new blank line after this is printed. It's for formatting purposes to make it look better in the terminal.
                    break # This 'break' statement takes effect only when this 'if' statement is reached and true. It ends the program.
                        
            else:
                print("Invalid input, please try again") # This else statement works with the input validation. When the answer is not 'y' or 'n' valid_input becomes false and this is printed and the loop runs again.




""" Following lines for testing purposes. Uncomment and run parachute.py to test. """
parachute = Parachute() # creates an instance of parachute using the 'Parachute()' class
parachute.draw_chute() # uses the 'draw_chute()' Method (function) to draw the parachute
parachute.draw_man() # uses the 'draw_man()' Method (function) to draw the man.
parachute.erase_chute_test()