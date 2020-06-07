import pygame
import random
from clases_accesorias import Images, Fonts

class SlotMachine:
    def __init__(self, width, height, title):
        self.screen_size = (width, height)
        self.game_title = title
        pygame.mixer.set_num_channels(2)
        #self.win = pygame.mixer.Sound("sounds/win.wav")
        self.spin_snd = pygame.mixer.Sound("sounds/spin_snd.ogg")
        self.spinning_snd = pygame.mixer.Sound("sounds/spinning_snd.ogg")
        self.screen = pygame.display.set_mode(self.screen_size) # you can set FULLSCREEN, as second paremeter

        # Start and background logo via 25 & demas
        self.startimage = Images("images/logo.png", [width/2, height/2])
        self.demas_logo = Images("./images/demas_logo.png", [width / 2, height / 2])
        self.confeti_image = Images("./images/confeti2.png",[width / 2, height / 2])

        #Load and resize background
        self.background = Images("images/logo.png", [1000, 525], (200, 200))

        # List of images for the slots
        self.images = []
        self.images.append(Images("images/img.png", [(width/2)+350, height/2], (100, 100)))
        self.images.append(Images("images/img1.png", [(width/2)+350, height/2], (100, 100)))
        self.images.append(Images("images/img2.png", [(width / 2) + 350, height / 2], (100, 100)))
        self.images.append(Images("images/img3.png", [(width / 2) + 350, height / 2], (100, 100)))
        self.images.append(Images("images/img4.png", [(width / 2) + 350, height / 2], (100, 100)))
        self.images.append(Images("images/img5.png", [(width / 2) + 350, height / 2], (100, 100)))

        #Machine image
        self.machine = Images("images/machine.png", ((width/2), height/2), (width, height))

        # Fonts
        self.play_font = Fonts("./fonts/font.ttf", "JUGAR", 200, (0, 0, 0), (width/2, height/2))
        self.one_font = Fonts("./fonts/font.ttf", "Mas suerte la próxima :(", 70, (0, 0, 0), (200, 500))
        self.two_font = Fonts("./fonts/font.ttf", "Acertaste dos. faltó poco.", 70, (0, 0, 0), (200, 500))
        self.three_font = Fonts("./fonts/font.ttf", "GANASTE! Felicitaciones", 70, (0, 0, 0), (200, 500))

        # Results of spinning
        self.results = [None, None, None]

    def get_spin(self, difficult=5):
        """ This method is used to choice the result of the spins """
        for i in range(3):
            # This is allow us set the difficult of the game.
            # For example, if "difficult = 1" you always win.
            # Becouse the result will always be self.images[0]
            spinned_result = random.randint(0, difficult)

            if spinned_result in range(0):
                self.results[i] = self.images[0]
            elif spinned_result in range(1, 2):
                self.results[i] = self.images[1]
            elif spinned_result in range(2, 3):
                self.results[i] = self.images[2]
            elif spinned_result in range(3, 4):
                self.results[i] = self.images[3]
            elif spinned_result in range(4, 5):
                self.results[i] = self.images[4]
            elif spinned_result in range(5, 6):
                self.results[i] = self.images[5]