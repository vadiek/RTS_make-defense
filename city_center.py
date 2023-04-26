import pygame
from settlers import Settlers

class City_center():

    def __init__(self, screen, centerx, centery, setlers):
        self.screen = screen
        self.image = pygame.image.load('image/city_center.png')
        self.rect = self.image.get_rect()  # определяем прямоугольник объекта
        self.screen_rect = screen.get_rect()  # определяем прямоугольник окна
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.movement = False # определяем способность объекта к движению
        self.spawn = False # отвечает за спавн юнитов
        self.setlers = setlers
        self.selected = False

        self.sizex = self.rect.size[0]
        self.sizey = self.rect.size[1]
        self.grani = ((self.rect.centerx - (self.sizex / 2)), (self.rect.centerx + (self.sizex / 2)),
                     (self.rect.centery - (self.sizey / 2)), (self.rect.centery + (self.sizey / 2)))

    def output(self):
        self.screen.blit(self.image, self.rect)

    def spawn_setl(self):
        if self.spawn and self.selected:
            setl = Settlers(self.screen, self.rect.right + 60, self.rect.centery)
            self.setlers.append(setl)

    def select(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print('proverka')
            if self.grani[0] < event.pos[0] < self.grani[1] and self.grani[2] < event.pos[1] < self.grani[3]:
                self.selected = True
                self.image = pygame.image.load('image/city_center_selected.png')
            else:
                self.selected = False
                self.image = pygame.image.load('image/city_center.png')
