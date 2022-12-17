import pygame
import random

pygame.font.init()
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\tetris_music.ogg')
pygame.mixer.music.play(-1)


s_width = 1280
s_height = 720
play_width = 300
play_height = 600
block_size = 30

top_left_x = ((s_width - play_width) // 2)
top_left_y = s_height - play_height - 50

logo_position_x = 1
logo_move_x = 0.5
logo_position_y = 1
logo_move_y = 0.5

setting_changed = False
background = None

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255),
                (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(shape_colors)
        self.rotation = 0

class Setting():
    default_bg = (0, 0, 0)
    assassings_bg = pygame.image.load("backgrounds/assassins.jpg")
    beach_bg = pygame.image.load("backgrounds/beach.jpg")
    galaxy_bg = pygame.image.load("backgrounds/galaxy.jpg")
    lake_bg = pygame.image.load("backgrounds/lake.jpg")
    waterfall_bg = pygame.image.load("backgrounds/waterfall.jpg")
    winter_bg = pygame.image.load("backgrounds/winter.jpg")
    
    
    def setting_menu(self):
        white = (255, 255, 255)
        grey = (126, 126, 126)
        bg_color = white
        sound_color = white
        while True:
            pygame.font.init()
            font = pygame.font.Font( r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\digital_font.TTF", 60)
            choose_background_label = font.render("Choose background", 1, bg_color)
            choose_background_label_rect = choose_background_label.get_rect(midbottom=(300, 200))
            sound_on = True
            if sound_on:
                sound = font.render("Sound on", 1, sound_color)
            elif sound_on == False:
                sound = font.render("Sound off", 1, sound_color)
            sound_rect = sound.get_rect(midbottom=(300, 400))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.MOUSEMOTION:
                    if choose_background_label_rect.collidepoint(pygame.mouse.get_pos()):
                        bg_color = grey
                    else:
                        bg_color = white
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if choose_background_label_rect.collidepoint(pygame.mouse.get_pos()):
                        self.choose_background()
                        return
            win.fill((0, 0, 0))
            win.blit(choose_background_label, choose_background_label_rect)
            win.blit(sound, sound_rect)
            pygame.display.update()
            
    def choose_background(self):
        global setting_changed
        global background
        assassins = pygame.transform.scale(self.assassings_bg, (320, 180)).convert_alpha()
        assassins_rect = assassins.get_rect(midbottom = (250, 300))
        beach = pygame.transform.scale(self.beach_bg, (320,180)).convert_alpha()
        beach_rect = beach.get_rect(midbottom = (650, 300))
        galaxy = pygame.transform.scale(self.galaxy_bg, (320, 180)).convert_alpha()
        galaxy_rect = galaxy.get_rect(midbottom = (1050, 300))
        lake = pygame.transform.scale(self.lake_bg, (320, 180)).convert_alpha()
        lake_rect = lake.get_rect(midbottom = (250, 600))
        waterfall = pygame.transform.scale(self.waterfall_bg, (320, 180)).convert_alpha()
        waterfall_rect = waterfall.get_rect(midbottom = (650, 600))
        winter = pygame.transform.scale(self.winter_bg, (320, 180)).convert_alpha()
        winter_rect = winter.get_rect(midbottom = (1050, 600))
        all_backgrounds = {assassins: (self.assassings_bg, assassins_rect), beach: (self.beach_bg, beach_rect), galaxy: (self.galaxy_bg, galaxy_rect), lake: (self.lake_bg, lake_rect), waterfall: (self.waterfall_bg, waterfall_rect), winter: (self.winter_bg, winter_rect)}
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.MOUSEMOTION:
                    for image, value in all_backgrounds.items():
                        if value[1].collidepoint(pygame.mouse.get_pos()):
                            image.set_alpha(64)
                        else:
                            image.set_alpha(255)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for image, value in all_backgrounds.items():
                        if value[1].collidepoint(pygame.mouse.get_pos()):
                            setting_changed = True
                            background = value[0]
                            return
            win.fill((0, 0, 0))
            for image, value in all_backgrounds.items():
                win.blit(image, value[1])
            pygame.display.update()
            


def create_grid(locked_pos={}):
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(10) if grid[i]
                     [j] == (0, 0, 0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(surface, text, size, color):
    font = pygame.font.Font( r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\digital_font.TTF", size)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width()/2),
                 top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy +
                         i*block_size), (sx+play_width, sy + i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j *
                             block_size, sy), (sx + j*block_size, sy + play_height))


def clear_rows(grid, locked):

    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)

    return inc


def draw_next_shape(shape, surface):
    font = pygame.font.Font(
        r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\digital_font.TTF", 80)
    label = font.render('Next Shape', 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*block_size +
                                 130, sy + i*block_size - 50, block_size, block_size), 0)

    surface.blit(label, (sx, sy - 180))


def update_score(nscore):
    score = max_score()

    with open(r'C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))


def max_score():
    with open(r'C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score


def draw_window(surface, grid, score=0, last_score=0):
    global setting_changed
    global background
    if setting_changed == False:
        surface.fill((0, 0, 0))
    else:
        surface.blit(background, (0, 0))
    pygame.font.init()

    tetris_logo = pygame.image.load(
        r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\tetris_logo.png").convert_alpha()
    tetris_logo = pygame.transform.scale(tetris_logo, (305, 216))
    surface.blit(tetris_logo, (90, 190))

    font = pygame.font.Font(
        r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\digital_font.TTF", 80)
    label = font.render('Score', 1, (255, 255, 255))
    label2 = font.render(str(score), 1, (255, 255, 255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx + 100, sy + 240))
    surface.blit(label2, (sx + 190, sy + 310))

    label = font.render('High Score', 1, (255, 255, 255))
    label2 = font.render(last_score, 1, (255, 255, 255))

    sx = top_left_x - 200
    sy = top_left_y + 200

    surface.blit(label, (sx - 220, sy + 240))
    surface.blit(label2, (sx - 70, sy + 310))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size,
                             top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (26, 110, 167), (top_left_x,
                     top_left_y, play_width, play_height), 3)

    draw_grid(surface, grid)


def pause(win, clock):
    
    pygame.font.init()
    font = pygame.font.Font(r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\digital_font.TTF", 150)
    font2 = pygame.font.Font(r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\digital_font.TTF", 70)
    label = font.render('Paused', 1, (255, 0, 0))
    label2 = font2.render("Press any key to continue", 1, (255, 0, 0))
    win.blit(label, (400, 250))
    win.blit(label2, (250, 350))
    
    
    loop = 1
    while loop:
        pygame.mixer.music.pause()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
            if event.type == pygame.KEYDOWN:
                pygame.mixer.music.play(-1)
                win.fill((0, 0, 0))
                loop = 0
        pygame.display.update()
        clock.tick(60)


def main(win):
    last_score = max_score()
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_SPACE:
                    for i in range(20):
                        if (valid_space(current_piece, grid)):
                            current_piece.y = i
                        elif not (valid_space(current_piece, grid)):
                            break
                    current_piece.y = i - 2
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
                if event.key == pygame.K_p:
                    pause(win, clock)

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(win, grid, score, last_score)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            draw_text_middle(win, "YOU LOST!", 120, (255, 0, 0))
            pygame.display.update()
            pygame.time.delay(3500)
            run = False
            update_score(score)


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def main_menu(win):
    global logo_position_x
    global logo_move_x
    global logo_position_y
    global logo_move_y
    main_menu_bg = pygame.image.load(
        r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\tetris_bg.jpg")
    play_button = pygame.image.load(
        r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\play_button.png").convert_alpha()
    play_button = pygame.transform.scale(play_button, (200, 80))
    play_rect = play_button.get_rect(bottomleft=(421, 630))
    settings_button = pygame.image.load(
        r"C:\Users\ANDRZ\Desktop\ZaRaczke\Tetris\settings_button.png").convert_alpha()
    settings_button = pygame.transform.scale(settings_button, (200, 80))
    settings_rect = settings_button.get_rect(bottomright=(857, 630))
    logo = pygame.image.load(
        r"C:\Users\ANDRZ\Downloads\319050571_1503471206812421_3038328311112936503_n.png").convert_alpha()
    logo = pygame.transform.scale(logo, (100, 100))

    run = True
    while run:
        
        logo_start_x = 0 + logo_position_x
        logo_start_y = 0 + logo_position_y

        win.blit(main_menu_bg, (0, 0))
        win.blit(play_button, play_rect)
        win.blit(settings_button, settings_rect)
        win.blit(logo, (logo_start_x, logo_start_y))
        if logo_position_x >= 1200:
            logo_move_x = -0.3
        if logo_position_x <= 0:
            logo_move_x = 0.3
        if logo_position_y <= 0:
            logo_move_y = 0.2
        if logo_position_y >= 100:
            logo_move_y = -0.2
        logo_position_x += logo_move_x
        logo_position_y += logo_move_y

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(event.pos):
                    main(win)
                elif settings_rect.collidepoint(event.pos):
                    settings = Setting()
                    settings.setting_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main(win)

    pygame.display.quit()


win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)
