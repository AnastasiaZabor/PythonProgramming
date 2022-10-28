import tic_tac_toe

board = tic_tac_toe.TicTacToeBoard()
print(*board.get_field(), sep="\n")
board.make_move(1, 1)
print(*board.get_field(), sep="\n")
board.make_move(1, 2)
print(*board.get_field(), sep="\n")
board.make_move(1, 3)
print(*board.get_field(), sep="\n")
