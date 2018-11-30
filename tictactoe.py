game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
        ]


def board_draw():
    print("---  ---  ---")
    print("|   |   |   |")
    print("---  ---  ---")
    print("|   |   |   |")
    print("---  ---  ---")
    print("|   |   |   |")
    print("---  ---  ---")


def board_draw2():
    print(game[0])
    print(game[1])
    print(game[2])


def inputc():
    coord = input("Enter coordinates of position: ")
    coord.strip()
    a, b = coord.split()
    a.strip()
    b.strip()
    x = int(a[0])
    y = int(b)
    return [x, y]


def placer(a, b):  # a is list of coord, b is X or O
    print("YUHH")
    x = a[0] - 1
    y = a[1] - 1
    if game[x][y] == " ":
        game[x][y] = b
    else:
        print("Spot is taken")
        return False


def win_check(x):
    a = b = 0
    while a < 3:
        if game[a][0] == x and game[a][1] == x and game[a][2] == x:
            return True
        if game[0][a] == x and game[1][a] == x and game[2][a] == x:
            return True
        a += 1
    if game[0][0] == x and game[1][1] == x and game[2][2] == x:
        return True
    if game[2][0] == x and game[1][1] == x and game[0][2] == x:
        return True
    return False


def tie_checker():
    i = j = counter = 0
    while i < 3:
        while j < 3:
            if game[i][j] == "X" or game[i][j] == "O":
                counter += 1
            j += 1
        j = 0
        i += 1

    if counter >= 9:
        print("The game is tied!")
        return True
    return False


def program():
    print("Welcome to Tic Tac Toe deluxe®")
    print("******************************")
    print("X goes first")
    place = [0, 0]
    while True:
        print("Player 1, enter a coordinate to place X (x, y): ")
        place = inputc()
        if placer(place, "X") == False:
            break
        board_draw2()
        if tie_checker() == True:
            break
        if win_check("X") == True:
            print("Congrats! player 1 wins!")
            break
        print("Player 2, enter a coordinate to place Y (x, y): ")
        place = inputc()
        if placer(place, "O") == False:
            break
        board_draw2()
        if tie_checker() == True:
            break
        if win_check("O") == True:
            print("Congrats! player 2 wins!")
            break
    print("Goodbye")

program()
