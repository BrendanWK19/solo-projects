import pygame
import math

pygame.init()
screen = pygame.display.set_mode((400,600))
pygame.display.set_caption("Calculator")
gray = (65,65,65)
font = pygame.font.SysFont('Verdana', 40, bold = False)

#buttons
zerosurf = font.render('0', True, 'white')
zerobutton = pygame.Rect(102.5,500,95,95)

onesurf = font.render('1', True, 'white')
onebutton = pygame.Rect(2.5,400,95,95)

twosurf = font.render('2', True, 'white')
twobutton = pygame.Rect(102.5,400,95,95)

threesurf = font.render('3', True, 'white')
threebutton = pygame.Rect(202.5,400,95,95)

foursurf = font.render('4', True, 'white')
fourbutton = pygame.Rect(2.5,300,95,95)

fivesurf = font.render('5', True, 'white')
fivebutton = pygame.Rect(102.5,300,95,95)

sixsurf = font.render('6', True, 'white')
sixbutton = pygame.Rect(202.5,300,95,95)

sevensurf = font.render('7', True, 'white')
sevenbutton = pygame.Rect(2.5,200,95,95)

eightsurf = font.render('8', True, 'white')
eightbutton = pygame.Rect(102.5,200,95,95)

ninesurf = font.render('9' , True, 'white')
ninebutton = pygame.Rect(202.5,200,95,95)

plussurf = font.render('+', True, 'white')
plusbutton = pygame.Rect(302.5,400,95,95)

#function for color change when over button
def isonbutton(button, surf):
    # if on button
    if (button).collidepoint((a, b)):
        pygame.draw.rect(screen, (180,180,180), button)

    #if off button
    else:
        pygame.draw.rect(screen, (110,110,110), button)
        screen.blit(surf,(button.x+35, button.y+22))

input = 0
nextInput = 0
run = True
while run:
    screen.fill((gray))
    #event handler
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            run =  False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if zerobutton.collidepoint(event.pos):
                imput = 0
            if onebutton.collidepoint(event.pos):
                input = 1
            if twobutton.collidepoint(event.pos):
                input = 2
            if threebutton.collidepoint(event.pos):
                input = 3
            if fourbutton.collidepoint(event.pos):
                input = 4
            if fivebutton.collidepoint(event.pos):
                input = 5
            if sixbutton.collidepoint(event.pos):
                input = 6
            if sevenbutton.collidepoint(event.pos):
                input = 7
            if eightbutton.collidepoint(event.pos):
                input = 8
            if ninebutton.collidepoint(event.pos):
                input = 9
            if plusbutton.collidepoint(event.pos):
                plusinput(input)
            
    #initiate buttons
    a,b = pygame.mouse.get_pos()
    isonbutton(zerobutton, zerosurf)
    isonbutton(onebutton, onesurf)
    isonbutton(twobutton, twosurf)
    isonbutton(threebutton, threesurf)
    isonbutton(fourbutton, foursurf)
    isonbutton(fivebutton, fivesurf)
    isonbutton(sixbutton, sixsurf)
    isonbutton(sevenbutton, sevensurf)
    isonbutton(eightbutton, eightsurf)
    isonbutton(ninebutton, ninesurf)
    isonbutton(plusbutton, plussurf)

    #input
    displaysurf = font.render(str(input), True, 'white')
    screen.blit(displaysurf, (0,100))
    #plus
    def plusinput(input):
        return str(input) + '+'
    pygame.display.update()

pygame.quit()