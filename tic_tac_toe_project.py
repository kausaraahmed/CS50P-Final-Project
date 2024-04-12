import tabulate
import os
from pyfiglet import Figlet

figlet =Figlet()
figlet.setFont(font="digital")

def main():
    ui_matrix = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    game_UI(ui_matrix)
    position_array = []
    
    for index in range(9):
        while True: 
            try:
                if is_even(index):
                    choice = int(input("[Player-1] Choose Position: "))
                else:
                    choice = int(input("[Player-2] Choose Position: "))
                
                if choice < 1 or choice > 9:
                    print("Invalid input. [Position must be between 1 and 9]")
                    continue
                
                if choice in position_array:
                    print("This position is taken.\n")
                else:
                    position_array.append(choice)
                    break
                
            except ValueError:
                print("Invalid input. [Position must be a number]")
        
        row, col = choice_position(choice)
        
        if is_even(index):
            ui_matrix[row][col] = 'X'
        else:
            ui_matrix[row][col] = 'O'
        
        game_UI(ui_matrix)
        
        if index >= 4:
            winner = found_winner(ui_matrix)
            if winner:
                win_player(winner)
                break
            elif index == 8:
                print(figlet.renderText("Match tie..\n"))
                
def is_even(index):
    return index % 2 == 0

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')

def game_UI(ui_matrix):
    clear_screen()
    print()
    print(tabulate.tabulate(ui_matrix, headers="", tablefmt="heavy_grid"))
    print()

def found_winner(ui_matrix):
    # Compare rows
    for i in range(3):
        if ui_matrix[i][0] == ui_matrix[i][1] == ui_matrix[i][2]:
            return ui_matrix[i][0]

    # Compare columns
    for i in range(3):
        if ui_matrix[0][i] == ui_matrix[1][i] == ui_matrix[2][i]:
            return ui_matrix[0][i]

    # Compare primary diagonal
    if ui_matrix[0][0] == ui_matrix[1][1] == ui_matrix[2][2]:
        return ui_matrix[0][0]

    # Compare secondary diagonal
    if ui_matrix[0][2] == ui_matrix[1][1] == ui_matrix[2][0]:
        return ui_matrix[0][2]

    return None

def win_player(player):
    if player == 'X':
        # print(figlet.renderText(("Player - 1 Wins ..\n").upper()))
        print(figlet.renderText("Winner: Player-1\n"))
    elif player == 'O':
        print(figlet.renderText("Winner: Player-2\n"))

def choice_position(a):
    pos_dict = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }
    return pos_dict.get(a, None)


if __name__ == "__main__":
    main()
