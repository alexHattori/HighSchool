import pygame
import random
import math
import time

background_color = (0,0,255)
colorInt = 0;
forward = True

(width, height) = (1000, 700)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('You guys all suck')
running = True
pygame.init()
myfont = pygame.font.SysFont("monospace", 72)
state = 0
selected = 0

numRows = 3
numCols = 3
board = [[0 for i in xrange(3)] for i in xrange(3)]

myTurn = False#1==random.randint(0,1)
turn = 1
compFirst = False

if(not myTurn):
    compFirst = True
class X():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def display(self):
        pygame.draw.line(screen,(200,0,0),(self.x-117,self.y-117),(self.x+117,self.y+117),10)
        pygame.draw.line(screen,(200,0,0),(self.x-117,self.y+117),(self.x+117,self.y-117),10)
class O():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def display(self):
        pygame.draw.circle(screen,(100,50,255),(self.x,self.y),100,10)
        
class Square():
    def __init__(self,col,row):
        self.col = col
        self.row = row
        self.val = 0
        self.contactRect = pygame.Rect(150+self.col+1*233,self.row+1*233,233,233)
        self.contactRectColor = (255,255,255)
    def update(self):
        self.val = board[self.col][self.row]
        self.contactRect = pygame.Rect(150+self.col*233,self.row*233,233,233)
        (mouseX, mouseY) = pygame.mouse.get_pos()
        mouseContactRect = pygame.Rect(mouseX,mouseY,1,1)
        if self.contactRect.colliderect(mouseContactRect):
            self.contactRectColor = (255,0,0)
        else:
            self.contactRectColor = (255,255,255)
    def display(self):
        if self.val == 1:
            occupant = O(150+self.col*(233)+117,self.row*233+117);
            occupant.display()
        elif self.val == 2:
            occupant = X(150+self.col*(233)+117,self.row*233+117);
            occupant.display()
        if(self.contactRectColor == (255,0,0)):
            pygame.draw.rect(screen,self.contactRectColor,self.contactRect,5)
def displayBoard():
    pygame.draw.line(screen,(255,255,255),(150,0),(150,700),10)
    pygame.draw.line(screen,(255,255,255),(150+233,0),(150+233,700),10)
    pygame.draw.line(screen,(255,255,255),(150+466,0),(150+466,700),10)
    pygame.draw.line(screen,(255,255,255),(150+699,0),(150+699,700),10)
    pygame.draw.line(screen,(255,255,255),(150,0),(150+699,0),10)
    pygame.draw.line(screen,(255,255,255),(150,233),(150+699,233),10)
    pygame.draw.line(screen,(255,255,255),(150,466),(150+699,466),10)
    pygame.draw.line(screen,(255,255,255),(150,699),(150+699,699),10)

def win():
    if board[0] == [0,2,2] or (board[0][0] == 0 and board[1][0] == 2 and board[2][0] == 2) or (board[0][0] == 0 and board[1][1] == 2 and board[2][2] == 2):
        board[0][0] = 2
        return True
    elif board[1] == [0,2,2] or (board[0][0] == 2 and board[1][0] == 0 and board[2][0] == 2):
        board[1][0] = 2
        return True
    elif board[2] == [0,2,2] or (board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 0) or (board[2][0] == 0 and board[1][1] == 2 and board[0][2] == 2):
        board[2][0] = 2
        return True
    elif board[0] == [2,0,2] or (board[0][1] == 0 and board[1][1] == 2 and board[2][1] == 2):
        board[0][1] = 2
        return True
    elif board[1] == [2,0,2] or (board[0][1] == 2 and board[1][1] == 0 and board[2][1] == 2) or (board[0][0] == 2 and board[1][1] == 0 and board[2][2] == 2) or (board[0][2] == 2 and board[1][1] == 0 and board[2][0] == 2):
        board[1][1] = 2
        return True
    elif board[2] == [2,0,2] or (board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 0):
        board[2][1] = 2
        return True
    elif board[0] == [2,2,0] or (board[0][2] == 0 and board[1][2] == 2 and board[2][2] == 2) or (board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 0):
        board[0][2] = 2
        return True
    elif board[1] == [2,2,0] or (board[0][2] == 2 and board[1][2] == 0 and board[2][2] == 2):
        board[1][2] = 2
        return True
    elif board[2] == [2,2,0] or (board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 0) or (board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 0):
        board[2][2] = 2
        return True
def block():
    if board[0] == [0,1,1] or (board[0][0] == 0 and board[1][0] == 1 and board[2][0] == 1) or (board[0][0] == 0 and board[1][1] == 1 and board[2][2] == 1):
        board[0][0] = 2
        return True
    elif board[1] == [0,1,1] or (board[0][0] == 1 and board[1][0] == 0 and board[2][0] == 1):
        board[1][0] = 2
        return True
    elif board[2] == [0,1,1] or (board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 0) or (board[2][0] == 0 and board[2][1] == 1 and board[2][2] == 1) or (board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 0):
        board[2][0] = 2
        return True
    elif board[0] == [1,0,1] or (board[0][1] == 0 and board[1][1] == 1 and board[2][1] == 1):
        board[0][1] = 2
        return True
    elif board[1] == [1,0,1] or (board[0][1] == 1 and board[1][1] == 0 and board[2][1] == 1) or (board[0][0] == 1 and board[1][1] == 0 and board[2][2] == 1) or (board[0][2] == 1 and board[1][1] == 0 and board[2][0] == 1):
        board[1][1] = 2
        return True
    elif board[2] == [1,0,1] or (board[2][0] == 1 and board[2][1] == 0 and board[2][2] == 1) or (board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 0):
        board[2][1] = 2
        return True
    elif board[0] == [1,1,0] or (board[0][2] == 0 and board[1][2] == 1 and board[2][2] == 1) or (board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 0):
        board[0][2] = 2
        return True
    elif board[1] == [1,1,0] or (board[0][2] == 1 and board[1][2] == 0 and board[2][2] == 1):
        board[1][2] = 2
        return True
    elif board[2] == [1,1,0] or (board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 0) or (board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 0):
        board[2][2] = 2
        return True

def smartGuess():
    if compFirst:
        if turn == 1:
            board[0][2] = 2
            return True
        elif turn == 2 and (board[0][1] == 1 or board[1][0] == 1 or board[2][0] or board[2][1]):
            board[2][2] = 2
            return True
        elif turn == 2 and (board[0][0] == 1 or board[1][1] == 1 or board[2][2]):
            board[2][0] = 2
            return True
        elif turn == 2 and (board[1][2] == 1):
            board[0][0] = 2
            return True
        elif turn == 3 and (board[2][2] == 2 and board[0][2] and board[2][0] == 0 and board[0][1] == 1):
            board[2][0] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[2][0] == 2 and board[0][0] == 1 and board[2][2] == 0):
            board[2][2] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[2][2] == 2 and board[1][0] == 1 and board[1][1] == 0):
            board[1][1] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[2][2] == 2 and board[2][0] == 1 and board[0][0] == 0):
            board[0][0] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[0][0] == 2 and board[1][2] == 1 and board[2][0] == 0):
            board[2][0] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[2][0] == 2 and board[2][2] == 1 and board[0][0] == 0):
            board[0][0] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[2][2] == 2 and board[2][1] == 1 and board[0][0] == 0):
            board[0][0] = 2
            return True
        elif turn == 3 and (board[0][2] == 2 and board[2][0] == 2 and board[1][1] == 1):
            if(board[0][0] == 1 and board[2][2] == 0):
                board[2][2] = 2
                return True
            elif(board[2][2] == 1 and board[0][0] == 0):
                board[0][0] = 2
                return True 
        else:
            return False
    else:
        if turn == 2 and (board[0][0] == 1 or board[0][2] == 1 or board[2][0] == 1 or board[2][2] == 1):
            board[1][1] = 2
            return True
        elif turn == 3 and (board[0][2] == 1 and board[2][0] == 1 and board[1][2] == 0):
            board[1][2] = 2
            return True
        elif turn == 3 and (board[0][0] == 1 and board[2][2] == 1 and board[1][2] == 0):
            board[1][2] = 2
            return True
        elif turn == 2 and (board[1][0] == 1 or board[0][1] == 1 or board[1][2] == 1 or board[2][1] == 1):
            board[1][1] = 2
            return True
        elif turn == 3 and (board[1][0] == 1 and board[0][1] == 1 and board[0][0] == 0):
            board[0][0] = 2
            return True
        elif turn == 3 and (board[1][0] == 1 and board[2][1] == 1 and board[2][0] == 0):
            board[2][0] = 2
            return True
        elif turn == 3 and (board[1][2] == 1 and board[2][1] == 1 and board[2][2] == 0):
            board[2][2] = 2
            return True
        elif turn == 3 and (board[0][1] == 1 and board[1][2] == 1 and board[0][2] == 0):
            board[0][2] = 2
            return True
        elif turn == 2 and (board[1][1] == 1 and board[2][2] == 0):
            board[2][2] = 2
            return True
        elif turn == 3 and (board[1][1] == 1 and board[2][2] == 2 and board[0][2] == 0):
            board[0][2] = 2
            return True
        
        elif turn == 3 and (board[0][0] == 1 or board[2][0] == 1) and (board[0][1] == 1 or board[2][1] == 1) and board[1][0] == 0:
            board[1][0] = 2
            return True
        elif turn == 3 and (board[2][0] == 1 or board[2][2] == 1) and (board[1][0] == 1 or board[1][2] == 1) and board[2][1] == 0:
            board[2][1] = 2
            return True
        elif turn == 3 and (board[0][2] == 1 or board[2][2] == 1) and (board[0][1] == 1 or board[2][1] == 1) and board[1][2] == 0:
            board[1][2] = 2
            return True
        elif turn == 3 and (board[0][0] == 1 or board[0][2] == 1) and (board[1][0] == 1 or board[1][2] == 1) and board[0][1] == 0:
            board[0][1] = 2
            return True
        
        elif turn == 4 and (board[0][0] == 1 or board[2][0] == 1) and (board[0][1] == 1 or board[2][1] == 1) and board[0][2] == 0 and board[1][0] == 2:
            board[0][2] = 2
            return True
        elif turn == 4 and (board[2][0] == 1 or board[2][2] == 1) and (board[1][0] == 1 or board[1][2] == 1) and board[0][0] == 0 and board[2][1] == 2:
            board[0][0] = 2
            return True
        elif turn == 4 and (board[0][2] == 1 or board[2][2] == 1) and (board[0][1] == 1 or board[2][1] == 1) and board[2][0] == 0 and board[1][2] == 2:
            board[2][0] = 2
            return True
        elif turn == 4 and (board[0][0] == 1 or board[0][2] == 1) and (board[1][0] == 1 or board[1][2] == 1) and board[2][2] == 0 and board[0][1] == 2:
            board[2][2] = 2
            return True
        else:
            return False
    return False
def computerGuess():
    done = False
    if(not win()):
        if(not block()):
            if(not smartGuess()):
                while(not done):
                    col = random.randint(0,2)
                    row = random.randint(0,2)
                    if board[col][row] == 0:
                        board[col][row] = 2
                        done = True
def testIfWinner():
    winner = ""
    if board[0] == [1,1,1] or board[1] == [1,1,1] or board[2] == [1,1,1]:
        return 1
    elif board[0] == [2,2,2] or board[1] == [2,2,2] or board[2] == [2,2,2]:
        return 2
    
    elif board[0][0] == 1 and board[1][0] == 1 and board[2][0] == 1:
        return 1
    elif board[0][1] == 1 and board[1][1] == 1 and board[2][1] == 1:
        return 1
    elif board[0][2] == 1 and board[1][2] == 1 and board[2][2] == 1:
        return 1
    
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        return 1
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        return 1
    
    elif board[0][0] == 2 and board[1][0] == 2 and board[2][0] == 2:
        return 2
    elif board[0][1] == 2 and board[1][1] == 2 and board[2][1] == 2:
        return 2
    elif board[0][2] == 2 and board[1][2] == 2 and board[2][2] == 2:
        return 2
    
    elif board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2:
        return 2
    elif board[0][2] == 2 and board[1][1] == 2 and board[2][0] == 2:
        return 2
    
    elif board[0][0] != 0 and board[0][1] !=0 and board[0][2] !=0 and board[1][0] != 0 and board[1][1] !=0 and board[1][2] !=0 and board[2][0] != 0 and board[2][1] !=0 and board[2][2] !=0:
        return 3
    return 0
    
square1 = Square(0,0)
square2 = Square(0,1)
square3 = Square(0,2)
square4 = Square(1,0)
square5 = Square(1,1)
square6 = Square(1,2)
square7 = Square(2,0)
square8 = Square(2,1)
square9 = Square(2,2)

squares = [square1,square2,square3,square4,square5,square6,square7,square8,square9]

while running:
    time.sleep(0.01)
    screen.fill(background_color)
    if(forward):
        colorInt+=2
    else:
        colorInt-=2
    if(colorInt==254 or colorInt==0):
        forward = not(forward)
    background_color = (100,colorInt,100)
    if state == 0:
        options = ["Start"]
        labels = []
        selectedColor = (0,255,0)
        otherColor = (255,0,0)
        if pygame.key.get_pressed()[pygame.K_UP] != 0:
            if(selected > 0):
                selected -= 1
            else:
                selected = len(options)-1
        elif pygame.key.get_pressed()[pygame.K_DOWN] != 0:
            if(selected == len(options)-1):
                selected = 0
            else:
                selected += 1
        elif pygame.key.get_pressed()[pygame.K_RETURN] != 0:
            state = 1
        for a in range(0,len(options)):
            if(a==selected):
                label = myfont.render(options[a], 10,selectedColor)
            else:
                label = myfont.render(options[a], 10,otherColor)
            screen.blit(label, (400,a*300 + 400))     
    elif state == 1:
        displayBoard()
        for a in squares:
            a.update()
            a.display()
        if(not myTurn and testIfWinner()==0):
            computerGuess()
            myTurn = True
        if(testIfWinner()>0):
            state = 2
    elif state == 2:
        finish = testIfWinner()
        if finish == 2:
            dlabel = myfont.render('Get Rekt',20,(0,255,100),(255,255,255))
        elif finish == 3:
            dlabel = myfont.render('Draw',10,(0,0,0))
        elif finish == 1:
            dlabel = myfont.render('How?',10,(0,0,0))
        displayBoard()
        for a in squares:
            a.update()
            a.display()
        screen.blit(dlabel,(400,300))
        pygame.display.flip()
        screen.blit(dlabel,(400,300))
        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_SPACE] != 0:
            board = [[0 for i in xrange(3)] for i in xrange(3)]
            im = pygame.image.load('Shrek.png')
            img = pygame.transform.scale(im,(250,250))
            state = 1
            myTurn = 1==random.randint(0,1)
            turn = 1
            compFirst = False
            if(not myTurn):
                compFirst = True
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.display.quit()
        elif event.type == pygame.MOUSEBUTTONUP:
            for s in squares:
                if s.contactRectColor == (255,0,0) and s.val == 0 and myTurn == True and testIfWinner() == 0:
                    board[s.col][s.row] = 1
                    myTurn = False
                    turn+=1
                    break
