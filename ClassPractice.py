import random

class Player:
    # This class defines Player with 2 parameters - PlayerX - where x stands for number of player
    # and player_mark witch can be X or O
    def __init__(self, player_name, player_mark):
        self.player_name = player_name
        self.player_mark = player_mark


class Chaotic_AI(Player):
    # Class with AI wich chosses random spot and place's mark as long as it isnt occupied
    def __init__(self):
        pass


class Game:
    # Class made to import settings / To occupy less lines of code
    def __init__(self):
        self.board_status = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        self.win = Win(self.board_status)
        self.player1 = Player("Player1", "X")
        self.player2 = Player("Player2", "O")
        self.player_list = [self.player1, self.player2]

    def build_area(board_status):
        print("--------------")
        print("|", board_status[0], "|", board_status[1], "|", board_status[2], "|")
        print("|", board_status[3], "|", board_status[4], "|", board_status[5], "|")
        print("|", board_status[6], "|", board_status[7], "|", board_status[8], "|")
        print("--------------")

    def mark_spot(self,player):
        while True:
            mark = input("Mark the spot 1-9.")

            if mark.isdigit() is True and 0 < int(mark) < 10:
                self.board_status[int(mark)-1] = player.player_mark
                break
            else:
                print("Wrong input")


    def is_space_free(self):
        # Checks if given space is free
        if self == " ":
            return True
        else:
            return False

    def build_area(self):

        print("--------------")
        print("|", self.board_status[0], "|", self.board_status[1], "|", self.board_status[2], "|")
        print("|", self.board_status[3], "|", self.board_status[4], "|", self.board_status[5], "|")
        print("|", self.board_status[6], "|", self.board_status[7], "|", self.board_status[8], "|")
        print("--------------")

    def random_spot(self):
        self.ran = random.randint(1,10)
        return self.ran

    def is_win(self):  # Main condition checking for winning configuration on the board / also returns true for Tie
        return self.is_win_horizontal() or self.is_win_vertical() or self.is_win_diagonal()

    def is_win_horizontal(self):
        index = 0
        while index < 9:
            if (self.board_status[index] == self.board_status[index + 1] == self.board_status[index + 2]) and self.board_status[index] != " ":
                return True
            index += 3
        return False

    def is_win_vertical(self):
        index = 0
        while index < 3:
            if (self.board_status[index] == self.board_status[index + 3] == self.board_status[index + 6]) and self.board_status[index] != " ":
                return True
            index += 1

        return False

    def is_win_diagonal(self):

        if (self.board_status[0] == self.board_status[4] == self.board_status[8]) and self.board_status[0] != " ":
            return True
        elif (self.board_status[2] == self.board_status[4] == self.board_status[6]) and self.board_status[2] != " ":
            return True
        else:
            return False

    def is_tie(self, round):
        if round == 9:
            return True
        else:
            return False









class Win:
    # Check if win condition is met on given board

    def __init__(self, board):
        self.board = board

    def is_win(self):  # Main condition checking for winning configuration on the board / also returns true for Tie
        return self.is_win_horizontal() or self.is_win_vertical() or self.is_win_diagonal()

    def is_win_horizontal(self):
        index = 0
        while index < 9:
            if (self.board[index] == self.board[index + 1] == self.board[index + 2]) and self.board[index] != " ":
                return True
            index += 3
        return False

    def is_win_vertical(self):
        index = 0
        while index < 3:
            if (self.board[index] == self.board[index + 3] == self.board[index + 6]) and self.board[index] != " ":
                return True
            index += 1

        return False

    def is_win_diagonal(self):

        if (self.board[0] == self.board[4] == self.board[8]) and self.board[0] != " ":
            return True
        elif (self.board[2] == self.board[4] == self.board[6]) and self.board[2] != " ":
            return True
        else:
            return False

    def is_tie(self, round):
        if round == 9:
            return True
        else:
            return False

