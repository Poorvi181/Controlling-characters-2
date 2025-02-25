import pygame,sys

import pygame.imageext
pygame.init()
WIDTH,HEIGHT=900,500
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Space invasion")
screen.fill("white")
spaceimg=pygame.image.load("starsbg.png")
space=pygame.transform.scale(spaceimg,(WIDTH,HEIGHT))
border=pygame.Rect(WIDTH//2-5,0,10,HEIGHT)
redspaceship=pygame.image.load("spaceship1.png")
sw,sh=55,40
redship=pygame.transform.scale(redspaceship,(sw,sh))
redship1=pygame.transform.rotate(redship,90)
yellowspaceship=pygame.image.load("spaceship2.png")
yellowspaceship=pygame.image.load("spaceship1.png")
sw,sh=55,40
yellowship=pygame.transform.scale(yellowspaceship,(sw,sh))
yellowship1=pygame.transform.rotate(yellowship,90)
pygame.display.update()
def draw(red,yellow):
    screen.blit(space,(0,0))
    pygame.draw.rect(screen,"black",border)
    screen.blit(redship1,(red.x,red.y))
    screen.blit(yellowspaceship,(yellow.x,yellow.y))
    pygame.display.update()
def main():
    red=pygame.Rect(100,250,sw,sh)
    yellow=pygame.Rect(800,250,sw,sh)
    draw(red,yellow)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
if __name__=="__main__":
    main()
