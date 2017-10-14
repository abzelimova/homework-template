# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see:
# https://docs.python.org/3/library/random.html#random.shuffle
import random

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """

    field = [i for i in range(1, 16)]
    field.append(EMPTY_MARK)

    for _ in range(100):
        move = random.choice(list(MOVES.keys()))
        try:
            field = perform_move(field, move)
        except IndexError:
            pass

    # random.shuffle(field)

    return field


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """

    print('-' * 12)
    i = 0
    while i < 4:
        print('|'.join([str(title).ljust(2) for
                        title in field[i * 4:i * 4 + 4]]))
        i += 1
        print('-' * 12)


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    for i in range(1, len(field)):
        if field[i - 1] != i or field[i - 1] == EMPTY_MARK:
            return False

    return True


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """

    index_x = field.index(EMPTY_MARK)

    if index_x % 4 == 0 and key == 'a':
        raise IndexError()
    elif index_x % 4 == 3 and key == 'd':
        raise IndexError()
    elif index_x < 4 and key == 'w':
        raise IndexError()
    elif index_x > 11 and key == 's':
        raise IndexError()

    new_field = list(field)
    new_field[index_x], new_field[index_x + MOVES[key]] =\
        new_field[index_x + MOVES[key]], new_field[index_x]

    return new_field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right
    :return: <str> current move.
    """
    move = None
    while move not in MOVES.keys():
        move = input('Use "wasd" for step:\n')

    return move


def main():
    """
    The main method. It stars when the program is called.
    It also calls other methods.
    :return: None
    """

    field = shuffle_field()
    amount_moves = 0

    while True:
        try:
            print_field(field)
            key = handle_user_input()
            field = perform_move(field, key)
            amount_moves += 1
            if is_game_finished(field):
                print('You`re win! You have made {} steps').format(amount_moves)
                break

        except IndexError:
            print('It`s not possible. Try again')


if __name__ == '__main__':
    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    try:
        main()
    except KeyboardInterrupt:
        print('shutting down')
