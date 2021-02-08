import urllib.request, urllib.parse, urllib.error
import json


def solve(board):
    """
    solves sudoku board using backtracking
    board: 2d list of ints
    return: solution
    """

    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True

    for i in range(1,10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

def valid(board, pos, num):
    """
    returns if the attempted move is valid
    board: 2d list of ints
    pos: (row, col)
    num: int
    return: bool
    """

    #check row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #checks box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(board):
    """
    finds empty space in the board
    board: partially complete board
    return: (int, row) row col
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)

    return None

def print_board(board):
    '''
    prints the board
    board: 2d list of ints
    return: none
    '''
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")





while True:
    serviceurl = 'http://www.cs.utep.edu/cheon/ws/sudoku/new/'
    board = [[0 for i in range(1,10)] for j in range(1,10)]
    level = input("Enter level (1,2,3):")
    if len(level) < 1: break

    url = serviceurl + '?size=9?level=' + level

    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'response' not in js or js['response'] != True:
        print('==== Failure to Retrieve ====')
        print(data)
        continue

    for square in js['squares']:
        i = square["x"]
        j = square["y"]
        board[i][j] = square["value"]

    print_board(board)
    print()
    solve(board)
    print_board(board)
