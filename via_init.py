import random
from clases_accesorias import Images, Fonts
import time
import pygame
from pygame.locals import *

try:
   f = open("dificultad.txt", 'r')
   dificultad = int(f.read(4))
   # perform file operations
finally:
   f.close()

print(dificultad)

BACKGROUND_IMAGE = "images/logo.png"
FRAME_RATE = 10
GAME_TITLE = "Via 25 - El juego"
size = width, height = 1200, 700

pygame.init()

# Set the game clock
clock = pygame.time.Clock()

class SlotMachine:

    def __init__(self):
        # Set all the sounds
        pygame.mixer.init()
        
        pygame.mixer.set_num_channels(2)
        self.bet_snd = pygame.mixer.Sound("sounds/bet_snd.wav")
        self.spin_snd = pygame.mixer.Sound("sounds/spin_snd.ogg")
        self.spinning_snd = pygame.mixer.Sound("sounds/spinning_snd.ogg")
        self.bg_music = pygame.mixer.Sound("sounds/background_msc.wav")
        self.screen = pygame.display.set_mode(size, FULLSCREEN) #FULLSCREEN

        # Start and background logo via 25 & demas
        #self.startimage = Images(BACKGROUND_IMAGE, [width/2, height/2])
        #self.demas_logo = Images("./images/demas_logo.png", [width / 2, height / 2])

        #Load and resize background
        self.background = Images(BACKGROUND_IMAGE, [1000, 525], True, (200, 200))

        # List of images for the slots
        self.images = []
        self.images.append(Images("images/img.png", [(width/2)+350, height/2], True, (150, 150)))
        self.images.append(Images("images/img1.png", [(width/2)+350, height/2], True, (150, 150)))
        self.images.append(Images("images/img2.png", [(width / 2) + 350, height / 2], True, (150, 150)))
        self.images.append(Images("images/img3.png", [(width / 2) + 350, height / 2], True, (150, 150)))
        self.images.append(Images("images/img4.png", [(width / 2) + 350, height / 2], True, (150, 150)))
        self.images.append(Images("images/img5.png", [(width / 2) + 350, height / 2], True, (150, 150)))

        # Slots images
        self.rect1 = Images("images/slot.JPG", ((width/2)-350, height/2), True, (300, 500))
        self.rect2 = Images("images/slot.JPG", ((width/2), height/2), True, (300, 500))
        self.rect3 = Images("images/slot.JPG", ((width/2)+350, height/2), True, (300, 500))

        # Fonts
        self.play_font = Fonts("./fonts/font.ttf", "JUGAR", 200, (0, 0, 0), (width/2, height/2))
        self.one_font = Fonts("./fonts/font.ttf", "Mas suerte la próxima :(", 70, (0, 0, 0), (200, 500))
        self.two_font = Fonts("./fonts/font.ttf", "Acertaste dos. faltó poco.", 70, (0, 0, 0), (200, 500))
        self.three_font = Fonts("./fonts/font.ttf", "GANASTE! Felicitaciones", 70, (0, 0, 0), (200, 500))

        # Results of spinning
        self.results = [1,2,3]

    def get_spin(self, difficult=100):
        for i in range(3):
            # Save the wildcard number as spinned_result
            spinned_result = random.randint(0, difficult)

            if spinned_result in range(0, 20):
                self.results[i] = self.images[0]
            elif spinned_result in range(21, 40):
                self.results[i] = self.images[1]
            elif spinned_result in range(41, 60):
                self.results[i] = self.images[2]
            elif spinned_result in range(61, 82):
                self.results[i] = self.images[3]
            elif spinned_result in range(83, 100):
                self.results[i] = self.images[4]
            elif spinned_result in range(89, 95):
                self.results[i] = self.images[5]
    
    def roll_spin(self):
        t_end = time.time() + 1
        while time.time() < t_end:
            for image in self.images:
                self.screen.fill([255, 255, 255])
                self.screen.blit(slot.rect1.image, slot.rect1.rect)
                self.screen.blit(slot.rect2.image, slot.rect2.rect)
                self.screen.blit(slot.rect3.image, slot.rect3.rect)
                self.screen.blit(image.image, slot.rect1.corner)
                self.screen.blit(image.image, slot.rect2.corner)
                self.screen.blit(image.image, slot.rect3.corner)
                pygame.display.update()
                pygame.time.wait(100)
        self.screen.blit(slot.rect1.image, slot.rect1.rect)
        self.screen.blit(self.results[0].image, slot.rect1.corner)
        t_end1 = time.time() + 1
        while time.time() < t_end1:
            for image in self.images:
                self.screen.blit(image.image, slot.rect2.corner)
                self.screen.blit(image.image, slot.rect3.corner)
                pygame.display.update()
                pygame.time.wait(100)
                self.screen.blit(slot.rect2.image, slot.rect2.rect)
                self.screen.blit(slot.rect3.image, slot.rect3.rect)
                pygame.display.update()
        self.screen.blit(self.results[1].image, slot.rect2.corner)
        t_end3 = time.time() + 1
        while time.time() < t_end3:
            for image in self.images:
                self.screen.blit(image.image, slot.rect3.corner)
                pygame.display.update()
                pygame.time.wait(100)
                self.screen.blit(slot.rect3.image, slot.rect3.rect)
                pygame.display.update()
            self.screen.blit(self.results[2].image, slot.rect3.corner)
            pygame.display.update()
            

slot = SlotMachine()
start = 1

while 1:
    if start == 0:
        slot.screen.fill([255, 255, 255])
        #slot.screen.blit(slot.startimage.image, slot.startimage.rect)
        pygame.display.update()
        pygame.time.wait(4000)
        slot.screen.fill([255, 255, 255])
        #slot.screen.blit(slot.demas_logo.image, slot.demas_logo.rect)
        pygame.display.update()
        pygame.time.wait(4000)
        start = 0

    pygame.display.update()
    slot.screen.fill([255, 255, 255])
    slot.screen.blit(slot.play_font.fonts, slot.play_font.rect)
    #slot.screen.blit(slot.background.image, slot.background.rect)
    #slot.bg_music.play()
    slot.get_spin(dificultad)


    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            if event.key == K_RETURN:
                slot.roll_spin()
                if slot.results[0] == slot.results[1] and slot.results[1] == slot.results[2]:
                    slot.screen.blit(slot.three_font.fonts, slot.rect1.rect.bottomleft)
                    pygame.display.update()
                elif slot.results[0] == slot.results[1] or slot.results[1] == slot.results[2]  or slot.results[0] == slot.results[2]:
                    slot.screen.blit(slot.two_font.fonts, slot.rect1.rect.bottomleft)
                    pygame.display.update()
                else:
                    slot.screen.blit(slot.one_font.fonts, slot.rect1.rect.bottomleft)
                    pygame.display.update()
                pygame.time.wait(2000)
