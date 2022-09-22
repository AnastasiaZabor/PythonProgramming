import random

max_sweets_per_turn = 28

def lottery():
    return random.randint(0, 1)

def move(current_turn: int):
    if current_turn == 0:
        return player_move()
    return bot_move()

def bot_move():
    num = random.randint(1, 28)
    return num

def player_move():
    num = -1
    while not (0 < num <= max_sweets_per_turn):
        num = int(input("Введите кол-во конфет: "))
        if not (0 < num <= max_sweets_per_turn):
            print("Такое кол-во конфет нельзя взять!!!")
    return num

def inverse_current_turn(current_turn: int):
    if current_turn == 0:
        return 1
    return 0

def win(current_turn:int):
    if current_turn == 0:
        print("Вы победили")
    else:
        print("Победил бот")

def game():
    sweets = 2021

    current_turn = lottery()
    print(current_turn)
    num = move(current_turn)
    sweets -= num
    print(f'кол-во оставшихся конфет =  {sweets}')
    current_turn = inverse_current_turn(current_turn)

    while (sweets > 0):
        num = move(current_turn)
        if sweets >= num:
            sweets -= num
            print(f'взяли {num} конфет')
            print(f'кол-во оставшихся конфет =  {sweets}')
            current_turn = inverse_current_turn(current_turn)
        else:
            print(f'взяли последние {sweets} конфет')
            sweets = 0
            win(current_turn)
            return

game()



