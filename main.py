from os import system
from logo import start_screen

board_dict = {
    "a": ["|   |", "|   |", "|   |"],
    "b": [" ", " ", " "],
    "c": ["|   |", "|   |", "|   |"],
}

board_pos = {
    1: ("a", 1), 2: ("b", 1), 3: ("c", 1),
    4: ("a", 2), 5: ("b", 2), 6: ("c", 2),
    7: ("a", 3), 8: ("b", 3), 9: ("c", 3)
    }

WINNING_POS = [[1, 4, 7],
               [2, 5, 8],
               [3, 6, 9],
               [1, 5, 9],
               [3, 5, 7],
               [1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]
               ]

####################Game Board######################


def board_func():
    """this function is the game board which used to demonstrate the updated board of the game"""

    print("-" * 2 + "A" + "-" * 3 + "B" + "-" * 3 + "C" + "-" * 2)
    for i in range(3):
        print("-" * 13)
        print(board_dict["a"][i], board_dict["b"][i], board_dict["c"][i])
    print("-" * 13)


####################Game Dynamic###################

def player_1():
    col = input('Player "X": Select column A,B or C: ').lower()
    row = input('Player "X": Select row number 1,2 or 3: ')
    return col, int(row), "X"


def player_2():
    col = input('Player "O": Select column A,B or C: ').lower()
    row = input('Player "O": Select row number 1,2 or 3: ')
    return col, int(row), "O"


def player_input(col, row, p_input):
    """This function is the dynamic for the game with user inputs warning if
    they tried diffrent inputs than expected """

    def board_filler():
        for i in range(3):
            if col == "a" or col == "c":
                board_dict[col][row - 1] = "| " + p_input + " |"
            elif col == "b":
                board_dict[col][row - 1] = p_input
    try:
        board_filler()
        if col != "a" or col != "b" or col != "c":
            print("Invalid Column input.\nPlease chose column A, B or C error 1")
            board_filler()
    except IndexError:
        print("Invalid Row input. \nplease put number not more than 3. error 2")
        board_filler()



###game rules and identifying the winner

def loc(col, row, position_list):
    ###this function is to convert the position tuple into location number from 1 - 9
    for key, value in board_pos.items():
        if (col, row) == value:
            position = int(key)
            if position not in position_list:
                return position
            else:
                return f"Position had been occupied."


def check_pos(player1, player2):
    ##this function defines the winner if the position taken matches one of the winning positions
    sorted_position_p1 = sorted(player1)
    sorted_position_p2 = sorted(player2)
    for win_pos in WINNING_POS:
        if sorted(win_pos) == sorted_position_p1:
            print("Player X won")
            return True
        elif sorted(win_pos) == sorted_position_p2:
            print("Player O won")
            return True
            # print(win_pos, sorted_pos)


#print(loc("a", 3))a


#####################

game_on = True
# board_func()


player1_pos = []
player2_pos = []

while game_on:
    print(start_screen)
    occupied_pos = []
    winning_positions = True

    while winning_positions:

        if not check_pos(player1_pos, player2_pos):

            board_func()
            first_p = player_1()
            player_input(first_p[0], first_p[1], first_p[2])
            player1_pos.append(loc(first_p[0], int(first_p[1]),occupied_pos))

        if not check_pos(player1_pos, player2_pos):
            board_func()
            second_p = player_2()
            player_input(second_p[0], second_p[1], second_p[2])
            player2_pos.append(loc(second_p[0], int(second_p[1]), occupied_pos))

        else:
            winning_positions = False

        occupied_pos = player1_pos + player2_pos


    game_on = False



    # print(occupied_pos)
    #
    # print("p1 pos: ", player1_pos)
    # print("p2 pos: ", player2_pos)
    system('cls')

board_func()
print("You are the Winner!!!!!")
