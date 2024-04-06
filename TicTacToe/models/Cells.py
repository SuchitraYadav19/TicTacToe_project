from dataclasses import dataclass, field
from TicTacToe.models.Cell_State import CellState
#from TicTacToe.models import Players
from typing import Optional


@dataclass
class Cell:
    row: int
    col: int
    cell_state: CellState = field(default=CellState.EMPTY)
    #player: Optional[Players.Player] = None

