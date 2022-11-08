string = [" " for _ in range(9)]
player_turn = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
turn_count, x, y = 0, 0, 0
WIN = [list("OOO"), list("XXX")]
ROW_0, ROW_1, ROW_2, COLUMN_0, COLUMN_1, COLUMN_2, CROSS_DOWN, CROSS_UP = (str(),) * 8


def update_fields():
    global ROW_0, ROW_1, ROW_2, COLUMN_0, COLUMN_1, COLUMN_2, CROSS_DOWN, CROSS_UP
    ROW_0 = string[0:3]
    ROW_1 = string[3:6]
    ROW_2 = string[6:9]
    COLUMN_0 = string[0:7:3]
    COLUMN_1 = string[1:8:3]
    COLUMN_2 = string[2:9:3]
    CROSS_DOWN = string[0:9:4]
    CROSS_UP = string[2:7:2]


def grid():
    print("---------")
    print("|", string[0], string[1], string[2], "|")
    print("|", string[3], string[4], string[5], "|")
    print("|", string[6], string[7], string[8], "|")
    print("---------")


def check_win():
    update_fields()
    fields = [ROW_0, ROW_1, ROW_2, COLUMN_0, COLUMN_1, COLUMN_2, CROSS_DOWN, CROSS_UP]
    if abs(string.count("X") - string.count("O")) > 1:
        print("Impossible")
    else:
        win = any([i for i in fields if i in WIN])

        if win:
            print(player_turn[turn_count - 1], "wins")
            return win
        elif string.count(" ") == 0:
            print("Draw")
            return True
    return False


# determine which location on grid is specified through user input
def coordinate_mapping(m, n):
    grid_map = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    return grid_map[m - 1][n - 1]


# check if certain cell is empty or occupied
def check_if_empty(current_pos):
    global string

    if string[current_pos] == " ":
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False


# set location of symbol in array
def set_location(current_pos):
    global string, player_turn, turn_count
    string = string[0:current_pos] + list(player_turn[turn_count]) + string[current_pos + 1:]
    next_turn()


# asks for user input
def user_input():
    global y
    global x

    coords = input("Enter the coordinates: ")

    try:
        y, x = coords.split()
    except ValueError:
        print("You should enter numbers!")
        return

    try:
        int(y) and int(x)
    except ValueError:
        print("You should enter numbers!")
        return

    if (int(x) > 3) or (int(y) > 3) or (int(x) < 1) or (int(y) < 1):
        print("Coordinates should be from 1 to 3!")
        return

    # position holds the spot where the user input should be placed on grid
    position = coordinate_mapping(int(y), int(x))
    is_empty = check_if_empty(position)
    if is_empty:
        set_location(position)
    else:
        user_input()


def next_turn():
    global turn_count
    turn_count += 1


if __name__ == "__main__":
    while True:
        grid()
        user_input()
        if check_win():
            grid()
            break
