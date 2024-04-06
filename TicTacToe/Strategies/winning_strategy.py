from abc import ABC, abstractmethod
from TicTacToe.models.Boards import Board
from TicTacToe.models.Moves import Move


class WinningStrategy(ABC):

    @abstractmethod
    def check_winning(self, board: Board, move: Move):
        pass

    @abstractmethod
    def undo(self, board: Board, move: Move):
        pass
