#First we will import the pygame module

import pygame

#STARTUNG pygame using inint


pygame.init()

#makiing a window in which a game will work

screen = pygame.display.set_mode((500,500))

#Setting a caption to the pygame window

pygame.display.set_caption('ELIE ARMY')
#Adding a bg image to the game
#The image should be inn the same folder.



bg = pygame.image.load('filename.png')
pygame.display.update()


#Loading music in a game:

pygame.mixer.music.load('Filename.wav')

#Here -1 indicates that the music will run till the game ends
pygame.mixer.music.play(-1)

screen.blit(bg,(0,0))



#The whole game runs in a while loop

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Code of the game..





pygame.quit()
