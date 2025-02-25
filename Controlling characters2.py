import pygame,sys,time
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Controlling characters 2")
screen.fill("white")
player=pygame.image.load("ghost.png")
backround=pygame.image.load("halloweenbg.jpg")
sc=pygame.transform.scale(backround,(600,600))
playerx=300
playery=300
keys=[False,False,False,False]
pygame.display.update()
while playery < 600:
    screen.blit(sc,(0,0))
    screen.blit(player,(playerx,playery))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                keys[0]=True
            elif event.key==pygame.K_DOWN:
                keys[1]=True
            elif event.key==pygame.K_LEFT:
                keys[2]=True
            elif event.key==pygame.K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                keys[0]=False
            elif event.key==pygame.K_DOWN:
                keys[1]=False
            elif event.key==pygame.K_LEFT:
                keys[2]=False
            elif event.key==pygame.K_RIGHT:
                keys[3]=False
    if keys[0]:
        if playery > 0:
            playery-=7
    elif keys[1]:
        if playery < 350:
            playery+=7
    if keys[2]:
        if playerx > 0:
            playerx-=7
    elif keys[3]:
        if playerx < 450:
            playerx+=7
       
    playery+=3
    time.sleep(0.05)
print("Game Over!")