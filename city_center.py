import pygame
from settlers import Settlers

class City_center():

    def __init__(self, screen, centerx, centery, setlers):
        self.screen = screen
        self.image = pygame.image.load('city_center.png')
        self.rect = self.image.get_rect()  # определяем прямоугольник объекта
        self.screen_rect = screen.get_rect()  # определяем прямоугольник окна
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.spawn = False
        self.setlers = setlers

    def upload(self):
        self.screen.blit(self.image, self.rect)

    def spawn_setl(self):
        if self.spawn:
            setl = Settlers(self.screen, self.rect.right + 60, self.rect.centery)
            self.setlers.append(setl)

