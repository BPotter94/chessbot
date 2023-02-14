import math


class ChessGame:
    def __init__(self):
        self.board = [["R", "N", "B", "Q", "K", "B", "N", "R"],
                      ["P", "P", "P", "P", "P", "P", "P", "P"],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      [".", ".", ".", ".", ".", ".", ".", "."],
                      ["p", "p", "p", "p", "p", "p", "p", "p"],
                      ["r", "n", "b", "q", "k", "b", "n", "r"]
                      ]
        self.white_to_move = True

    def display_board(self):
        for row in self.board:
            print(" ".join(row))
        print("")

    # def make_move(self, move):
    #     self.board[move[0][1]][move[0][0]] = "."
    #     self.board[move[1][1]][move[1][0]] = move[2]
    #     self.white_to_move = not self.white_to_move

    # def get_possible_moves(self):
    #     moves = []
    #     for i in range(8):
    #         for j in range(8):
    #             piece = self.board[i][j]
    #             if piece == ".":
    #                 continue
    #             if piece.islower() == self.white_to_move:
    #                 continue
    #             if piece == "P":
    #                 if self.white_to_move:
    #                     if i == 6:
    #                         moves.append([(j, i), (j, i - 1), piece])
    #                         moves.append([(j, i), (j, i - 2), piece])
    #                     elif i > 0 and self.board[i - 1][j] == ".":
    #                         moves.append([(j, i), (j, i - 1), piece])
    #                     if j > 0 and i > 0 and self.board[i - 1][j - 1].islower():
    #                         moves.append([(j, i), (j - 1, i - 1), piece])
    #                     if j < 7 and i > 0 and self.board[i - 1][j + 1].islower():
    #                         moves.append([(j, i), (j + 1, i - 1), piece])
    #                 else:
    #                     if i == 1:
    #                         moves.append([(j, i), (j, i + 1), piece])
    #                         moves.append([(j, i), (j, i + 2), piece])
    #                     elif i < 7 and self.board[i + 1][j] == ".":
    #                         moves.append([(j, i), (j, i + 1), piece])
    #                     if j > 0 and i < 7 and self.board[i + 1][j - 1].isupper():
    #                         moves.append([(j, + 1)].isupper())
    #                         moves.append([(j, i), (j + 1, i + 1), piece])
    #             elif piece == "N":
    #                 for x in [-2, -1, 1, 2]:
    #                     for y in [-2, -1, 1, 2]:
    #                         if abs(x) != abs(y) and 0 <= j + x < 8 and 0 <= i + y < 8:
    #                             moves.append([(j, i), (j + x, i + y), piece])
    #             elif piece == "B":
    #                 for x, y in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
    #                     for k in range(1, 8):
    #                         if 0 <= j + k * x < 8 and 0 <= i + k * y < 8:
    #                             if self.board[i + k * y][j + k * x] == ".":
    #                                 moves.append(
    #                                     [(j, i), (j + k * x, i + k * y), piece])
    #                             else:
    #                                 if self.board[i + k * y][j + k * x].islower() != self.white_to_move:
    #                                     moves.append(
    #                                         [(j, i), (j + k * x, i + k * y), piece])
    #                                 break
    #             elif piece == "R":
    #                 for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    #                     for k in range(1, 8):
    #                         if 0 <= j + k * x < 8 and 0 <= i + k * y < 8:
    #                             if self.board[i + k * y][j + k * x] == ".":
    #                                 moves.append(
    #                                     [(j, i), (j + k * x, i + k * y), piece])
    #                             else:
    #                                 if self.board[i + k * y][j + k * x].islower() != self.white_to_move:
    #                                     moves.append(
    #                                         [(j, i), (j + k * x, i + k * y), piece])
    #                                 break
    #             elif piece == "Q":
    #                 for x, y in [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]:
    #                     for k in range(1, 8):
    #                         if 0 <= j + k * x < 8 and 0 <= i + k * y < 8:
    #                             if self.board[i + k * y][j + k * x] == ".":
    #                                 moves.append(
    #                                     [(j, i), (j + k * x, i + k * y), piece])
    #                             else:
    #                                 if self.board[i + k * y][j + k * x].islower() != self.white_to_move:
    #                                     moves.append(
    #                                         [(j, i), (j + k * x, i + k * y), piece])
    #                                 break
    #             elif piece == "K":
    #                 for x in [-1, 0, 1]:
    #                     for y in [-1].isupper():
    #                         moves.append([(j, i), (j + 1, i + 1), piece])
    #             elif piece == "N":
    #                 for x in [-2, -1, 1, 2]:
    #                     for y in [-2, -1, 1, 2]:
    #                         if abs(x) != abs(y) and 0 <= j + x < 8 and 0 <= i + y < 8:
    #                             moves.append([(j, i), (j + x, i + y), piece])
    #             elif piece == "B":
    #                 for x, y in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
    #                     for k in range(1, 8):
    #                         if 0 <= j + k * x < 8 and 0 <= i + k * y < 8:
    #                             if self.board[i + k * y][j + k * x] == ".":
    #                                 moves.append(
    #                                     [(j, i), (j + k * x, i + k * y), piece])
    #                             else:
    #                                 if self.board[i + k * y][j + k * x].islower() != self.white_to_move:
    #                                     moves.append(
    #                                         [(j, i), (j + k * x, i + k * y), piece])
    #                                 break
    #             elif piece == "R":
    #                 for x, y in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
    #                     for k in range(1, 8):
    #                         if 0 <= j + k * x < 8 and 0 <= i + k * y < 8:
    #                             if self.board[i + k * y][j + k * x] == ".":
    #                                 moves.append(
    #                                     [(j, i), (j + k * x, i + k * y), piece])
    #                             else:
    #                                 if self.board[i + k * y][j + k * x].islower() != self.white_to_move:
    #                                     moves.append(
    #                                         [(j, i), (j + k * x, i + k * y), piece])
    #                                 break
    #             elif piece == "Q":
    #                 for x, y in [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]:
    #                     for k in range(1, 8):
    #                         if 0 <= j + k * x < 8 and 0 <= i + k * y < 8:
    #                             if self.board[i + k * y][j + k * x] == ".":
    #                                 moves.append(
    #                                     [(j, i), (j + k * x, i + k * y), piece])
    #                             else:
    #                                 if self.board[i + k * y][j + k * x].islower() != self.white_to_move:
    #                                     moves.append(
    #                                         [(j, i), (j + k * x, i + k * y), piece])
    #                                 break
    #             elif piece == "K":
    #                 for x in [-1, 0, 1]:
    #                     for y in range(1, 8):
    #                         moves.append([(j, i), (j + x, i + y), piece])
    #     return moves

    # def make_move(self, move):
    #     self.board[move[1][1]][move[1][0]] = self.board[move[0][1]][move[0][0]]
    #     self.board[move[0][1]][move[0][0]] = "."
    #     self.white_to_move = not self.white_to_move

    # def evaluate_board(self):
    #     value = 0
    #     for i in range(8):
    #         for j in range(8):
    #             piece = self.board[i][j]
    #             if piece != ".":
    #                 if piece.isupper():
    #                     value += piece_values[piece]
    #                 else:
    #                     value -= piece_values[piece.upper()]
    #     return value

    # def minimax(self, depth, maximizing_player):
    #     if depth == 0:
    #         return self.evaluate_board()

    #     if maximizing_player:
    #         best_value = -math.inf
    #         for move in self.generate_moves():
    #             self.make_move(move)
    #             value = self.minimax(depth - 1, False)
    #             self.undo_move(move)
    #             best_value = max(best_value, value)
    #         return best_value
    #     else:
    #         best_value = math.inf
    #         for move in self.generate_moves():
    #             self.make_move(move)
    #             value = self.minimax(depth - 1, True)
    #             self.undo_move(move)
    #             best_value = min(best_value, value)
    #         return best_value

    # def get_best_move(self):
    #     best_value = math.inf
    #     best_move = None
    #     for move in self.get_possible_moves():
    #         self.make_move(move)
    #         value = self.minimax(4, False)
    #         self.undo_move(move)
    #         if value > best_value:
    #             best_value = value
    #             best_move = move
    #     return best_move

    def play_game(self):
        while True:
            if self.white_to_move:
                print("White to move:")
                self.display_board()
                # move = self.get_best_move()
                # print("White moves", move)
                # self.make_move(move)
            else:
                print("Black to move:")
                self.display_board()
                # move = self.get_best_move()
                # print("Black moves", move)
                # self.make_move(move)


if __name__ == "__main__":
    game = ChessGame()
    game.play_game()