# A python implementation of the game CookC (that's supposed to be written in C but C is hard).
import keyboard as kb
# import CookLCD as lcd

"""
Makes a board out of a correctly-formatted input file
"""
def mkBoard(file):
    board = []
    for line in file:
        if line[0] == "#":
            pass
        else:
            board.append(list(line))
    return board

"""
Prints the current board to the screen
 """
def drawBoard():
    for item in BOARD:
        itemStr = "".join(item)
        print(itemStr)


# Spawns a new player at the specified location
def spawn():
    for item in BOARD:
        itemString = "".join(item)
        found = itemString.find("?")
        if found < 0:
            pass
        elif found >= 0:
            item[found] = "V"

"""
Get the location of the player
"""
def getLocation():
    found = -1
    playerSprites = ("<", "V", "^", ">")
    for item in BOARD:
        itemString = "".join(item)
        found = 0
        while found == 0:
            for sprite in playerSprites:
                found = itemString.find(sprite)
    return found


"""
Moves the player based on what direction code was given
Key: [0:left, 1:down, 2:up, 3:right]
"""
def move(direction):
    location = getLocation()
    if location < 0:
        raise IndexError("Player not found.")
    if direction == 0:
        pass
    if direction == 1:
        pass
    if direction == 2:
        pass
    if direction == 3:
        pass
    else:
        raise IndexError("Invalid direction.")

"""
The main loop of the program, handles keyboard input and player movement
"""
def gameLoop():
    running = True 
    while running:
        try:
            if kb.is_pressed("q"):
                print("Quitting game.")
                break
            elif kb.is_pressed("left"):
                print("left")
                continue
            elif kb.is_pressed("down"):
                print("down")
                continue
            elif kb.is_pressed("up"):
                print("up")
                continue
            elif kb.is_pressed("right"):
                print("right")
                continue
        except KeyboardInterrupt:
            print("Interrupted by user.")
            break
    print("Finished.")



boardFile = open("gameBoards/concessions.txt")
BOARD = mkBoard(boardFile)

# Runs the program
def main():
    drawBoard()
    # lcd.write("Board generated.")
    print()

    spawn()
    drawBoard()
    gameLoop()

main()
