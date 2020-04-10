# A python implementation of the game CookC (that's supposed to be written in C but C is hard).
import keyboard as kb

# Makes a board out of a correctly-formatted input file
def mkBoard(file):
    board = []
    for line in file:
        if line[0] == "#":
            pass
        else:
            board.append(list(line))
    return board


# Prints the currect board to the screen
def drawBoard():
    for item in BOARD:
        itemStr = ''.join(item)
        print(itemStr)


# Spawns a new player at the specified location
def spawn():
    index = 0
    for item in BOARD:
        itemString = ''.join(item)
        found = itemString.find("?")
        if found < 0:
            pass
        elif found >= 0:
            print("FOUND!")
            item[found] = "V"


boardFile = open("gameBoards/concessions.txt")
BOARD = mkBoard(boardFile)

# Runs the program
def main():
    drawBoard()
    print()
    spawn()
    drawBoard()

main()

# TODO When moving, only convert the two lines needed (start and end position) into lists that can be edited
