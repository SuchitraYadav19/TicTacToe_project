from dataclasses import dataclass, field
from typing import List
from TicTacToe.models.Cells import Cell
from TicTacToe.models.Cell_State import CellState


@dataclass
class Board:
    size: int
    matrix: List[List[Cell]] = field(init=False)

    def __post_init__(self):
        self.matrix = []
        for i in range(self.size):
            curr = []
            for j in range(self.size):
                curr.append(Cell(i, j))
            self.matrix.append(curr)


if __name__ == "__main__":
    b = Board(3)
    print(b.matrix)

