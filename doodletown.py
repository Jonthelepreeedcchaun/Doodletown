import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys, math, pygame, random, time
import pickle
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #1920x1080
#screen.blit(pygame.font.SysFont('Comic Sans MS', size).render("Text Here", False, (r, g, b)), (x, y))

green = (155, 255, 155)

def text_objects(text, font, colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text, position, size, colour):
    smallText = pygame.font.Font(None, size)
    TextSurf, TextRect = text_objects(text, smallText, colour)
    TextRect.center = position
    screen.blit(TextSurf, TextRect)

def Append_to_save(Filename, Text):
    Save = open("%s.sav" %Filename, "a")
    Save.write(Text)
    Save.close()

def Overwrite_save(Filename, text):
    Save = open("%s.txt" %Filename, "w")
    Save.write(text)
    Save.close()

start_button_x = 0
Quit_Button_x = 0
Save_Button_x = 0
A_prsd = 0
W_prsd = 0
S_prsd = 0
D_prsd = 0
T_prsd = 0
Q_prsd = 0
Enter_prsd = 0
Space_prsd = 0
Esc_prsd = 0
Game_mode = "Menu"
Paused = 0
Area = "Outside"
minigame = ""
animation = "a"
nmtntime = 5
altcount = 20
scroll_x = 0
mouse_visi = 1
inventory = []
slot1open = 1
slot2open = 1
slot3open = 1
slot4open = 1
grabbed = 0
equipped = 0
cookbookicon_exception = 0
saveslot = 0


savdata = {'Area':Area, 'scroll_x':scroll_x, 'inventory':inventory}
data1 = {'Area':Area, 'scroll_x':scroll_x, 'inventory':inventory}
data2 = {'Area':Area, 'scroll_x':scroll_x, 'inventory':inventory}
data3 = {'Area':Area, 'scroll_x':scroll_x, 'inventory':inventory}
pygame.mouse.set_visible(0)

cursor_aimg = pygame.image.load('cursor_a.png')
cursor_bimg = pygame.image.load('cursor_b.png')
cursor_cimg = pygame.image.load('cursor_c.png')
inv_aimg = pygame.image.load('inv_a.png')
inv_bimg = pygame.image.load('inv_b.png')
inv_cimg = pygame.image.load('inv_c.png')

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
shrub_aimg = pygame.image.load('shrub_a.png')
shrub_bimg = pygame.image.load('shrub_b.png')
shrub_cimg = pygame.image.load('shrub_c.png')
bigtree_aimg = pygame.image.load('big_tree_a.png')
bigtree_bimg = pygame.image.load('big_tree_b.png')
bigtree_cimg = pygame.image.load('big_tree_c.png')

joeshop_aimg = pygame.image.load("Joe's Flower Emporium_a.png")
joeshop_bimg = pygame.image.load("Joe's Flower Emporium_b.png")
joeshop_cimg = pygame.image.load("Joe's Flower Emporium_c.png")
joedoor_aimg = pygame.image.load("Joe's Door_a.png")
joedoor_bimg = pygame.image.load("Joe's Door_b.png")
joedoor_cimg = pygame.image.load("Joe's Door_c.png")
joestand_aimg = pygame.image.load("Joestand_a.png")
joestand_bimg = pygame.image.load("Joestand_b.png")
joestand_cimg = pygame.image.load("Joestand_c.png")
joeshelf_aimg = pygame.image.load("shelf_a.png")
joeshelf_bimg = pygame.image.load("shelf_b.png")
joeshelf_cimg = pygame.image.load("shelf_c.png")

house_aimg = pygame.image.load("House_a.png")
house_bimg = pygame.image.load("House_b.png")
house_cimg = pygame.image.load("House_c.png")
homedoor_aimg = pygame.image.load("HomeDoor_a.png")
homedoor_bimg = pygame.image.load("HomeDoor_b.png")
homedoor_cimg = pygame.image.load("HomeDoor_c.png")
stove_aimg = pygame.image.load("stove_a.png")
stove_bimg = pygame.image.load("stove_b.png")
stove_cimg = pygame.image.load("stove_c.png")
carrot_aimg = pygame.image.load("carrot_a.png")
carrot_bimg = pygame.image.load("carrot_b.png")
carrot_cimg = pygame.image.load("carrot_c.png")
cookbook_smallimg = pygame.image.load("itemsmall_book.png")
cookbook_largeimg = pygame.image.load("itemlarge_book.png")

running = True
while running:
    savdata = {'Area':Area, 'scroll_x':scroll_x, 'inventory':inventory}
    if saveslot == 1:
        with open('savefile1', 'wb') as f:
            pickle.dump(savdata, f)
        with open('savefile1', 'rb') as f:
            data1 = pickle.load(f)
    if saveslot == 2:
        with open('savefile2', 'wb') as f:
            pickle.dump(savdata, f)
        with open('savefile2', 'rb') as f:
            data2 = pickle.load(f)
    if saveslot == 3:
        with open('savefile3', 'wb') as f:
            pickle.dump(savdata, f)
        with open('savefile3', 'rb') as f:
            data3 = pickle.load(f)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Esc_prsd = 1
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
            if event.key == pygame.K_q:
                Q_prsd = 1
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
            if event.key == pygame.K_q:
                Q_prsd = 0

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

    if Esc_prsd == 1:
        Paused = 1

    if Game_mode == "Menu":
        mouse_visi = 1
        message_display("DoodleTown", (960, 400), 65, green)

#start button
        start_button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - start_button_x, 500 - start_button_x), (1020 + start_button_x, 500 - start_button_x), (1020 + start_button_x, 550 + start_button_x), (900 - start_button_x, 550 + start_button_x)])
        if start_button.collidepoint(mouse_x, mouse_y):
            start_button_x = 10
            if mouse1:
                Game_mode = "Loadmenu"
        elif not start_button.collidepoint(mouse_x, mouse_y):
            start_button_x = 0
        #my version
        message_display("Start", (960, 525), 65, green)

#Quit Button
        Quit_Button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - Quit_Button_x, 600 - Quit_Button_x), (1020 + Quit_Button_x, 600 - Quit_Button_x), (1020 + Quit_Button_x, 650 + Quit_Button_x), (900 - Quit_Button_x, 650 + Quit_Button_x)])
        if Quit_Button.collidepoint(mouse_x, mouse_y):
            Quit_Button_x = 10
            if mouse1:
                running = False
        elif not Quit_Button.collidepoint(mouse_x, mouse_y):
            Quit_Button_x = 0
        message_display("Quit", (960, 625), 65, green)

    ##Loadmenu
    if Game_mode == "Loadmenu":
        start_button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - start_button_x, 500 - start_button_x), (1020 + start_button_x, 500 - start_button_x), (1020 + start_button_x, 550 + start_button_x), (900 - start_button_x, 550 + start_button_x)])
        if start_button.collidepoint(mouse_x, mouse_y):
            start_button_x = 10
            if mouse1:
                saveslot = 1
                Area = data1['Area']
                scroll_x = data1['scroll_x']
                inventory = data1['inventory']
                Game_mode = "Start"
        elif not start_button.collidepoint(mouse_x, mouse_y):
            start_button_x = 0
        #my version
        message_display("Save 1", (960, 525), 45, green)


        Quit_Button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - Quit_Button_x, 600 - Quit_Button_x), (1020 + Quit_Button_x, 600 - Quit_Button_x), (1020 + Quit_Button_x, 650 + Quit_Button_x), (900 - Quit_Button_x, 650 + Quit_Button_x)])
        if Quit_Button.collidepoint(mouse_x, mouse_y):
            Quit_Button_x = 10
            if mouse1:
                saveslot = 2
                Area = data2['Area']
                scroll_x = data2['scroll_x']
                inventory = data2['inventory']
                Game_mode = "Start"
        elif not Quit_Button.collidepoint(mouse_x, mouse_y):
            Quit_Button_x = 0
        message_display("Save 2", (960, 625), 65, green)


        Save_Button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - Save_Button_x, 700 - Save_Button_x), (1020 + Save_Button_x, 700 - Save_Button_x), (1020 + Save_Button_x, 750 + Save_Button_x), (900 - Save_Button_x, 750 + Save_Button_x)])
        if Save_Button.collidepoint(mouse_x, mouse_y):
            Save_Button_x = 10
            if mouse1:
                saveslot = 3
                Area = data3['Area']
                scroll_x = data3['scroll_x']
                inventory = data3['inventory']
                Game_mode = "Start"
        elif not Save_Button.collidepoint(mouse_x, mouse_y):
            Save_Button_x = 0
        message_display("Save 3", (960, 725), 65, green)

    if Game_mode == "Start":
        mouse_visi = 0
        if T_prsd == 1:
            print("xpos is", scroll_x)

        if Area == "Outside":
            #left "boundary" illusion
            if scroll_x > 1440 and D_prsd == 1:
                scroll_x = 1440

            #joe's Emporium (doors = -770)
            if scroll_x < -325 and scroll_x > -1555 and W_prsd == 1:
                Area = "Joe's"
                scroll_x = 285

            #house (doors = -2785)
            if scroll_x < -2530 and scroll_x > -3005 and W_prsd == 1:
                Area = "Home"
                scroll_x = 0

            #background
            if animation == "a":
                screen.blit(tree_aimg, (500 + scroll_x, 450))
                screen.blit(tree_aimg, (600 + scroll_x, 480))
                screen.blit(tree_aimg, (800 + scroll_x, 500))
                screen.blit(shrub_aimg, (1000 + scroll_x, 700))
                screen.blit(joeshop_aimg, (1200 + scroll_x, 100))
                screen.blit(shrub_aimg, (2850 + scroll_x, 700))
                screen.blit(bigtree_aimg, (3000 + scroll_x, 50))
                screen.blit(house_aimg, (3400 + scroll_x, 150))
            if animation == "b":
                screen.blit(tree_bimg, (500 + scroll_x, 450))
                screen.blit(tree_bimg, (600 + scroll_x, 480))
                screen.blit(tree_bimg, (800 + scroll_x, 500))
                screen.blit(shrub_bimg, (1000 + scroll_x, 700))
                screen.blit(joeshop_bimg, (1200 + scroll_x, 100))
                screen.blit(shrub_bimg, (2850 + scroll_x, 700))
                screen.blit(bigtree_bimg, (3000 + scroll_x, 50))
                screen.blit(house_bimg, (3400 + scroll_x, 150))
            if animation == "c":
                screen.blit(tree_cimg, (500 + scroll_x, 450))
                screen.blit(tree_cimg, (600 + scroll_x, 480))
                screen.blit(tree_cimg, (800 + scroll_x, 500))
                screen.blit(shrub_cimg, (1000 + scroll_x, 700))
                screen.blit(joeshop_cimg, (1200 + scroll_x, 100))
                screen.blit(shrub_cimg, (2850 + scroll_x, 700))
                screen.blit(bigtree_cimg, (3000 + scroll_x, 50))
                screen.blit(house_cimg, (3400 + scroll_x, 150))

        if Area == "Joe's":
            if scroll_x > 380:
                Area = "Outside"
                scroll_x = -770

            if scroll_x < -1840 and A_prsd == 1 and scroll_x > -8125:
                scroll_x = -1840

            if animation == "a":
                screen.blit(joedoor_aimg, (500 + scroll_x, 600))
                screen.blit(joestand_aimg, (1000 + scroll_x, 600))
                screen.blit(joeshelf_aimg, (10000 + scroll_x, 450))
            if animation == "b":
                screen.blit(joedoor_bimg, (500 + scroll_x, 600))
                screen.blit(joestand_bimg, (1000 + scroll_x, 600))
                screen.blit(joeshelf_bimg, (10000 + scroll_x, 450))
            if animation == "c":
                screen.blit(joedoor_cimg, (500 + scroll_x, 600))
                screen.blit(joestand_cimg, (1000 + scroll_x, 600))
                screen.blit(joeshelf_cimg, (10000 + scroll_x, 450))

        if Area == "Home":
            if scroll_x > 80:
                Area = "Outside"
                scroll_x = -2785

            if scroll_x < -165 and scroll_x > -420 and W_prsd == 1:
                minigame = "cooking"
                Paused = 1

            if scroll_x < -625 and scroll_x > -705 and S_prsd and not "cookbook" in inventory:
                if slot1open == 1:
                    inventory.append("cookbook")
                    slot1open = "cookbook"
                elif slot2open == 1:
                    inventory.append("cookbook")
                    slot2open = "cookbook"
                elif slot3open == 1:
                    inventory.append("cookbook")
                    slot3open = "cookbook"
                elif slot4open == 1:
                    inventory.append("cookbook")
                    slot4open = "cookbook"
                else:
                    message_display("No room in inventory!", (100, 100), 65, red)

            if animation == "a":
                screen.blit(homedoor_aimg, (810 + scroll_x, 600))
                screen.blit(stove_aimg, (1100 + scroll_x, 620))
            if animation == "b":
                screen.blit(homedoor_bimg, (810 + scroll_x, 600))
                screen.blit(stove_bimg, (1100 + scroll_x, 620))
            if animation == "c":
                screen.blit(homedoor_cimg, (810 + scroll_x, 600))
                screen.blit(stove_cimg, (1100 + scroll_x, 620))
            if not "cookbook" in inventory:
                screen.blit(cookbook_smallimg, (1600 + scroll_x, 800))

        #Buddy animation
        if Paused == 0:
            if not A_prsd == 1 and not D_prsd == 1:
                if animation == "a":
                    screen.blit(buddy_aimg, (910, 650))
                if animation == "b":
                    screen.blit(buddy_bimg, (910, 650))
                if animation == "c":
                    screen.blit(buddy_cimg, (910, 650))
        if Paused == 1:
            if animation == "a":
                screen.blit(buddy_aimg, (910, 650))
            if animation == "b":
                screen.blit(buddy_bimg, (910, 650))
            if animation == "c":
                screen.blit(buddy_cimg, (910, 650))
        if Paused == 0:
            if A_prsd == 1 and not D_prsd == 1:
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

            if Q_prsd == 1:
                minigame = "inventory"
                Paused = 1

        if Paused == 1:
            mouse_visi = 1
            if Esc_prsd == 1:
                start_button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - start_button_x, 500 - start_button_x), (1020 + start_button_x, 500 - start_button_x), (1020 + start_button_x, 550 + start_button_x), (900 - start_button_x, 550 + start_button_x)])
                if start_button.collidepoint(mouse_x, mouse_y):
                    start_button_x = 10
                    if mouse1:
                        Paused = 0
                        Esc_prsd = 0
                elif not start_button.collidepoint(mouse_x, mouse_y):
                    start_button_x = 0
                #my version
                message_display("Resume", (960, 525), 45, green)


                Quit_Button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - Quit_Button_x, 600 - Quit_Button_x), (1020 + Quit_Button_x, 600 - Quit_Button_x), (1020 + Quit_Button_x, 650 + Quit_Button_x), (900 - Quit_Button_x, 650 + Quit_Button_x)])
                if Quit_Button.collidepoint(mouse_x, mouse_y):
                    Quit_Button_x = 10
                    if mouse1:
                        running = False
                elif not Quit_Button.collidepoint(mouse_x, mouse_y):
                    Quit_Button_x = 0
                message_display("Quit", (960, 625), 65, green)


                Save_Button = pygame.draw.polygon(screen, (255, 255, 255), [(900 - Save_Button_x, 700 - Save_Button_x), (1020 + Save_Button_x, 700 - Save_Button_x), (1020 + Save_Button_x, 750 + Save_Button_x), (900 - Save_Button_x, 750 + Save_Button_x)])
                if Save_Button.collidepoint(mouse_x, mouse_y):
                    Save_Button_x = 10
                    if mouse1:
                        Overwrite_save("savefile", "uhhhh data i guess idk\n")
                        Paused = 0
                        Esc_prsd = 0
                elif not Save_Button.collidepoint(mouse_x, mouse_y):
                    Save_Button_x = 0
                message_display("Save", (960, 725), 65, green)
            elif Esc_prsd == 0: #minigames
                Quit_Button = pygame.draw.polygon(screen, (255, 255, 255), [(100 - Quit_Button_x, 80 - Quit_Button_x), (220 + Quit_Button_x, 80 - Quit_Button_x), (220 + Quit_Button_x, 130 + Quit_Button_x), (100 - Quit_Button_x, 130 + Quit_Button_x)])
                if Quit_Button.collidepoint(mouse_x, mouse_y):
                    Quit_Button_x = 10
                    if mouse1:
                        Paused = 0
                elif not Quit_Button.collidepoint(mouse_x, mouse_y):
                    Quit_Button_x = 0
                message_display("Back", (160, 105), 65, green)

                if minigame == "inventory":
                    if animation == "a":
                        screen.blit(inv_aimg, (0, 0))
                    if animation == "b":
                        screen.blit(inv_bimg, (0, 0))
                    if animation == "c":
                        screen.blit(inv_cimg, (0, 0))

                    if equipped == "cookbook":
                        screen.blit(cookbook_largeimg, (815, 700))
                        if not "cookbook" in inventory:
                            equipped = 0

                    if "cookbook" in inventory:
                        if slot1open == "cookbook" and cookbookicon_exception == 0:
                            cookbookicon_x = 162
                            cookbookicon_y = 248
                        if slot2open == "cookbook" and cookbookicon_exception == 0:
                            cookbookicon_x = 588
                            cookbookicon_y = 248
                        if slot3open == "cookbook" and cookbookicon_exception == 0:
                            cookbookicon_x = 1046
                            cookbookicon_y = 248
                        if slot4open == "cookbook" and cookbookicon_exception == 0:
                            cookbookicon_x = 1488
                            cookbookicon_y = 248

                        cookbookicon = screen.blit(cookbook_largeimg, (cookbookicon_x, cookbookicon_y))
                        if cookbookicon.collidepoint(mouse_x, mouse_y) and mouse1 == 1:
                            if grabbed == 0 or grabbed == "cookbook":
                                grabbed = "cookbook"
                                cookbookicon_exception = 1
                                cookbookicon_x = mouse_x - 110
                                cookbookicon_y = mouse_y - 110
                                if cookbookicon_y < 450:
                                    if cookbookicon_x < 250 and slot1open == 1:
                                        slot1open = "cookbook"
                                        if slot2open == "cookbook":
                                            slot2open = 1
                                        if slot3open == "cookbook":
                                            slot3open = 1
                                        if slot4open == "cookbook":
                                            slot4open = 1
                                    if cookbookicon_x > 250 and cookbookicon_x < 800 and slot2open == 1:
                                        slot2open = "cookbook"
                                        if slot1open == "cookbook":
                                            slot1open = 1
                                        if slot3open == "cookbook":
                                            slot3open = 1
                                        if slot4open == "cookbook":
                                            slot4open = 1
                                    if cookbookicon_x > 800 and cookbookicon_x < 1200 and slot3open == 1:
                                        slot3open = "cookbook"
                                        if slot1open == "cookbook":
                                            slot1open = 1
                                        if slot2open == "cookbook":
                                            slot2open = 1
                                        if slot4open == "cookbook":
                                            slot4open = 1
                                    if cookbookicon_x > 1200 and slot4open == 1:
                                        slot4open = "cookbook"
                                        if slot1open == "cookbook":
                                            slot1open = 1
                                        if slot2open == "cookbook":
                                            slot2open = 1
                                        if slot3open == "cookbook":
                                            slot3open = 1
                                elif cookbookicon_y > 450 and cookbookicon_x > 650 and cookbookicon_x < 950:
                                    equipped = "cookbook"
                        else:
                            cookbookicon_exception = 0

                        if cookbookicon.collidepoint(mouse_x, mouse_y) and mouse2 == 1:
                            inventory.remove("cookbook")
                            if slot1open == "cookbook":
                                slot1open = 1
                            elif slot2open == "cookbook":
                                slot2open = 1
                            elif slot3open == "cookbook":
                                slot3open = 1
                            elif slot4open == "cookbook":
                                slot4open = 1

                    if not grabbed == "cookbook": #add all items here
                        grabbed = 0

                if minigame == "cooking":
                    if animation == "a":
                        screen.blit(carrot_aimg, (mouse_x, mouse_y))
                    if animation == "b":
                        screen.blit(carrot_bimg, (mouse_x, mouse_y))
                    if animation == "c":
                        screen.blit(carrot_cimg, (mouse_x, mouse_y))

    if mouse_visi == 1:
        if animation == "a":
            screen.blit(cursor_aimg, (mouse_x, mouse_y))
        if animation == "b":
            screen.blit(cursor_bimg, (mouse_x, mouse_y))
        if animation == "c":
            screen.blit(cursor_cimg, (mouse_x, mouse_y))
    pygame.time.wait(10)
    pygame.display.flip()
    if Area == "Outside":
        screen.fill((155, 155, 255))
    if Area == "Joe's":
        screen.fill((234, 162, 162))
    if Area == "Home":
        screen.fill((255, 255, 155))
exit()
