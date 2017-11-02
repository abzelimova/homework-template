import json
import random

consignment = 0


def is_english_letters(word):
    alphabet = []
    for i in range(97, 123):
        index = i - 96
        alphabet.insert(index, (chr(i)))

    for i in range(len(word)):
        if word[i] in alphabet:
            return True
        else:
            return False


def kill_a_person(param):  # Вывод трупика
    if param == 0:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 ' ', ' ', '|', ' ', ' ', '', '|', ' ', ' ', '']
    if param == 1:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 '0', ' ', '|', ' ', ' ', '', '|', ' ', ' ', '']
    if param == 2:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 '0', ' ', '|', ' ', '|', '', '|', ' ', ' ', '']
    if param == 3:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 '0', ' ', '|', '-', '|', ' ', '|', ' ', ' ', '']
    if param == 4:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 '0', ' ', '|', '-', '|', '-', '|', ' ', ' ', '']
    if param == 5:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 '0', ' ', '|', '-', '|', '-', '|', ' ', '| ', '']
    if param >= 6:
        field = ['|', '-', '-', ' ', '|', ' ', '|', ' ', '|', ' ',
                 '0', ' ', '|', '-', '|', '-', '|', ' | | ', '']
    print_line(field)


def print_line(field):  # рисует правильного трупика в консоли
    n = 4
    print('------------------------')
    for i in range(0, len(field), n):
        prepared_line = ['{:2s}'.format((x)) for x in field[i:i + n]]
        print(''.join(prepared_line))
    print('------------------------')


class LogicOfGame(object):
    def __init__(self, word):
        self.word = word
        self.change_of_letters = str('_' * len(word))
        self.letter = ''
        self.param = 0
        self.guessed_letters = 0
        self.sum_of_letters = 0

    def is_right_letter(self):
        if self.letter not in self.word:
            print('Такой буквы нет!')
            self.param += 1
            kill_a_person(self.param)
            return False
        else:
            i = 0
            while i < len(self.word):
                if self.word[i] == self.letter:
                    self.guessed_letters += 1
                    self.change_of_letters = self.change_of_letters[:i] + \
                        self.letter + self.change_of_letters[i + 1:]
                i += 1
            return True

    def is_finish_game(self):
        if self.param >= 6 or self.change_of_letters == self.word:
            print('Игра окончена')
            return True
        return False

    def __str__(self):
        new = ''
        for i in self.change_of_letters:
            new += i + ' '
        return new


def start_game(game_word):
    game = LogicOfGame(game_word)
    while not game.is_finish_game():
        print(game)
        game.letter = input('Введите букву: ')
        game.sum_of_letters += 1
        game.is_right_letter()
    if game.param >= 6:
        print('Вы проиграли.Количество попыток: ', game.sum_of_letters,
              'Количество угаданых букв', game.guessed_letters)
        return False
    else:
        print('Количество попыток: ', game.sum_of_letters,
              'Количество угаданых букв', game.guessed_letters)
        return True


def main():
    computer_victiry = 0
    person_victory = 0
    first_victory = 0
    second_victory = 0
    round_count = 1

    choice = input('Введите 1 если хотите играть с человеком,'
                   '\n\r 2 - с компьютером. Мой выбор: ')
    print(choice)
    if choice == '1':
        while first_victory < 2 and second_victory < 2:
            game_word = input('Введите слово:')
            while not is_english_letters(game_word):
                print('Используйте только английские слова')
                game_word = input('Введите слово:')
            if start_game(game_word):
                if int(round_count) % 2 == 1:
                    first_victory += 1
                else:
                    second_victory += 1
            else:
                if int(round_count) % 2 == 1:
                    second_victory += 1
                else:
                    first_victory += 1
            round_count += 1
            print('Счет: ', first_victory, ' : ', second_victory)
        if first_victory == 2:
            print('Победил первый игрок')
        else:
            print('Победил второй игрок')

    if choice == '2':
        while computer_victiry < 2 and person_victory < 2:
            with open('words.json', 'r', encoding='utf-8') as fh:
                game_word = random.choice(json.load(fh)['words'])
            if start_game(game_word):
                    person_victory += 1
            else:
                computer_victiry += 1
            round_count += 1
            print('Счет: ', computer_victiry, ' : ', person_victory)
        if computer_victiry == 2:
            print('Победил компьютер игрок, а Вы проиграли')
        else:
            print('Поздравляем, Вы выиграли')


if __name__ == '__main__':
        try:
            main()
        except KeyboardInterrupt:
            print('bye')
