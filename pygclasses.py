import pygame

class Images():
    """This class is useful to upload images whit some necessary attributess to work in pygame"""
    def __init__(self, image_file, location, new_size=0): 
        self.image = pygame.image.load(image_file)
        if new_size: #This allow change the size of the image
            self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = location

class Fonts():
    """This class is useful to upload fonts whit some necessary attributess to work in pygame"""
    def __init__(self, type_font, text_font, size_font, color_font, position=(0, 0)):
        self.fonts = pygame.font.Font(type_font, size_font)
        self.fonts = self.fonts.render(text_font, True, color_font)
        self.rect = self.fonts.get_rect()
        self.rect.centerx, self.rect.centery = position