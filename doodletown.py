import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, math, pygame, random, time
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #1920x1080
#screen.blit(pygame.font.SysFont('Comic Sans MS', size).render("Text Here", False, (r, g, b)), (x, y))

start_button_x = 0
A_prsd = 0
W_prsd = 0
S_prsd = 0
D_prsd = 0
T_prsd = 0
Enter_prsd = 0
Space_prsd = 0
Game_mode = "Menu"
Area = "Outside"
animation = "a"
nmtntime = 5
altcount = 20
scroll_x = 0

buddy_aimg = pygame.image.load('buddy_a.png')
buddy_bimg = pygame.image.load('buddy_b.png')
buddy_cimg = pygame.image.load('buddy_c.png')
buddy_1img = pygame.image.load('buddy_walk1.png')
buddy_2img = pygame.image.load('buddy_walk2.png')
buddy_1bimg = pygame.image.load('buddy_b1.png')
buddy_2bimg = pygame.image.load('buddy_b2.png')
buddy_1cimg = pygame.image.load('buddy_c1.png')
buddy_2cimg = pygame.image.load('buddy_c2.png')
buddy_1limg = pygame.image.load('buddy_walk1l.png')
buddy_2limg = pygame.image.load('buddy_walk2l.png')
buddy_1blimg = pygame.image.load('buddy_b1l.png')
buddy_2blimg = pygame.image.load('buddy_b2l.png')
buddy_1climg = pygame.image.load('buddy_c1l.png')
buddy_2climg = pygame.image.load('buddy_c2l.png')

tree_aimg = pygame.image.load('tree_a.png')
tree_bimg = pygame.image.load('tree_b.png')
tree_cimg = pygame.image.load('tree_c.png')

joeshop_aimg = pygame.image.load("Joe's Flower Emporium_a.png")
joeshop_bimg = pygame.image.load("Joe's Flower Emporium_b.png")
joeshop_cimg = pygame.image.load("Joe's Flower Emporium_c.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                A_prsd = 1
            if event.key == pygame.K_w:
                W_prsd = 1
            if event.key == pygame.K_s:
                S_prsd = 1
            if event.key == pygame.K_d:
                D_prsd = 1
            if event.key == pygame.K_RETURN:
                Enter_prsd = 1
            if event.key == pygame.K_SPACE:
                Space_prsd = 1
            if event.key == pygame.K_t:
                T_prsd = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                A_prsd = 0
            if event.key == pygame.K_w:
                W_prsd = 0
            if event.key == pygame.K_s:
                S_prsd = 0
            if event.key == pygame.K_d:
                D_prsd = 0
            if event.key == pygame.K_RETURN:
                Enter_prsd = 0
            if event.key == pygame.K_SPACE:
                Space_prsd = 0
            if event.key == pygame.K_t:
                T_prsd = 0

    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse1, mouse3, mouse2 = pygame.mouse.get_pressed()

    if altcount > 0:
        altcount -= 1
    elif altcount == 0:
        altcount = 20
    if nmtntime > 0:
        nmtntime -= 1
    elif nmtntime == 0 and animation == "a":
        animation = "b"
        nmtntime = 5
    elif nmtntime == 0 and animation == "b":
        animation = "c"
        nmtntime = 5
    elif nmtntime == 0 and animation == "c":
        animation = "a"
        nmtntime = 5

    if Game_mode == "Menu":
        font = pygame.font.Font(None, 65)
        text = font.render("DoodleTown", True, (155, 255, 155))
        text_rect = text.get_rect(center = (960, 400))
        screen.blit(text, text_rect)

        start_button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - start_button_x, 500 - start_button_x), (1020 + start_button_x, 500 - start_button_x), (1020 + start_button_x, 550 + start_button_x), (900 - start_button_x, 550 + start_button_x)])
        if start_button.collidepoint(mouse_x, mouse_y):
            start_button_x = 10
            if mouse1:
                Game_mode = "Start"
        elif not start_button.collidepoint(mouse_x, mouse_y):
            start_button_x = 0
        font = pygame.font.Font(None, 65)
        text = font.render("Start", True, (155, 255, 155))
        text_rect = text.get_rect(center = (960, 525))
        screen.blit(text, text_rect)

    if Game_mode == "Start":
        if T_prsd == 1:
            print("xpos is", scroll_x)

        if Area == "Outside":
            #left "boundary" illusion
            if scroll_x > 1440 and D_prsd == 1:
                scroll_x = 1440

            #joe's Emporium (doors = -770)
            if scroll_x < -325 and scroll_x > -1555 and W_prsd == 1:
                Area = "Joe's"
                scroll_x = 0

            #background
            if animation == "a":
                screen.blit(tree_aimg, (500 + scroll_x, 450))
            if animation == "b":
                screen.blit(tree_bimg, (500 + scroll_x, 450))
            if animation == "c":
                screen.blit(tree_cimg, (500 + scroll_x, 450))
            if animation == "a":
                screen.blit(tree_aimg, (600 + scroll_x, 480))
            if animation == "b":
                screen.blit(tree_bimg, (600 + scroll_x, 480))
            if animation == "c":
                screen.blit(tree_cimg, (600 + scroll_x, 480))

            if animation == "a":
                screen.blit(joeshop_aimg, (1200 + scroll_x, 100))
            if animation == "b":
                screen.blit(joeshop_bimg, (1200 + scroll_x, 100))
            if animation == "c":
                screen.blit(joeshop_cimg, (1200 + scroll_x, 100))

        if Area == "Joe's": #jj
            pass

        #Buddy animation
        if not A_prsd == 1 and not D_prsd == 1:
            if animation == "a":
                screen.blit(buddy_aimg, (910, 650))
            if animation == "b":
                screen.blit(buddy_bimg, (910, 650))
            if animation == "c":
                screen.blit(buddy_cimg, (910, 650))
        if A_prsd == 1:
            scroll_x += 5
            if animation == "a":
                if altcount < 11:
                    screen.blit(buddy_1limg, (910, 650))
                if altcount > 10:
                    screen.blit(buddy_2limg, (910, 650))
            if animation == "b":
                if altcount < 11:
                    screen.blit(buddy_1blimg, (910, 650))
                if altcount > 10:
                    screen.blit(buddy_2blimg, (910, 650))
            if animation == "c":
                if altcount < 11:
                    screen.blit(buddy_1climg, (910, 650))
                if altcount > 10:
                    screen.blit(buddy_2climg, (910, 650))
        if D_prsd == 1:
            scroll_x -= 5
            if animation == "a":
                if altcount < 11:
                    screen.blit(buddy_1img, (910, 650))
                if altcount > 10:
                    screen.blit(buddy_2img, (910, 650))
            if animation == "b":
                if altcount < 11:
                    screen.blit(buddy_1bimg, (910, 650))
                if altcount > 10:
                    screen.blit(buddy_2bimg, (910, 650))
            if animation == "c":
                if altcount < 11:
                    screen.blit(buddy_1cimg, (910, 650))
                if altcount > 10:
                    screen.blit(buddy_2cimg, (910, 650))

    pygame.time.wait(10)
    pygame.display.flip()
    if Area == "Outside":
        screen.fill((155, 155, 255))
    if Area == "Joe's":
        screen.fill((204, 132, 132))
