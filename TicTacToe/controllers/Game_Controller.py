from TicTacToe.models.Game import Game
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


class GameController:

    def start_game(self, players: List[Player], winning_strategies, dimension):
        builder = (Game.get_builder().
                   set_players(players=players).
                   set_winning_strategies(winning_strategies).
                   set_dimension(dimension=dimension))
        return builder.build()

    def make_move(self, game: Game):
        game.make_move()

    def undo(self, game: Game):
        game.undo()

    def check_winner(self, game: Game):
        return game.winner.name
    def check_game_state(self, game):
        return game.state

    def print_board(self, game):
        game.print_board()


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
        try:
            controller.make_move(game)
        except MoveNotValidException:
            print("Invalid move")

    if controller.check_game_state(game) == GameState.ENDED:
        print(f"Game is won by {controller.check_winner(game)}")

