import pygame

pygame.display.init()
screen = pygame.display.set_mode(size=(1000,800))
pygame.display.set_caption("BlackJack")
pygame.font.init()
black = (0,0,0)

clubs_sprite_sheet = pygame.image.load('Cards/Clubs-88x124.png').convert_alpha()
spades_sprite_sheet = pygame.image.load('Cards/Spades-88x124.png').convert_alpha()
hearts_sprite_sheet = pygame.image.load('Cards/Hearts-88x124.png').convert_alpha()
diamonds_sprite_sheet = pygame.image.load('Cards/Diamonds-88x124.png').convert_alpha()

def get_image(sheet, frame, width, height, scale):
    playing_card = pygame.Surface((width, height)).convert_alpha()
    playing_card.blit(sheet, (0,0), ((frame * width), 0, width, height))
    playing_card = pygame.transform.scale(playing_card, (width * scale, height * scale))
    playing_card.set_colorkey(black)
    return playing_card

aceheart = get_image(hearts_sprite_sheet, 0, 88, 124, 1.25)
twoheart = get_image(hearts_sprite_sheet, 1, 88, 124, 1.25)
threeheart = get_image(hearts_sprite_sheet, 2, 88, 124, 1.25)
fourheart = get_image(hearts_sprite_sheet, 3, 88, 124, 1.25)
fiveheart = get_image(hearts_sprite_sheet, 4, 88, 124, 1.25)

run = True
while run:

    screen.fill('darkgreen')

    #show frame image
    screen.blit(aceheart, (0,0))
    screen.blit(twoheart, (150, 0))
    screen.blit(threeheart, (300,0))
    screen.blit(fourheart, (450,0))
    screen.blit(fiveheart, (600,0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()