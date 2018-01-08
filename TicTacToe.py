# Tic Tac Toe game
import os
import time
from ClassPractice import Player, Win


def build_area(board_status):
    print("--------------")
    print("|", board_status[0], "|", board_status[1], "|", board_status[2], "|")
    print("|", board_status[3], "|", board_status[4], "|", board_status[5], "|")
    print("|", board_status[6], "|", board_status[7], "|", board_status[8], "|")
    print("--------------")


def mark_spot(player, board):  # For argument takes Player (X or O), and board (List in which changes will be made)
    while True:
        mark = input("Mark the spot 1-9.")

        if mark.isdigit() is True and 0 < int(mark) < 10:
            board[int(mark)-1] = player.player_mark
            break
        else:
            print("Wrong input")


def play_again():

    again = input("Write y to play again or anything to leave")
    if again.lower() == "y":
        main()
    else:
        pass


def main():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    player_list = [player1, player2]
    round_count = 0
    area_status = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    win_condition = Win(area_status)

    while win_condition.is_win() is False and round_count < 9:
        os.system("cls")
        build_area(area_status)
        current_player = player_list[round_count % 2]
        mark_spot(current_player, area_status)
        round_count += 1
        time.sleep(1)

    if win_condition.is_tie(round_count):
        build_area(area_status)
        print("Tie!")
    else:
        build_area(area_status)
        print(current_player.player_name, " WON!")

    play_again()



main()


# BugFixes:
# Wrong input on turn changing player / solved : while loop
# Known issues/Wannabe features : Mark same spot problem/ Player turn indicator/ Win count / (panic)Exit button
# Wish : Starting rules set into text file (code frugality)