import copy
import random


class TicTacToeAI:
    def __init__(self, player):
        self.player = player

    def get_move(self, board, size):
        # Find all available positions on the board
        size = int(size)
        available_moves = []
        for i in range(size):
            for j in range(size):
                if board[i][j] == ' ':
                    available_moves.append((i, j))
                    
        # If there are no available moves, return None
        if not available_moves:
            return None
        # Choose a random available move
        return available_moves[random.randint(0, len(available_moves) - 1)]
