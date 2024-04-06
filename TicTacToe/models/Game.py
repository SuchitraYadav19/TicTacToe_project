from dataclasses import field
from typing import List, Optional


from TicTacToe.models.Symbols import Symbols
from TicTacToe.models.Player_Type import PlayerType
from TicTacToe.models.Boards import Board
from TicTacToe.models.Cells import Cell
from TicTacToe.models.Cell_State import CellState
from TicTacToe.models.Game_State import GameState
from TicTacToe.models.Moves import Move
from TicTacToe.models.Players import Player
from TicTacToe.models.HumanPlayers import HumanPlayer
from TicTacToe.Custom_Exceptions.SymbolsException import SymbolsNotUniqueException
from TicTacToe.Custom_Exceptions.NotAValidMove import MoveNotValidException
from TicTacToe.Custom_Exceptions.WrongDimention import WrongDimensionException
from TicTacToe.Strategies.winning_strategy import WinningStrategy
from TicTacToe.Strategies.RowWinningStrategy import RowWinningStrategy
from TicTacToe.Strategies.ColumnWinningStrategy import ColumnWinningStrategy
from TicTacToe.Strategies.DiagonalWinningStrategy import DiagonalWinningStrategy
from TicTacToe.Custom_Exceptions.NotAValidMove import MoveNotValidException


class Game:
    # board: Board
    # players: List[Player]
    # state: GameState = GameState.IN_PROGRESS
    # moves: List[Move]
    # winner: Player
    # next_player_idx: int
    # winning_strategy: List[WinningStrategy]

    def __init__(self, players: List[Player], winning_strat:List[WinningStrategy], dimension):
        self.players: List[Player] = players
        self.winning_strategy = winning_strat
        self.board = Board(dimension)
        self.moves: List[Move] = []
        self.state = GameState.IN_PROGRESS
        self.next_player_idx: int = 0
        self.winner: Optional[Player] = None

    @classmethod
    def get_builder(cls):
        return Game.GameBuilder()

    def undo(self):
        if len(self.moves) == 0:
            return
        last_move: Move = self.moves.pop()
        cell, player = last_move.cell, last_move.player

        r = cell.row
        c = cell.col
        self.next_player_idx = (self.next_player_idx - 1) % len(self.players)
        self.board.matrix[r][c] = Cell(r, c)

        for strats in self.winning_strategy:
            strats.undo(self.board, last_move)

    def make_move(self):
        curr_player: Player = self.players[self.next_player_idx]

        print(f"Turn of curr_player {curr_player.name}")

        curr_move: Move = curr_player.player_make_move(self.board)
        # print(curr_move)

        if self.__check_move(curr_move):
            cell: Cell = self.board.matrix[curr_move.cell.row][curr_move.cell.col]
            cell.player = curr_player
            cell.cell_state = CellState.FULL
            # print(curr_move)

        else:
            raise MoveNotValidException("Not a valid move")

        self.moves.append(curr_move)
        self.next_player_idx = (self.next_player_idx+1)% len(self.players)

        if self.__check_winning(board=self.board, move=curr_move):
            self.winner = curr_player
            self.state = GameState.ENDED

    def __check_winning(self, board: Board, move: Move) -> bool:
        each: WinningStrategy
        winnings = [each.check_winning(board, move) for each in self.winning_strategy]
        return any(winnings)

    def __check_move(self, mov: Move):
        cell: Cell = self.board.matrix[mov.cell.row][mov.cell.col]
        if cell.cell_state == CellState.EMPTY:
            return True
        return False

    def print_board(self):
        new_board = self.board.matrix
        for row in new_board:
            for cell in row:
                if cell.cell_state == CellState.EMPTY:
                    print("|      |", end="")
                else:
                    print(f"|  {cell.player.symbol.char}   |", end="")
            print()
        print("----------------")

    class GameBuilder:
        players: List[Player] = field(default_factory=list)
        winning_stgy: List[WinningStrategy] = field(default_factory=list)
        dimension: int = field(default=0)

        def set_dimension(self, dimension):
            self.dimension = dimension
            return self

        def add_player(self, player):
            self.players.append(player)
            return self

        def add_winning_strategy(self, strategy):
            self.winning_stgy.append(strategy)
            return self

        def set_winning_strategies(self, winning_strategies):
            self.winning_stgy = winning_strategies
            return self

        def set_players(self, players):
            self.players = players
            return self

        def __validate_dimension(self):
            if self.dimension != (len(self.players)+1):
                raise WrongDimensionException("Board dimension should be one grater than the number of players")
            return True

        def __validate_symbols(self):
            var = set([player.symbol.char for player in self.players])
            if len(var) != len(self.players):
                raise SymbolsNotUniqueException("Each player should have a unique symbol")
            return True

        def __validate(self):
            validations = [self.__validate_symbols(), self.__validate_dimension()]
            return all(validations)

        def build(self):
            if self.__validate():
                return Game(players=self.players, winning_strat=self.winning_stgy, dimension=self.dimension)


# if __name__ == "__main__":
#     dim = 3
#     to_players = [(HumanPlayer(symbol=Symbols("X"), name="A", iden=1, player_type=PlayerType.HUMAN)),
#                   (HumanPlayer(symbol=Symbols("O"), name="B", iden=2, player_type=PlayerType.HUMAN))]
#     winning_strategies = [
#         RowWinningStrategy(), ColumnWinningStrategy(), DiagonalWinningStrategy()
#     ]
#     builder = (Game.get_builder().
#                set_players(players=to_players).
#                set_winning_strategies(winning_strategies).
#                set_dimension(dimension=dim))
#     game = builder.build()
#     game.make_move()
#     game.print_board()



