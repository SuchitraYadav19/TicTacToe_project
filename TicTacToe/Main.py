from TicTacToe.models.Players import Player
from TicTacToe.models.HumanPlayers import HumanPlayer
from TicTacToe.models.Symbols import Symbols
from TicTacToe.models.Player_Type import PlayerType
from TicTacToe.models.Boards import Board
from TicTacToe.Strategies.winning_strategy import WinningStrategy
from TicTacToe.Strategies.RowWinningStrategy import RowWinningStrategy
from TicTacToe.Strategies.ColumnWinningStrategy import ColumnWinningStrategy
from TicTacToe.Strategies.DiagonalWinningStrategy import DiagonalWinningStrategy
from typing import List
from TicTacToe.Custom_Exceptions.NotAValidMove import MoveNotValidException
from TicTacToe.models.Game_State import GameState
from TicTacToe.controllers.Game_Controller import GameController


if __name__ == "__main__":

    controller = GameController()
    to_players = [(HumanPlayer(symbol=Symbols("X"), name="A", iden=1, player_type=PlayerType.HUMAN)),
                  (HumanPlayer(symbol=Symbols("O"), name="B", iden=2, player_type=PlayerType.HUMAN))]
    game = controller.start_game(
        dimension=3,
        players=to_players,
        winning_strategies=[
            RowWinningStrategy(), ColumnWinningStrategy(), DiagonalWinningStrategy()
        ]
    )
    # controller.make_move(game)
    # controller.print_board(game)
    while controller.check_game_state(game) == GameState.IN_PROGRESS:
        controller.print_board(game)
        move_or_undo = input("Enter m for move and u for undo: ")

        if move_or_undo == "m":
            try:
                controller.make_move(game)
            except MoveNotValidException:
                print("Invalid move")

        elif move_or_undo == "u":
            controller.undo(game)

    if controller.check_game_state(game) == GameState.ENDED:
        controller.print_board(game)
        print(f"Game is won by {controller.check_winner(game)}")

