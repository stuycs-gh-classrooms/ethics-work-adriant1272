board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def printBoard():
    ret = "\n"
    for i in range(4):
        if i < 3:
            ret += str(i) + " "
            for j in range(3):
                if j==0 or j==1:
                    ret += f'{board[i][j]} | '
                else:
                    ret+=board[i][j]
        else:
            ret += "  "
            for j in range(3):
                ret += str(j) + "   "
        ret += "\n"
    print(ret)


def addChar(x, y, char):
    if  x < 0 or x > 2 or y < 0 or y > 2 or  board[x][y] != " ":
        print("Invalid Coordinate")
        return False
    else:
        board[x][y] = char
        return True

addChar(0, 1, "O")
addChar(0, 2, "X")
printBoard()

def runGame():
    winner = ""
    player = 0
    goodTurn = True
    print("dis is da game")
    while winner == "":
        if goodTurn:
            printBoard()
            print(f'Player {player+1} is up!')
        else:
            print(f'Try Again, Player {player+1}')
        xCor = int(input("Enter desired X Coordinate: "))
        yCor = int(input("Enter desired Y Coordinate: "))
        
        if player==0:
            goodTurn = addChar(yCor, xCor, "X")
        if player==1:
            goodTurn = addChar(yCor, xCor, "Y")
        
        if goodTurn:
            player += 1
            player%2
        
        
runGame()
    
