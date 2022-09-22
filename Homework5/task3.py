from tkinter import *
import random, time

def game(x:int):
    global game1
    global game2
    global station_number
    max_station_number = 8
    game1[x] = 'X'
    buttons[x].config(text='X', bg='grey', state='disabled')
    game2.remove(x)
    if x == 4 and station_number == 0:
        t = random.choice(game2)
    elif x != 4 and station_number == 0:
        t = 4
    if station_number > 0:
        t = max_station_number - x
    game1[t] = 'O'
    time.sleep(1)
    buttons[t].config(text='O', bg='grey', state='disabled')
    game2.remove(t)
    station_number +=1

def win(game2:int, t:int):
    if (len(game2) > 1):
        game2.remove(t)
    else:
        label['text'] = Label(text="Игра закончена ничьей")


game1 = [None] * 9
game2 = list(range(9))
station_number = 0


root = Tk()
label = Label(width=20, text="Крестики-нолики", font=('Arial', 16, 'bold'))
buttons = [Button(width=5, height=2, font=('Arial', 20, 'bold'), bg='blue', command= lambda x = i: game(x)) for i in range(9)]

label.grid(row=0, column=0, columnspan=3)
row = 1
col = 0

for i in range(9):
    buttons[i].grid(row=row, column=col)
    col += 1
    if col == 3:
        row +=1
        col = 0
root.mainloop()
