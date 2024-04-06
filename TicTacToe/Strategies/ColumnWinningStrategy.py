from TicTacToe.models.Boards import Board
from TicTacToe.models.Moves import Move
from TicTacToe.Strategies.winning_strategy import WinningStrategy
from TicTacToe.models.Players import Player

from typing import Dict,Tuple


class ColumnWinningStrategy(WinningStrategy):

    def __init__(self):
        self.col_map: Dict[Tuple[int, str], int] = dict()

    def check_winning(self, board: Board, move: Move):
        arr = board.matrix

        c = move.cell.col
        player: Player = move.player

        key_items = (c, player.symbol.char)
        if key_items not in self.col_map:
            self.col_map[key_items] = 0

        self.col_map[key_items] += 1

        if self.col_map[key_items] == board.size:
            return True
        return False

    def undo(self, board: Board, move: Move):
        c = move.cell.col

        player: Player = move.player
        key_items = (c, player.symbol.char)
        self.col_map[key_items] -= 1

