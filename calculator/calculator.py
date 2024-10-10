import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Calculator")
gray = (65,65,65)
font = pygame.font.SysFont('Arial', 40, bold = False)

#buttons
zerosurf = font.render('0', True, 'white')
zerobutton = pygame.Rect(100,500,100,100)
onesurf = font.render('1', True, 'white')
onebutton = pygame.Rect(0,400,100,100)

#function for color change when over button
def isonbutton(button, surf):
    if (button).collidepoint((a, b)):
        pygame.draw.rect(screen, (180,180,180), button)
    else:
        pygame.draw.rect(screen, (110,110,110), button)
        screen.blit(surf,(button.x+5, button.y+5))

run = True
while run:
    screen.fill((gray))
    #event handler
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            run =  False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if zerobutton.collidepoint(event.pos):
                pygame.quit()
            if onebutton.collidepoint(event.pos):
                pygame.quit()
    a,b = pygame.mouse.get_pos()
    isonbutton(zerobutton, zerosurf)
    isonbutton(onebutton, onesurf)
    
    pygame.display.update()

pygame.quit()