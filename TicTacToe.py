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

        if mark.isdigit() is True and int(mark) < 10 and int(mark) > 0 :
            board[int(mark)-1] = player.player_mark
            break
        else:
            print("Wrong input")


def main():
    player1 = Player("Player1", "X")
    player2 = Player("Player2", "O")
    player_list = [player1, player2]
    round_count = 0
    area_status = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    win_condition = Win(area_status)

    while True:
        os.system("cls")
        build_area(area_status)
        current_player = player_list[round_count % 2]
        mark_spot(current_player, area_status)
        if win_condition.is_win():
            build_area(area_status)
            print(current_player.player_name, " WON!")
            break
        round_count += 1
        time.sleep(1)


main()
