class Player:
    # This class defines Player with 2 parameters - PlayerX - where x stands for number of player
    # and player_mark witch can be X or O
    def __init__(self, player_name, player_mark):
        self.player_name = player_name
        self.player_mark = player_mark


"""""""""""
class WinCondition:
    # This class is set of rules defining win condition and ending a game
    def __init__(self,position1,position2,position3):
        self.position1 = position1
        self.position2 = position2
        self.position3 = position3

    def Win(self):
        # Checks if 3 positions are occupied by the same symbol
        if self.position1 == self.position2 == self.position3:
            return True
        else:
            return False

"""""""""


class Win:
    # Check if win condition is met on given board

    def __init__(self, board):
        self.board = board

    def is_win(self):
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
