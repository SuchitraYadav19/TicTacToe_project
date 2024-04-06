from TicTacToe.models.Boards import Board
from TicTacToe.models.Moves import Move
from TicTacToe.Strategies.winning_strategy import WinningStrategy
from TicTacToe.models.Players import Player

from typing import Dict


class DiagonalWinningStrategy(WinningStrategy):

    def __init__(self):
        self.left_map: Dict[str, int] = dict()
        self.right_map: Dict[str, int] = dict()

    def check_winning(self, board: Board, move: Move):
        arr = board.matrix
        r = move.cell.row
        c = move.cell.col

        player: Player = move.player

        if r == c:
            key_item = player.symbol.char
            if key_item not in self.left_map:
                self.left_map[key_item] = 0

            self.left_map[key_item] += 1

            if self.left_map[key_item] == board.size:
                return True

        if (r+c) == board.size-1:
            key_item = player.symbol.char
            if key_item not in self.right_map:
                self.right_map[key_item] = 0

            self.right_map[key_item] += 1

            if self.right_map[key_item] == board.size:
                return True

        return False

    def undo(self, board: Board, move: Move):
        r = move.cell.row
        c = move.cell.col

        player: Player = move.player
        key_item = player.symbol.char

        if r == c:
            self.left_map[key_item] -= 1

        if (r+c) == board.size-1:
            self.right_map[key_item] -= 1

