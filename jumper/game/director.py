from game.terminal_service import TerminalService
from game.parachute import Parachute
from game.word import Word


class Director:
    """A person who directs the game. 

    The responsibility of a Director is to control the sequence of play.

    Attributes:
        parachute (Parachute): The parachute that disappears as a result of missed guesses.
        is_playing (boolean): Whether or not to keep playing.
        word (Word): The hidden word which the user is trying to guess.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.

        Args:
            self (Director): an instance of Director.
        """
        self._is_playing = True
        self._letter_guess = ""

        self._parachute = Parachute()
        self._word = Word()
        self._terminal_service = TerminalService()

    def start_game(self):
        """Starts the game by running the main game loop.

        Args:230
            self (Director): an instance of Director.
        """

        while self._is_playing:
            if self._word.word_match_complete == True:
                self._terminal_service.write_text("Game won")
                self._is_playing = False
            elif len(self._parachute._chute) > 0:
                self._do_outputs()
                self._get_inputs()
                self._do_updates()
            # else:
            #    self._terminal_service.write_text("Game Over")

    def _get_inputs(self):
        """Gets input from the user.

        Args:
            self (Director): An instance of Director.
        """

        self._letter_guess = self._terminal_service.read_text(
            "\nGuess a letter [a-z]: ")
        #self._guess = self._word.check_guess_matches(letter_guess)

    def _do_updates(self):
        """Keeps watch on if the word is guessed an updates the parachute.

        Args:
            self (Director): An instance of Director.
        """
        guess_correct = self._word.check_guess_matches(self._letter_guess)

        self._parachute.erase_chute(guess_correct)

        if len(self._parachute._chute) == 0:
            self._is_playing = False

        if self._word.word_match_complete:
            self._is_playing = False

    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._terminal_service.write_text(self._word.clue())
        self._terminal_service.write_text(self._parachute._chute)
        self._terminal_service.write_text(self._parachute._man)
