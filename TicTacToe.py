# Tic Tac Toe game
import os
import time
from ClassPractice import Player, Game



def main():

    game = Game()
    round_count = 0

    while game.is_win() is False and round_count < 9:
        os.system("cls")
        game.build_area()
        current_player = game.player_list[round_count % 2]
        game.mark_spot(current_player)
        round_count += 1

    game.build_area()
    print(current_player.player_name, " WON!")

    if game.play_again() is True:
        return main()


main()
