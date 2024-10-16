from methods import deal
import pygame

#initialize display
pygame.display.init()
screen = pygame.display.set_mode(size=(1000,500))
pygame.display.set_caption("BlackJack")
pygame.font.init()

#load sprite sheet
clubs_sprite_sheet_image = pygame.image.load('Cards/Clubs-88x124.png').convert_alpha()

#fonts
font = pygame.font.SysFont('Impact', 40 , bold=False)
hit_surf = font.render('Hit', True, 'white')
stand_surf = font.render('Stand', True, 'white')
playagain_surf = font.render('Play Again', True, 'white')
exit_surf = font.render('Exit', True, 'white')
hbutton = pygame.Rect(280,400,60,60)
sbutton = pygame.Rect(610,400,105,60)
play_again_button = pygame.Rect(400, 400, 180, 60)
exit_button = pygame.Rect(50,400,70,60)

#function to draw text
def drawtext(text, font, color, x, y):
    surf = font.render(text, True, color)
    screen.blit(surf, (x,y))

def game_loop():
    #deal intitial cards and initialize hands
    phand = 0
    dhand = 0
    phand += deal(phand)
    #dhand += deal(dhand) #deal hidden card
    phand += deal(phand) 
    dhand += deal(dhand)
    print(phand)
    print("Player Score: " + str(phand))
    print("Dealer score: "+ str(dhand))
    #game loop
    run = True
    while run:
        screen.fill('darkgreen')
        drawtext("Player Score: " + str(phand), font, 'white', 350, 400)
        drawtext("Dealer Score: " + str(dhand), font, 'white', 50, 50)
        #event handler
        for event in pygame.event.get():
            #quit game
            if event.type == pygame.QUIT:
                pygame.quit()
            #hit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hbutton.collidepoint(event.pos):
                    phand += deal(phand)
                    print("player score: "+ str(phand))
            #stand button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sbutton.collidepoint(event.pos):
                    print("Stand")
                    #dealer logic
                    while run == True:
                        if dhand < 17:
                            dhand += deal(dhand)
                            print("dealer score: " + str(dhand))
                        elif dhand == 21:
                            print("dealer blackjack")
                            drawtext("Blackjack! You lose!", font, 'white', 0,0)
                            
                            run = False
                            break
                        elif dhand > 21:
                            print("dealer bust")
                            run = False
                            drawtext("Dealer Busts! You Win!", font, 'white', 0,0)
                            break
                        elif dhand > phand:
                            print("dealer wins")
                            run = False
                            drawtext("Dealer Wins!", font, 'white', 0,0)
                            break
                        elif dhand == phand:
                            print("push")
                            drawtext("Push", font, 'white', 0,0)
                            run = False
                            break
                        else:
                            print("player wins")
                            drawtext("You Win!", font, 'white', 0,0)
                            run = False
                            break
            #exit button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.collidepoint(event.pos):
                    pygame.QUIT()
        #checks game logic
        if phand >= 22:
            print("Bust")
            run = False
        elif phand == 21:
            print("Blackjack!")
            run = False

        #buttons
        a, b = pygame.mouse.get_pos()
        #hit
        if hbutton.collidepoint((a, b)):
            pygame.draw.rect(screen, (180,180,180), hbutton)
        else:
            pygame.draw.rect(screen, (110,110,110), hbutton)
        screen.blit(hit_surf,(hbutton.x+5, hbutton.y+5))
        #stand
        if sbutton.collidepoint((a, b)):
            pygame.draw.rect(screen,(180,180,180), sbutton)
        else:
            pygame.draw.rect(screen, (110,110,110), sbutton)
        screen.blit(stand_surf,(sbutton.x+5, sbutton.y+5))
        #exit
        if exit_button.collidepoint((a,b)):
            pygame.draw.rect(screen, (180,180,180), exit_button)
        else:
            pygame.draw.rect(screen, (110,110,110), exit_button)
        screen.blit(exit_surf, (exit_button.x+5, exit_button.y+5))
        pygame.display.update()

    return True # show that game ended

def main():
    while True:
        if not game_loop():
            break
        screen.fill('darkgreen')
        pygame.draw.rect(screen, (180, 180, 180), play_again_button)
        screen.blit(playagain_surf, (play_again_button.x + 5, play_again_button.y + 5))
        pygame.display.update()
        
        # wait for user to play again
        play_again = False
        while not play_again:
            for event in pygame.event.get():
                #play again button
                a, b = pygame.mouse.get_pos()
                if play_again_button.collidepoint((a, b)):
                    pygame.draw.rect(screen, (180, 180, 180), play_again_button)
                else:
                    pygame.draw.rect(screen, (110, 110, 110), play_again_button)
                screen.blit(playagain_surf, (play_again_button.x + 5, play_again_button.y + 5))
                
                pygame.display.update()

                #event handler outside of run
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_again_button.collidepoint(event.pos):
                        play_again = True
                if exit_button.collidepoint((a,b)):
                    pygame.draw.rect(screen, (180,180,180), exit_button)
                else:
                    pygame.draw.rect(screen, (110,110,110), exit_button)
                screen.blit(exit_surf, (exit_button.x+5, exit_button.y+5))

main()

#test 

