import tkinter

def check_null():
    for column in range(3):
        for row in range(3):
            if buttons[column][row]['text'] == "":
                return False
    return True

def print_winner():
    global win

    if win is False:
        win = True
        print("Le joueur " + current_player + " à gagné !")
        reset_game()

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def check_win(clicked_row, clicked_col):
    # win horizontal
    count = 0
    for i in range(3):
        current_button = buttons[i][clicked_row]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # win vertical
    count = 0
    for i in range(3):
        current_button = buttons[clicked_col][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # win diagonal
    count = 0
    for i in range(3):
        current_button = buttons[i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    # win diagonal reverse
    count = 0
    for i in range(3):
        current_button = buttons[2-i][i]
        if current_button['text'] == current_player:
            count += 1
    if count == 3:
        print_winner()

    if win is False:
        count = 0
        for  col in range(3):
            for row in range(3):
                current_button = buttons[col][row]
                if current_button['text'] == "X" or current_button['text'] == "O":
                    count += 1
        if count == 9:
            print("Match nul !")
            reset_game()

def place_symbole(row, column):
    clicked_button = buttons[column][row]
    if clicked_button['text'] == "" :
        clicked_button.config(text = current_player)

        check_win(row, column)
        switch_player()

def reset_game():
    global win, current_player
    for column in range(3):
        for row in range(3):
            buttons[column][row].config(text="")
    win = False
    current_player = "X"

def draw_grid():
    for column in range(3):
        buttons_in_cols = []
        for row in range(3):
            button = tkinter.Button(root, font=('Arial', 20), width=10, height=5
                                    , command=lambda r=row, c=column: place_symbole(r, c))
            button.grid(row=row, column=column)
            buttons_in_cols.append(button)
        buttons.append(buttons_in_cols)

#liste stockage
buttons = []
current_player = "X"
win = False

# création fenêtre
root = tkinter.Tk()

# personnalisation fenêtre
root.title("Morpion")
root.minsize(500, 500)

# appel de la fonction pour créer les boutons
draw_grid()

root.mainloop()
