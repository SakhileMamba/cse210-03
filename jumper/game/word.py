import random


class Word:

    def __init__(self):
        self.word_list = ["fox", "cat", "happy", "drama",
                          "cartoons", "television", "biscuits", "wifi", "laptop"]
        self.random_word = random.choice(self.word_list)
        self.guess_state = []

        for x in self.random_word:
            self.guess_state.append("_")

        print(self.guess_state)

    def check_guess_matches(self, guessed_character):
        if guessed_character in self.random_word:
            i = 0
            for x in self.random_word:
                if x == guessed_character:
                    self.guess_state[i] = x
                i += 1

            print(self.guess_state)
            print("".join(self.guess_state))
            return True
        else:
            return False


word = Word()
word.check_guess_matches('e')
