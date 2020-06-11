import random
from slotmachine import SlotMachine
import pygame
from pygame.locals import *

pygame.mixer.init()
pygame.mixer.music.load("sounds/back.mp3")
pygame.init()

f = open("dificultad.txt", 'r')
dificultad = int(f.read())
f.close()

slot = SlotMachine(1200, 700, "Via 25 - HELADOS")
pygame.display.set_caption(slot.game_title)

start = True # intro
waiting = True # shows "JUGAR"
x = 75 # First ice cream position
x2 = 250
x3 = 425
y = 150 # Ice cream position
play = 0 # This is so that you can stop the ice cream individually
counter = 0 # Count the times the ice creams spin
speed = 5 # How fast the ice creams spin

pos_wx = 150 # This positions are used to the "waiting ice creams movement" and confetti effect
pos_wy = -150

while 1:
    if start: # Presentation: logos.
        slot.screen.fill([255, 255, 255])
        # slot.screen.blit(slot.startimage.image, slot.startimage.rect)
        # pygame.display.update()
        # pygame.time.wait(1000)
        # slot.screen.fill([255, 255, 255])
        # slot.screen.blit(slot.demas_logo.image, slot.demas_logo.rect)
        slot.screen.blit(slot.eric_font.fonts, slot.eric_font.rect)
        pygame.display.update()
        pygame.time.wait(2500)
        start = False

        # Background music
        pygame.mixer.music.play(-1)

        # Choice aleatory the images to show in waiting screen
        i0, i1, i2 = random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)

    if waiting: # Screen before press ENTER and play
        slot.get_spin(dificultad)
        pos_wy += 1
        slot.screen.fill([255,255,255])
        slot.screen.blit(slot.play_font.fonts, slot.play_font.rect)
        slot.screen.blit(slot.enter_font.fonts, slot.enter_font.rect)
        slot.screen.blit(slot.ice_cream_list[i0].image, (pos_wx, pos_wy))
        slot.screen.blit(slot.ice_cream_list[i1].image, (pos_wx+400, pos_wy))
        slot.screen.blit(slot.ice_cream_list[i2].image, (pos_wx+800, pos_wy))
        pygame.time.delay(3)
        pygame.display.update()
        if pos_wy > slot.screen_size[1]: # Up the images of the three ice creams
            pos_wy = -150
            i0, i1, i2 = random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)

    if play == 1 and counter != 6: # The spinning of ice cream, but not the choiced
        y += speed
        slot.screen.fill([255, 255, 255])
        slot.screen.blit(slot.ice_cream_list[i0].image, (x, y))
        slot.screen.blit(slot.ice_cream_list[i1].image, (x2, y))
        slot.screen.blit(slot.ice_cream_list[i2].image, (x3, y))
        slot.screen.blit(slot.machine.image, (0,0))
        pygame.display.update()
    elif counter == 6 and y < 215: # This is so that the choiced is also shown going down
        y += speed
        slot.screen.fill([255, 255, 255])
        slot.screen.blit(slot.results[0].image, (x, y))
        slot.screen.blit(slot.ice_cream_list[i1].image, (x2, y))
        slot.screen.blit(slot.ice_cream_list[i2].image, (x3, y))
        slot.screen.blit(slot.machine.image, (0,0))
        pygame.display.update()

    elif play == 2 and counter != 10: # same above
        y += speed
        slot.screen.fill([255, 255, 255])
        slot.screen.blit(slot.results[0].image, (x, 225))
        slot.screen.blit(slot.ice_cream_list[i1].image, (x2, y))
        slot.screen.blit(slot.ice_cream_list[i2].image, (x3, y))
        slot.screen.blit(slot.machine.image, (0,0))
        pygame.display.update()
    elif counter == 10 and y < 215: # same above
        y += speed
        slot.screen.fill([255, 255, 255])
        slot.screen.blit(slot.results[0].image, (x, 225))
        slot.screen.blit(slot.results[1].image, (x2, y))
        slot.screen.blit(slot.ice_cream_list[i2].image, (x3, y))
        slot.screen.blit(slot.machine.image, (0,0))
        pygame.display.update()
    elif play == 3 and counter != 12: # same
        y += speed
        slot.screen.fill([255, 255, 255])
        slot.screen.blit(slot.results[0].image, (x, 225))
        slot.screen.blit(slot.results[1].image, (x2, 225))
        slot.screen.blit(slot.ice_cream_list[i2].image, (x3, y))
        slot.screen.blit(slot.machine.image, (0,0))
        pygame.display.update()
    elif counter == 12 and y < 225: # same
        y += speed
        slot.screen.fill([255, 255, 255])
        slot.screen.blit(slot.results[0].image, (x, 225))
        slot.screen.blit(slot.results[1].image, (x2, 225))
        slot.screen.blit(slot.results[2].image, (x3, y))
        slot.screen.blit(slot.machine.image, (0,0))
        pygame.display.update()
    # Here check the results
    elif play == 4: 
        if slot.results[0] == slot.results[1] and slot.results[1] == slot.results[2]:
            pos_wy += speed+10
            slot.screen.fill([255, 255, 255])
            slot.screen.blit(slot.results[0].image, (x, 225))
            slot.screen.blit(slot.results[1].image, (x2, 225))
            slot.screen.blit(slot.results[2].image, (x3, 225))
            slot.screen.blit(slot.machine.image, (0, 0))
            slot.screen.blit(slot.confeti_image.image, (0,pos_wy-1409)) #Show the confetti
            slot.screen.blit(slot.confeti_image.image, (0,pos_wy))
            slot.screen.blit(slot.three_font.fonts, slot.three_font.rect)
            pygame.display.update()
            # Confetti movement
            if pos_wy > slot.screen_size[1]: #[1] is heigth
                counter += 1
                pos_wy = -slot.screen_size[1]
                if counter == 15:
                    play = 0
                    counter = 0
                    waiting = 1
                    pos_wy = 0
        elif slot.results[0] == slot.results[1] or slot.results[1] == slot.results[2]  or slot.results[0] == slot.results[2]:
            slot.screen.blit(slot.two_font.fonts, slot.three_font.rect)
            pygame.display.update()
            pygame.time.delay(2000)
            # Reset al the values to play again
            play = 0
            counter = 0
            waiting = True
        else:
            slot.screen.blit(slot.one_font.fonts, slot.one_font.rect)
            pygame.display.update()
            pygame.time.delay(2000)
            # Reset al the values to play again
            play = 0
            counter = 0
            waiting = True
    # Here count the times the ice creams spins   
    if y > 400:
        counter += 1
        y = 100
        i0, i1, i2 = random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)
        if counter == 6:
            play += 1 # Stop the first ice cream
        elif counter == 10:
            play += 1 # Stop the second ice cream
        elif counter == 12:
            play += 1 # Stop the third ice cream and next show the results

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if event.key == K_RETURN:
                # slot.spinning_snd.play(-1)
                if play == 0: # You can play only you are in the waiting area
                    random.shuffle(slot.ice_cream_list)
                    waiting = False
                    play +=1
