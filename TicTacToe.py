# Tic Tac Toe game
import os
import time
from ClassPractice import Game, Chaotic_AI, Player


def two_players():

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


def one_player():

    game = Game()
    ai = Chaotic_AI(game)
    player = Player("You", "X")
    round_count = 0

    while round_count < 9:
        os.system("cls")
        game.build_area()

        if round_count % 2 == 0:
            game.mark_spot(player)
            round_count += 1
            if game.is_win():
                game.build_area()
                print("You win!")
                break
            else:
                continue

        elif round_count % 2 == 1:
            ai.mark_spot_comp()
            round_count += 1
            if game.is_win():
                game.build_area()
                print("Ai wins")
                break
            else:
                continue

    if game.is_tie():
        game.build_area()
        print("Tie")
    else:
        pass


def main():
    print("Welcome to TicTacToe")
    game_mode = input("1 for 1 Player vs AI | 2 for 2 players")
    if game_mode == "1":
        one_player()
    elif game_mode == "2":
        two_players()

    if Game.play_again(True) is True:
        return main()


main()

'''''''''''
Problemy: Można postawić swój krzyżyk na czyimś kółku
          Przez to powyżej gra liczy tylko 9 rund i zawsze kończy się remisem. 
'''''''''''
