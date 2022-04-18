'''Projekt Wisielec'''

key_word = 'Python'.upper()
LIVES = 6


def convert_key_word():
    converted_key_word = list(key_word)
    return converted_key_word

def make_invisible_board(converted_key_word):
    invisible_board = []
    for _ in range(len(converted_key_word)):
        invisible_board.append('_')
    return invisible_board

def take_user_input():
    inp = input('Wybierz literę>>>')
    return inp.upper()

def take_alphabet():
    letters = []
    for i in range(65,91):
        letters.append(chr(i))
    return letters

def check_user_input(alphabet):
    while True:
        user_input = take_user_input()
        if user_input not in alphabet:
            print('wybierz literę')
            continue
        return user_input



def check_if_letter_in_word(converted_key_word, ui):
    if ui in converted_key_word:
        return True
    return False

def give_exact_letters(ui, invisible_board, converted_key_word):
    for i in range(len(invisible_board)):
        if converted_key_word[i] == ui:
            invisible_board[i] = ui
    return invisible_board

def is_winner(table):
    for element in table:
        if element == '_':
            return False
    return True


def draw():
    print(' ___')
    print('|   |')
    print('|   O ')
    print("|  /|\\")
    print('|  / \\')
    print('|________')

def move(inv, converted_key_word, chances):
    alphabet = take_alphabet()
    ui = check_user_input(alphabet)
    letter_in = check_if_letter_in_word(converted_key_word, ui)
    table = give_exact_letters(ui, inv, converted_key_word)
    if letter_in:
        print(table)
    else:
        print(table)
        chances -= 1
        print(f'Ta litera nie występuje. Pozostało Ci {chances} sznas!')
    return chances

def main():
    chances = LIVES
    converted_key_word = convert_key_word()
    inv = make_invisible_board(converted_key_word)
    print(inv)
    while True:
        if is_winner(inv):
            print('To właściwe słowo! Zwycięstwo!')
            break
        chances = move(inv, converted_key_word, chances)
        if chances == 0:
            draw()
            break
    print('Dziękujemy za wspólną grę!')

main()
