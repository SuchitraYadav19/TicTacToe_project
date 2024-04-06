from dataclasses import dataclass, field
from TicTacToe.models.Symbols import Symbols as Sym
from TicTacToe.models.Player_Type import PlayerType

from TicTacToe.models.Boards import Board

@dataclass
class Player:
    symbol: Sym
    name: str
    iden : int
    player_type: PlayerType

    def player_make_move(self, board: Board):
        pass
        # row = int(input("Enter row number: "))
        # col = int(input("Enter column number: "))
        #
        # print(f"Player {self.name} selected {row} {col}")
        #
        # mov = Move(cell=Cell(row, col), player=self)
        # # print(mov)
        # return mov


