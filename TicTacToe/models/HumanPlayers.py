from dataclasses import dataclass, field
from TicTacToe.models.Symbols import Symbols
from TicTacToe.models.Player_Type import PlayerType
from TicTacToe.models.Players import Player
from TicTacToe.models import Moves
from TicTacToe.models import Cells
from TicTacToe.models.Boards import Board


@dataclass
class HumanPlayer(Player):

    def player_make_move(self, board: Board):
        row = int(input("Enter row number: "))
        col = int(input("Enter column number: "))

        print(f"Player {self.name} selected {row} {col}")

        return Moves.Move(cell=Cells.Cell(row, col), player=self)


# if __name__ == "__main__":
#     b = Board(3)
#     sym = Symbols("X")
#     h_player = HumanPlayer(symbol=sym,name="A", iden= 1, player_type=PlayerType.HUMAN)
#     h_player.player_make_move(b)
#     print(h_player)

