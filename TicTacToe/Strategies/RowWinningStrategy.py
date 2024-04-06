from TicTacToe.models.Boards import Board
from TicTacToe.models.Moves import Move
from TicTacToe.models.Players import Player
from TicTacToe.Strategies.winning_strategy import WinningStrategy
from typing import Dict, Tuple


class RowWinningStrategy(WinningStrategy):

    def __init__(self):
        self.row_map: Dict[Tuple[int, str], int] = dict()

    def check_winning(self, board: Board, move: Move):
        arr = board.matrix
        r = move.cell.row

        player: Player = move.player

        key_items = (r, player.symbol.char)
        if key_items not in self.row_map:
            self.row_map[key_items] = 0

        self.row_map[key_items] += 1

        if self.row_map[key_items] == board.size:
            return True
        return False

    def undo(self, board: Board, move: Move):
        r = move.cell.row

        player: Player = move.player
        key_items = (r, player.symbol.char)
        self.row_map[key_items] -= 1
