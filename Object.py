import pygame
from pygame.sprite import Sprite

class Img(Sprite):
    def __init__(self, screen, img, x, y, name, offscreen=False):
        super().__init__()
        
        self.screen = screen

        self.name = name
        
        self.image = pygame.image.load(img)
        self.myGroups = []
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.leftM = 0
        self.rightM = 0
        self.upM = 0
        self.downM = 0
        self.offscreen = offscreen

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def move(self):
        self.rect.centerx += self.rightM - self.leftM
        self.rect.centery += self.downM - self.upM
        if not self.offscreen:
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
            elif self.rect.left < 0:
                self.rect.left = 0

            if self.rect.bottom > self.screen_rect.bottom:
                self.rect.bottom = self.screen_rect.bottom
            elif self.rect.top < 0:
                self.rect.top = 0
    def onleftedge(self):
        return self.rect.left <= 0
    def onrightedge(self):
        return self.rect.right >= self.screen_rect.right
    def ontopedge(self):
        return self.rect.top <= 0
    def onbottomedge(self):
        return self.rect.bottom >= self.screen_rect.bottom

class Rect(Sprite):
    def __init__(self, screen, x, y, width, height, color, name, offscreen=False):
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.myGroups = []
        self.name = name

        self.leftM, self.rightM, self.upM, self.downM = 0, 0, 0, 0
        self.offscreen = offscreen
    def blitme(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
    def move(self):
        self.rect.centerx += self.rightM - self.leftM
        self.rect.centery += self.downM - self.upM
        if not self.offscreen:
            if self.rect.right > self.screen_rect.right:
                self.rect.right = self.screen_rect.right
            elif self.rect.left < 0:
                self.rect.left = 0

            if self.rect.bottom > self.screen_rect.bottom:
                self.rect.bottom = self.screen_rect.bottom
            elif self.rect.top < 0:
                self.rect.top = 0
    def onleftedge(self):
        return self.rect.left <= 0
    def onrightedge(self):
        return self.rect.right >= self.screen_rect.right
    def ontopedge(self):
        return self.rect.top <= 0
    def onbottomedge(self):
        return self.rect.bottom >= self.screen_rect.bottom
