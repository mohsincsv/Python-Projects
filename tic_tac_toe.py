from tkinter import *
import random

COLORS = ['red','blue']
players = ['X','O']
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


def Give_Pass(row,col):

    global player

    if buttons[row][col]['text'] == "" and is_found_winner() is False:

        if player == players[0]:

            buttons[row][col]['text'] = player
            buttons[row][col]['fg'] = COLORS[0]
            buttons[row][col]['bg'] = 'white'

            if is_found_winner() is False:
                player = players[1]
                label.config(text= players[1]+" turn")

            elif is_found_winner() is True:
                label.config(text= players[0]+" Wins")
            elif is_found_winner() == "Tied":
                label.config(text= "Tied")

        else:

            buttons[row][col]['text'] = player
            buttons[row][col]['fg'] = COLORS[1]
            buttons[row][col]['bg'] = 'white'

            if is_found_winner() is False:
                player = players[0]
                label.config(text= players[0] + " turn")

            elif is_found_winner() is True:
                label.config(text= players[1] + "'Wins")
            elif is_found_winner() == "Tied":
                label.config(text= player + "'Tied")

def is_found_winner():
    
    # Checking for Rows

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] ==buttons[row][2]['text'] != "":
            buttons[row][0]['bg'] = 'lightGreen'
            buttons[row][1]['bg'] = 'lightGreen'
            buttons[row][2]['bg'] = 'lightGreen'
            return True

    # Checking for Cols

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] ==buttons[2][col]['text'] != "":
            buttons[0][col]['bg'] = 'lightGreen'
            buttons[1][col]['bg'] = 'lightGreen'
            buttons[2][col]['bg'] = 'lightGreen'
            return True

    # Checking for Diagonals

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0]['bg'] = 'lightGreen'
        buttons[1][1]['bg'] = 'lightGreen'
        buttons[2][2]['bg'] = 'lightGreen'
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2]['bg'] = 'lightGreen'
        buttons[1][1]['bg'] = 'lightGreen'
        buttons[2][0]['bg'] = 'lightGreen'
        return True

    elif is_Full() == True:

        for row in range(3):
            for col in range(3):
                buttons[row][col]['bg'] = 'lightYellow'
        
        return "Tied"

    else:
        return False

def is_Full():
    
    count = 0

    for row in range(3):
        for col in range(3):
            if buttons[row][col]['text'] == "":
                count += 1

    if count >= 1:
        return False
    else:
        return True

def NewGame():
    
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text="",bg="#F0F0F0")

if __name__ == '__main__':

    window = Tk()
    window.title("Tic-Tac-Toe Game")

    label = Label(text=player + " turn", font=("Consolas",40))
    label.pack()

    rst_bttn = Button(text='Restart', font=("Consolas",20),
    command=NewGame)
    rst_bttn.pack()

    frame = Frame(window)
    frame.pack()

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                    command= lambda row=row, column=column: Give_Pass(row,column))
            buttons[row][column].grid(row=row,column=column)


    window.mainloop()