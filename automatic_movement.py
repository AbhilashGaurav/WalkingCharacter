import pygame as py
import os
win = py.display.set_mode((200,280)) #the width and height of our screen
py.display.set_caption("Sprite pygame movement")
FPS = 30 #Frames per second
 
class Sprite_Window(py.sprite.Sprite):
    def __init__(self):
        super(Sprite_Window, self).__init__()
        folderPath = "Character_images_left"
        myList = os.listdir(folderPath)
        self.images = []
        for imPath in myList:
            self.images.append(py.image.load(f'{folderPath}/{imPath}'))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = py.Rect(5, 5, 150, 198)
 
    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
 
py.init()
my_sprite = Sprite_Window()
my_group = py.sprite.Group(my_sprite)
clock = py.time.Clock()
q=1 
while q:
    for event in py.event.get():
        if event.type == py.QUIT:
            q=0
    my_group.update()
    bg = py.image.load('hacker.gif')   #background image 
    win.blit(bg,(1,1)); my_group.draw(win)
    py.display.update()
    clock.tick(13)
 # Code by Abhilash Gaurav
