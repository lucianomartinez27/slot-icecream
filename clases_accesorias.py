import pygame
class Images():
    def __init__(self, image_file, location, resizable=False, new_size=None): 
        self.image = pygame.image.load(image_file)
        if resizable:
            self.image = pygame.transform.scale(self.image, new_size)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.corner = ((self.rect.centerx - 70), (self.rect.centery - 70))


class Fonts():
    def __init__(self, type_font, text_font, size_font, color_font, position=(0, 0)):
        self.fonts = pygame.font.Font(type_font, size_font)
        self.fonts = self.fonts.render(text_font, True, color_font)
        self.rect = self.fonts.get_rect()
        self.rect.centerx, self.rect.centery = position