print("Welcome to Tic Tac Toe!")

matrix = [[" ", " ", " "],[" ", " ", " "],[" "," ", " "]]

def print_matrix():
    print(matrix[0][0], " | ", matrix[0][1], " | ", matrix[0][2])
    print("--------------")
    print(matrix[1][0], " | ", matrix[1][1], " | ", matrix[1][2])
    print("--------------")
    print(matrix[2][0], " | ", matrix[2][1], " | ", matrix[2][2])

"""
Functions:
    1. We need the game to keep looping until one wins, or no further moves are possible
    2. We need to make a move
        2a. We need to check if a move is valid
    3. We need to check if a player has won
    4. We need to check if the game is a draw

Attributes:
    1. The game board [matrix]
    2. The current player (X or O)
    3. Game State [not_started, "started", "ended"]
"""

