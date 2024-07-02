# -*- coding: utf-8 -*-

import math
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    for row in board:
        if ' ' in row:
            return None
    return 'Draw'
def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves
def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return -1
    elif winner == 'O':
        return 1
    elif winner == 'Draw':
        return 0
    if is_maximizing:
        max_eval = -math.inf
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = 'O'
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = ' '
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_possible_moves(board):
            board[move[0]][move[1]] = 'X'
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = ' '
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval
def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for move in get_possible_moves(board):
        board[move[0]][move[1]] = 'O'
        move_value = minimax(board, 0, False, -math.inf, math.inf)
        board[move[0]][move[1]] = ' '
        if move_value > best_value:
            best_value = move_value
            best_move = move
    return best_move
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        while True:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Cell already taken. Try again.")
        print_board(board)
        if check_winner(board):
            break
        print("Simple will now play:")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
            print_board(board)
        if check_winner(board):
            break
    winner = check_winner(board)
    if winner == 'X':
        print("Congratulations! You win!")
    elif winner == 'O':
        print("Simple wins! Better luck next time.")
    else:
        print("It's a draw!")
play_game()
