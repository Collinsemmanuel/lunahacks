import pygame as pg
import time
import random
#creating the Game interface
pg.init()
display_height = 300
display_width = 400
display = pg.display.set_mode((display_width, display_height))
pg.display.set_caption("Snake Frenzy") #title

#In game colors 
yellow = (255, 255, 0)  
white = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

#Setting the speed of the snake.
clock = pg.time.Clock()
snake_speed = 10



#font and positioning of prompts on screen.
font = pg.font.SysFont(None, 20)
scorefont = pg.font.SysFont("comicsans", 20)
pausemenufont = pg.font.SysFont("comicsansms", 35)
def prompt(msg, color):
    text = font.render(msg, True, color)
    display.blit(text, [display_width/10, display_height/3])

def pauser(msg, color):
    text = pausemenufont.render(msg, True, color)
    display.blit(text, [30, 30])
#The score 
def scoreboard(score):
    text = scorefont.render("Score:"+str(score), True, blue)
    display.blit(text, (10, 10))

#The pausemenu
def pausemenu():
    paused = True 
    while paused == True:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_c:
                    paused = False 
                if event.key == pg.K_q:
                    pg.quit()
                    quit()

            pauser("Paused", red)
            prompt("C : Continue.\n Q : Quit.", black)
            
            pg.display.update()
            clock.tick(5)



#THE GAME.
snake_block = 10
def The_snake(snake_block, Afflength):
    for i in Afflength:
        pg.draw.rect(display, black, [i[0], i[1], snake_block, snake_block])

 


def gameloop():
    Game_over = False
    game_close = False
    score = 0
    
    #coordinates of the snake. 
    x1 = display_width/2
    y1 = display_height/2
    #Checking the score
    def scores(score):
        if x1 ==foodx and y1 == foody:
            score +=1 
        return score
    #For tracking changes of x1 and y1
    x1_change = 0
    y1_change = 0
    #Necessary lists 
    Afflength = [] #Alters position
    snakelength = 1
    
    #Generates random coordinates for the food.
    foodx = round(random.randrange(0, display_width - snake_block)/10.0)*10.0
    foody = round(random.randrange(0, display_height - snake_block)/10.0)*10.0

    while not Game_over:
        while game_close == True:
            display.fill(white)
            ans = ("Q : Quit\n N : New Game\n")
            prompt(ans, red)
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        Game_over = True
                        game_close = False 
                    if event.key == pg.K_n:
                        gameloop()

        
        

        for event in pg.event.get():
            #For exiting the application.
            if event.type == pg.QUIT:
                Game_over = True
            #Getting the snake to move.
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pg.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
                if event.key == pg.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pg.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pg.K_ESCAPE:
                    pausemenu()


        #Ending the game when snake reaches the boundaries of the display interface 
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        

        #Drawing the snake.
        x1 += x1_change
        y1 += y1_change
        display.fill(green) 
        head = []
        head.append(x1)
        head.append(y1)
        Afflength.append(head)
        #Ensures the snake is not too long
        if len(Afflength) > snakelength:
            del Afflength[0]

        #If snake's head touches the body
        for i in Afflength[:-1]:#':-1' all except the last is compared 
            if i == head:
                game_close = True
            

        The_snake(snake_block, Afflength)
        scoreboard(snakelength - 1)
        pg.display.update()
        

        #When head comes into contact with the food then,,
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block)/10.0)*10.0
            foody = round(random.randrange(0, display_height - snake_block)/10.0)*10.0
            
            snakelength += 1
            

        #drawing the food 
        pg.draw.rect(display, yellow, [foodx, foody, snake_block, snake_block])
        pg.display.update()
        clock.tick(snake_speed)#Difficulty
        
    

    prompt("YOU LOST", green)
    pg.display.update()
    time.sleep(2)#Delays the program before running next code 

    pg.quit()
    quit()

gameloop()