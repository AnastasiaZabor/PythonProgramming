EMPTY_CELL = '-'
X_CELL = 'X'
ZERO_CELL = '0'

FIRST_PLAYER = 'X'
SECOND_PLAYER = '0'


class TicTacToeBoard:
    __field: list[list[str]]
    __state: str
    __current_player: str

    def __init__(self):
        self.__field = [[EMPTY_CELL for _ in range(3)] for _ in range(3)]
        self.__state = None
        self.__current_player = FIRST_PLAYER
        print('Начинаем игру')

    def get_field(self):
        return self.__field

    def check_field(self):
        return self.__state

    def make_move(self, row, col):
        if self.__field[row - 1][col - 1] != EMPTY_CELL:
            print(f'Клетка {row}, {col} уже занята')
        else:
            self.__field[row - 1][col - 1] = self.__current_player
            self._set_next_player()
        if self.__state is None:
            print('Продолжаем играть')
        return

    def _set_next_player(self):
        if self.__current_player == FIRST_PLAYER:
            self.__current_player = SECOND_PLAYER
        else:
            self.__current_player = FIRST_PLAYER



