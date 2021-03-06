from ui import UI
import random
import re


class Hangman:
    word_list = []

    def __init__(self, lives=5):
        self.word_to_guess = random.choice(self.word_list)
        self.used_letters = []
        self.wrong_words_tried = []
        self.lives = lives
        self.attempts_counts = 1

    @property
    def dashes(self):
        letters_to_replace_with_dashes_pattern = self.pattern_from_used_letter()
        return re.sub(letters_to_replace_with_dashes_pattern, '_', self.word_to_guess)

    @classmethod
    def add_word(cls, word):
        cls.word_list.append(word)

    def get_dashes(self):
        return self.dashes

    def get_lives(self):
        return self.lives

    def get_used_letters(self):
        return self.used_letters

    def get_word_to_guess(self):
        return self.word_to_guess

    def get_attempts_counts(self):
        return self.attempts_counts

    def pattern_from_used_letter(self):
        return re.compile('[^ {}]'.format(''.join(self.used_letters)))

    def next_try(self):
        UI.print_try_kinds()
        try_kind = UI.input_try_kind()
        if try_kind == 'letter':
            self.next_letter_try()
        if try_kind == 'word':
            self.all_word_try()
        self.attempts_counts += 1

    def next_letter_try(self):
        letter = UI.input_letter()
        letter = letter.upper()
        if letter in self.word_to_guess:
            self.correct_letter_try(letter)
        else:
            self.wrong_letter_try(letter)

    def correct_letter_try(self, letter):
        self.used_letters.append(letter)

    def wrong_letter_try(self, letter):
        self.lives -= 1
        self.used_letters.append(letter)

    def all_word_try(self):
        word = UI.input_all_word()
        if word == self.word_to_guess:
            self.correct_word_try(word)
        else:
            self.wrong_word_try(word)

    def correct_word_try(self, word):
        self.used_letters.extend(list(word))

    def wrong_word_try(self, word):
        self.lives -= 1


class HangmanResult:
    results = []

    def __init__(self, word_to_guess, lives, attempts, player):
        self.word_to_guess = word_to_guess
        self.saved_lives = lives
        self.attempts = attempts
        self.player = player
        HangmanResult.results.append(self)

    @classmethod
    def add_result(cls, word_to_guess, lives, attempts, player):
        result = HangmanResult(word_to_guess, lives, attempts, player)
        player.add_result(result)

    @classmethod
    def get_results(cls):
        return cls.results

    def get_word_to_guess(self):
        return self.word_to_guess

    def get_saved_lives(self):
        return self.saved_lives

    def get_attempts(self):
        return self.attempts

    def get_player(self):
        return self.player

