import pygame as py
import os
py.init()

win = py.display.set_mode((600,480))
py.display.set_caption("Sprite pygame direction movement")
folderPath_left = "Character_images_left"
folderPath_right = "Character_images_right"
myList_right = os.listdir(folderPath_right)
myList_left = os.listdir(folderPath_left)
#picture for rigth movement
movement_right=[]
for imPath in myList_right:
    movement_right.append(py.image.load(f'{folderPath_right}/{imPath}'))

#picture for left movement
movement_left=[]
for imPath in myList_left:
    movement_left.append(py.image.load(f'{folderPath_left}/{imPath}'))
    
bg = py.image.load('hacker.gif')
standing_position = py.image.load('r1.png')

x = 20; y = 100
width = 40; height = 100
velocity = 5

clock = py.time.Clock()

left = False
right = False
movement_count = 0

def Sprite_Window():
    global movement_count
    
    win.blit(bg,(1,1))  
    if movement_count + 1 >= 20:
        movement_count = 0
                                    
    if right:
        win.blit(movement_right[movement_count//4], (x,y))
        movement_count =movement_count+ 1
    elif left:  
        win.blit(movement_left[movement_count//4], (x,y))
        movement_count =movement_count + 1
    else:
        win.blit(standing_position, (x, y))
        movement_count = 0
        
    py.display.update() #to update the display screen
    
run = 1
while run:
    clock.tick(33) #this will manage the frame rate and provide more smoothness to the movement
    for event in py.event.get():
        if event.type == py.QUIT:
            run=0
    keys = py.key.get_pressed()
    
    if keys[py.K_RIGHT] and x < 480 - velocity - width: # to move to the end of the screen 
        x += velocity # for moving in the right direction
        right = True; left = False
    elif keys[py.K_LEFT] and x > velocity - width: # to move to the end of the screen
        x -= velocity # for moving in the left direction
        right = False; left = True    
    else: 
        left = False;right = False
        movement_count = 0
        
    Sprite_Window()     
py.quit()
