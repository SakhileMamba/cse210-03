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
        self._chute = ["  ___  ", " /___\ ", " \   / ",
                       "  \ /  "]  # The "_" before chute means it's private.
        self._man = ["   o   ", "  /|\  ", "  / \  ", "", "^^^^^^^"]

    def erase_chute(self, answer):  # will receive 'answer' data from the Word class
        if answer == True:
            for i in self._chute:
                print(i)
            for i in self._man:
                print(i)

        elif answer == False:
            # Removes the item at index position 0. Note, if you don't specify an index position, pop() removes the last item on the list.
            self._chute.pop(0)
            for i in self._chute:
                print(i)
            # This says, it the length of 'self._chute' does not (!) equal zero, loop through 'self._man' and print each index content.
            if len(self._chute) != 0:
                for i in self._man:
                    print(i)

        if len(self._chute) == 0:
            # if the length gets to zero, changes the content of index position [0] in 'self._man' to an 'x' to replace the head of our man.
            self._man[0] = "   x   "
            for i in self._man:
                print(i)
            # end_game = print(f"You fell!\n") # Was going to return this print statement when chute == 0 but switched to boolean to end game from Director.
            # This 'return' statement takes effect only when this 'if' statement is reached and true. It ends the program.
            return True
