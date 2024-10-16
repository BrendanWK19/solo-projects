import pygame
import random

#initialize
pygame.init()
screen = pygame.display.set_mode((400,500))
pygame.display.set_caption("2048")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 24)

#2048 colors (dictionary)
colors = {0: (204, 192, 179),
          2: (238, 228, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 95),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          'dark text': (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

#initialize variables
board_values = [[0 for _ in range(4)] for _ in range(4)]
game_over = False
spawn_new = True
init_count = 0
direction = ''

#take turn based on direction
def take_turn(direction, board):
    merged = [[False for _ in range(4)] for _ in range(4)]
    if direction == 'UP':
        for i in range(4):
            for j in range(4):
                shift = 0
                if i > 0:
                    for q in range(i):
                        if board[q][j] == 0:
                            shift += 1
                    if shift > 0:
                        board[i - shift][j] = board[i][j]
                        board[i][j] = 0
                    if board[i - shift - 1][j] == board[i - shift][j] and not merged[i - shift][j] \
                            and not merged[i - shift - 1][j]:
                        board[i - shift - 1][j] *= 2
                        board[i - shift][j] = 0
                        merged[i - shift - 1][j] = True

    elif direction == 'DOWN':
        for i in range(3):
            for j in range(4):
                shift = 0
                for q in range(i + 1):
                    if board[3 - q][j] == 0:
                        
    elif direction == 'LEFT':
        pass
    elif direction == 'RIGHT':
        pass

    return board


#spawn new pieces randmonly on turn start
def new_pieces(board):
    count = 0
    full = False
    while any(0 in row for row in board) and count < 1: # some zero in some row in the board (check for empty spaces)
        row = random.randint(0,3)
        col = random.randint(0,3)
        if board[row][col] == 0: # found empty space
            count +=1
            if random.randint(1,10) == 10:
                board[row][col] = 4
            else:
                board[row][col] = 2
    if count < 1:
        full = True    
    return board, full

#draw background for board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], [0,0,400,400], 0, 10)
    pass

#draw tiles for game
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = color['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75], 0 , 5)
            if value > 0:
                value_len = len(str(value))
                font = pygame.font.Font('freesansbold.ttf', 48 - (5 * value_len))
                value_text = font.render(str(value), True, value_color)
                text_rect = value_text.get_rect(center = (j * 95 + 57, i * 95 + 57))
                screen.blit(value_text, text_rect)
                pygame.draw.rect(screen, 'black', [j * 95 + 20, i * 95 + 20, 75, 75], 2 , 5)

#game loop
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_values)

    if spawn_new or init_count < 2:
        board_values, game_over = new_pieces(board_values)
        spawn_new =  False
        init_count +=1

    if direction != '':
        board_values = take_turn(direction, board_values)
        direction = ''
        spawn_new = True

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =  False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                direction = 'UP'
            elif event.key == pygame.K_s:
                direction = 'DOWN'
            elif event.key == pygame.K_a:
                direction = 'LEFT'
            elif event.key == pygame.K_d:
                direction = 'RIGHT'
    
    pygame.display.flip()
    pygame.display.update()

pygame.quit()