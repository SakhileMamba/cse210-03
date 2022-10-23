import random


class Word:

    def __init__(self):
        self._word_list = ["fox", "cat", "happy", "drama",
                           "cartoons", "television", "biscuits", "wifi", "laptop"]
        self._random_word = random.choice(self._word_list)
        self._guess_state = []

        for x in self._random_word:
            self._guess_state.append("_")

    def clue(self):
        return "".join(self._guess_state)

    def check_guess_matches(self, guessed_character):
        if guessed_character in self._random_word:
            i = 0
            for x in self._random_word:
                if x == guessed_character:
                    self._guess_state[i] = x
                i += 1

            return True
        else:
            return False

    def word_match_complete(self):
        if "".join(self._guess_state) == self._random_word:
            return True
        else:
            return False
