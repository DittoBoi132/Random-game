import time
import pygame
import sys
import random
from pygame.locals import *
pygame.init()

#screen
screen = pygame.display.set_mode((800,600),RESIZABLE)
pygame.display.set_caption("test")

#colours
white = (255,255,255)
green = (0, 255, 0)
yellow = (255,255,0)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
cyan = (0,255,255)
pink = (255,153,255)
orange = (255,143,0)
purple = (255, 0, 255)
brown = (141, 111, 100)
darkBrown = (91, 74, 68)

#variables
score = 0
lives = 1
option = True
clock = pygame.time.Clock()
    
#game over
def gameOver():
    global option
    if lives == 0:
        screen.fill(black)
        font = pygame.font.SysFont("Times_new_roman", 48)
        txtsurf = font.render("GAME OVER", True, white)
        screen.blit(txtsurf, (screen.get_width() //2  - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(3000)

        while option:
            rect1 = text5.get_rect(topleft = (screen.get_width() //2 - text5.get_width() // 2, screen.get_height() //2 + text4.get_height()))
            rect2 = text6.get_rect(topleft = (screen.get_width() //2 - text6.get_width() // 2, screen.get_height() //2 - text3.get_height()))
            screen.fill(black)
            screen.blit(text5, rect1)
            pygame.draw.rect(screen, (darkBrown),rect1, 5)
            screen.blit(text6, rect2)
            pygame.draw.rect(screen, (darkBrown),rect2, 5)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rect1.collidepoint(event.pos):
                        game()
                        option = False
                    if rect2.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()

#display score
def displayScore():
    disScore = f"Score: {score}"
    font = pygame.font.SysFont("Times_new_roman", 12)
    txtsurf = font.render(disScore, True, white)
    screen.blit(txtsurf, (20,35))
    pygame.display.update()

#display lives
def displayLives():
    disLives = f"Lives: {lives}"
    font = pygame.font.SysFont("Times_new_roman", 12)
    txtsurf = font.render(disLives, True, white)
    screen.blit(txtsurf, (20,20))
    pygame.display.update()

#display level
def displayLevel():
    disLevel = f"Level: {level}"
    font = pygame.font.SysFont("Times_new_roman", 12)
    txtsurf = font.render(disLevel, True, white)
    screen.blit(txtsurf, (20,5))
    pygame.display.update()

#random lives
def lifeChoose():
    global lives
    for i in range(40):
        lives = random.randrange(1,120)
        disLives = f"Lives: {lives}"
        font = pygame.font.SysFont("Times_new_roman", 72)
        txtsurf = font.render(disLives, True, white)
        screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        screen.fill(black)
        clock.tick(20)
    lives = random.randrange(1,5)
    disLives = f"Lives: {lives}"
    font = pygame.font.SysFont("Times_new_roman", 72)
    txtsurf = font.render(disLives, True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    print(lives)
        
#display level, start
def levelStart():
    disLevel = f"Level {level}"
    font = pygame.font.SysFont("Times_new_roman", 72)
    txtsurf = font.render(disLevel, True, white)
    txt = screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    strat = True
    while strat:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if txt.collidepoint(event.pos):
                    strat = False

#loose life
def looseLife():
    global lives
    screen.fill(black)
    font = pygame.font.SysFont("Times_new_roman", 72)
    txtsurf = font.render("OOPS!", True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.fill(black)
    disLives = f"Lives: {lives}"
    font = pygame.font.SysFont("Times_new_roman", 72)
    txtsurf = font.render(disLives, True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(1000)
    screen.fill(black)
    lives -= 1
    disLives = f"Lives: {lives}"
    font = pygame.font.SysFont("Times_new_roman", 72)
    txtsurf = font.render(disLives, True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)
    gameOver()

#gain lives
def lifeGain(num):
    global lives
    num2 = random.randrange(0, 400)
    if num2 == 23:
        looseLife()
        looseLife()
        num = -2
    print("lives gained =", num-1)
    if num == "1" or "2":
        screen.fill(black)
        disLives = f"Lives: {lives}"
        font = pygame.font.SysFont("Times_new_roman", 72)
        txtsurf = font.render(disLives, True, white)
        screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(1000)
        if num == 1:
            lives += 0
        elif num == 2:
            lives += 1
            screen.fill(black)
            disLives = f"Lives: {lives}"
            font = pygame.font.SysFont("Times_new_roman", 72)
            txtsurf = font.render(disLives, True, white)
            screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(2000)
            screen.fill(black)
    if num == 0:
        looseLife()
    
    displayLevel()
    displayLives()
    displayScore()
    pygame.display.update()
    
#gain score
def scoreGain(num):
    global score
    num2 = random.randrange(1,100)
    if num2 == 23:
        for i in range(0,num):
            score -= 1
            screen.fill(black)
            displayLevel()
            displayLives()
            displayScore()
            clock.tick(20)
    elif num2 == 24:
            for i in range(0,200):
                score -= 1
                screen.fill(black)
                displayLevel()
                displayLives()
                displayScore()
                clock.tick(20)
    else:
        for i in range(0,num):
            score += 1
            screen.fill(black)
            displayLevel()
            displayLives()
            displayScore()
            clock.tick(20)
    print("odds =", num2)
    print("score gained =", num)
    print("total score =", score)
    pygame.time.delay(2000)

#win
def win():
    global option
    screen.fill(black)
    font = pygame.font.SysFont("Times_new_roman", 48)
    txtsurf = font.render("YOU WIN", True, white)
    screen.blit(txtsurf,(screen.get_width() //2 - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(3000)

    while option:
        rect1 = text5.get_rect(topleft = (screen.get_width() //2 - text5.get_width() // 2, screen.get_height() //2 + text4.get_height()))
        rect2 = text6.get_rect(topleft = (screen.get_width() //2 - text6.get_width() // 2, screen.get_height() //2 - text3.get_height()))
        screen.fill(black)
        screen.blit(text5, rect1)
        pygame.draw.rect(screen, (darkBrown),rect1, 5)
        screen.blit(text6, rect2)
        pygame.draw.rect(screen, (darkBrown),rect2, 5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    game()
                    option = False
                if rect2.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

#menu
font = pygame.font.SysFont("Times_new_roman", 48)

def menu():
    menu = True
    while menu:
        rect1 = text1.get_rect(topleft = (screen.get_width() //2 - text1.get_width() // 2, screen.get_height() //2 + text1.get_height()))
        rect2 = text2.get_rect(topleft = (screen.get_width() //2 - text2.get_width() // 2, screen.get_height() //2 - text2.get_height()))
        screen.fill(black)
        screen.blit(text1, rect1)
        pygame.draw.rect(screen, (darkBrown),rect1, 5)
        screen.blit(text2, rect2)
        pygame.draw.rect(screen, (darkBrown),rect2, 5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                    running = False
                    menu = False
                if rect2.collidepoint(event.pos):
                    menu = False

#first
def first1():
    screen.fill(black)
    levelStart()
    pygame.time.delay(250)
    if level == "1":
        lifeChoose()
        pygame.time.delay(2000)
        test()
        screen.fill(black)
        displayLevel()
        displayLives()
        displayScore()
        pygame.display.update()
    test()
    screen.fill(black)
    displayLevel()
    displayLives()
    displayScore()
    pygame.display.update()
    pygame.time.delay(2000)
    first = False

def levl():
    global lvl
    while lvl:
        rect1 = text4.get_rect(topleft = (screen.get_width() //2 - text4.get_width() // 2, screen.get_height() //2 + text4.get_height()))
        rect2 = text3.get_rect(topleft = (screen.get_width() //2 - text3.get_width() // 2, screen.get_height() //2 - text3.get_height()))
        screen.fill(black)
        screen.blit(text4, rect1)
        pygame.draw.rect(screen, (darkBrown),rect1, 5)
        screen.blit(text3, rect2)
        pygame.draw.rect(screen, (darkBrown),rect2, 5)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(event.pos):
                    lifeGain(random.randrange(0,3))
                    lvl = False
                if rect2.collidepoint(event.pos):
                    scoreGain(random.randrange(0,200))
                    lifeGain(random.randrange(0,2))
                    lvl = False
                    
    screen.fill(black)
    displayLevel()
    displayLives()
    displayScore()
    pygame.display.update()
    test()
    lvl = True
    first = True
    
#tests
def test():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                menu()
            if event.key == K_SPACE:
                looseLife()
            if event.key == K_RETURN:
                scoreGain(random.randrange(0,200))

text1 = font.render("EXIT", True, white)
text2 = font.render("CONTINUE", True, white)
text3 = font.render("Score", True, white)
text4 = font.render("Lives", True, white)
text5 = font.render("RESTART", True, white)
text6 = font.render("QUIT", True, white)

#game
def game():
    global score
    global lives
    global level
    global lvl
    global cL
    
    #start
    starting = True
    while starting:
        screen.fill(black)
        rect = pygame.draw.rect(screen, darkBrown, pygame.Rect(screen.get_width() //2 - 150,screen.get_height() //2 - 50, 300, 100),10)
        font = pygame.font.SysFont("Times_new_roman", 72)
        txtsurf = font.render("welcome", True, white)
        screen.blit(txtsurf,(screen.get_width() //2  - txtsurf.get_width() // 2, screen.get_height() //2  - txtsurf.get_height() // 2))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect.collidepoint(event.pos):
                    starting = False

    #start variables
    score = 0
    lives = 1
    running = True
    cL = True
    pause = False
    lvl = True
    level  = "1"
    screen.fill(black)
    displayLevel()
    displayLives()
    displayScore()
    pygame.display.update()

    if running:
        first = True
    
        #level 1
        while cL:
            level = "1"
            if first:
                first1()

            levl()
            cL = False

        #level 2
        cL = True
        while cL:
            level = "2"
            if first:
                first1()

            levl()
            cL = False
        
        #level 3
        cL = True        
        while cL:
            level = "3"
            if first:
                first1()

            levl()
            cL = False
    
        #level 4
        cL = True
        while cL:
            level = "4"
            if first:
                first1()
            
            levl()
            cL = False

        #level 5
        cL = True
        while cL:
            level = "5"
            if first:
                first1()
            
            levl()
            cL = False

        #level 6
        cL = True
        while cL:
            level = "6"
            if first:
                first1()
            
            levl()
            cL = False
        
        pygame.display.flip()   
        clock.tick(50)

    if score >= 400:
        win()
    else:
        lives = 0
        gameOver()
        
game()
    
