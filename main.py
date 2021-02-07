import numpy as np
import math
import os

ai, human = 'X', 'O'

def clear():
    os.system('cls')

def check_winner(board):
    rows, cols = np.shape(board)
    cond_1 = np.hsplit(board, 3)
    cond_2 = np.vsplit(board, 3)

    board_flip = np.fliplr(board)
    x_case = np.where(board.diagonal() == 'X', True, False)
    x_case_f = np.where(board_flip.diagonal() == 'X', True, False)
    o_case = np.where(board.diagonal() == 'O', True, False)
    o_case_f = np.where(board_flip.diagonal() == 'O', True, False)

    if x_case.all() or x_case_f.all():
        return 'X'
    elif o_case.all() or o_case_f.all():
        return 'O'

    for elem in cond_1:
        caseX = np.where(elem == 'X', True, False)
        caseO = np.where(elem == 'O', True, False)
        if caseX.all():
            return 'X'
        elif caseO.all():
            return 'O'
    for elem in cond_2:
        caseX = np.where(elem == 'X', True, False)
        caseO = np.where(elem == 'O', True, False)
        if caseX.all():
            return 'X'
        elif caseO.all():
            return 'O'

    if np.where(board != '', True, False).all():
        return 'tie'

def best_move(board):
    pos = np.argwhere(board.__eq__('') == True)
    move = []
    best_score = -math.inf
    for values in pos:
        x, y = values
        board[x, y] = ai
        score = min_value(board, 0)
        board[x, y] = ''
        if score > best_score:
            best_score = score
            move = [x, y]

    board[move[0], move[1]] = ai
    print_board(board)
    make_move(board)


def min_value(board, depth):

    if check_winner(board) == human:
        return -10
    elif check_winner(board) == ai:
        return 10
    elif check_winner(board) == 'tie':
        return 0
    pos = np.argwhere(board.__eq__('') == True)

    best_score = math.inf
    for values in pos:
        x, y = values
        board[x, y] = human
        score = max_value(board, depth+1)
        board[x, y] = ''
        best_score = min(score, best_score)
    return best_score

def max_value(board, depth):
    if check_winner(board) == human:
        return -10
    elif check_winner(board) == ai:
        return 10
    elif check_winner(board) == 'tie':
        return 0

    pos = np.argwhere(board.__eq__('') == True)
    best_score = -math.inf
    for values in pos:
        x, y = values
        board[x, y] = ai
        score = min_value(board, depth+1)
        board[x, y] = ''
        best_score = max(best_score, score)

    return best_score

def make_move(board):
    current_move = human
    if check_winner(board) == ai:
        print("Ai won the game")
    elif check_winner(board) == 'tie':
        print('It is a tie')
    elif current_move == human:
        x = int(input("Please enter X co-ordinate: "))
        y = int(input("Please enter Y co-ordinate: "))
        try:
            if board[x, y] == '':
                board[x, y] = human
                if check_winner(board) == human:
                    print("Congratulations you won the game")
                elif check_winner(board) == 'tie':
                    print_board(board)
                    print("It's a tie")
                else:
                    best_move(board)
            else:
                print("Position is already occupied, Please enter new pos:")
                make_move(board)
        except:
            print("Invalid Position. Please enter again:")
            make_move(board)

def print_board(board):
    clear()
    for index, elems in enumerate(board):
        for idx, val in enumerate(elems):
            if idx != 2:
                print('', val, ' | ', end='')
            else:
                print(val)
        if index != 2:
            print('-------------')


if __name__ == '__main__':
    board = np.full((3, 3), '', dtype=str)
    print_board(board)
    make_move(board)
