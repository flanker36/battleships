import random
###########
# CONFIGS
###########
battleship_length = 4
aircraft_length = 5
destroyer_length = 3
cb_width = 10
flags = ['yoko','tate']
count = 30

#######################
#GENERATE CHECKERBOARD
#######################
CheckerBoard = []
def generateChekerBoard():
    for i in range(cb_width):
        temp = []
        for j in range(cb_width):
            temp.append(0)
        CheckerBoard.append(temp)
#print(CheckerBoard)

#############
# UTILITIES
#############
def generateStartPoint():
    while True:
        startx = random.randint(0,cb_width-1)
        starty = random.randint(0,cb_width-1)
        if not CheckerBoard[startx][starty]:
            #print(startx,starty)
            break
    return {'x':startx,'y':starty}

def printCheckerBoard():
    for i in range(cb_width):
        temparray = []
        for j in range(cb_width):
                if not CheckerBoard[i][j]:
                    temparray.append(str(CheckerBoard[i][j]))
                elif CheckerBoard[i][j] == 'X':
                    temparray.append('X')
                else:
                    temparray.append('0')
        print(temparray)

def checkWin(shiplist):
    win = 1
    for ship in shiplist:
        if ship.length:
            win = 0
            break
    if(win):
        print('YOU WIN')
    return win

##########
# MODELS
##########
class Ship:
    def __init__(self):
        self.id = 0
        self.length = -1
        self.position = []

    def deploy(self):
        flag = random.sample(flags,1)[0]
        while True:
            #print(flag)
            startpoint = generateStartPoint()
            check = True
            if flag == 'tate':
                for i in range(self.length):
                    #print(i)
                    if startpoint['x']+i >= cb_width-1 or CheckerBoard[startpoint['x']+i][startpoint['y']] :
                        check = False
                        break
                if check:
                    for i in range(self.length):
                        CheckerBoard[startpoint['x'] + i][startpoint['y']] = self.id
                    break
            else:
                for i in range(self.length):
                    #print(i)
                    if startpoint['y']+i+i >= cb_width-1 or CheckerBoard[startpoint['x']][startpoint['y']+i] :
                        check = False
                        break
                if check:
                    for i in range(self.length):
                        CheckerBoard[startpoint['x']][startpoint['y']+i] = self.id
                    break
    def isHit(self):
        print(self.id + ' is hit.')
        self.length -= 1
        if not self.length:
            self.sink()

    def sink(self):
        print(self.id + ' is sanked.')

class Battleship(Ship):
    def __init__(self,id,length = battleship_length):
        self.id = id
        self.length = length


class Aircraft(Ship):
    def __init__(self,id,length = aircraft_length):
        self.id = id
        self.length = length

class Destroyer(Ship):
    def __init__(self,id,length = destroyer_length):
        self.id = id
        self.length = length

################
# BATTLE
################
def fire(x,y):
    if not CheckerBoard[x][y]:
        print('MISS!')
        CheckerBoard[x][y] = 'X'
        return None
    elif CheckerBoard[x][y] == 'X':
        print('You have hit here. Try another place!')
        return None
    else:
        id = CheckerBoard[x][y]
        CheckerBoard[x][y] = 'X'
        return id

##############
# THIS IS GAME
##############
print('Generating chekerboard ...')
generateChekerBoard()

print('Generating ships ...')
ships = []
for i in range(1,4):
    newship = Battleship(str(i))
    newship.deploy()
    ships.append(newship)


while count:
    if(checkWin(ships)):
        break

    print('You still have '+ str(count) +' times.')
    printCheckerBoard()
    ainput = input("Input the position you want to fire, split it by space button : \n")
    ainput = ainput.split(' ')
    try:
        x = int(ainput[0])-1
        y = int(ainput[1])-1
        result = fire(x,y)
        if result:
            ships[int(result)-1].isHit()
        count -= 1
    except:
        print("Something wrong with your input, try again!")

print('GAME OVER!')







