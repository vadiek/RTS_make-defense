import pygame

class Settlers():

    def __init__(self, screen, centerx, centery):

        self.screen = screen
        self.image = pygame.image.load('settlers.png')
        self.rect = self.image.get_rect() #определяем прямоугольник объекта
        self.screen_rect = screen.get_rect() #определяем прямоугольник окна
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.right_move = False
        self.left_move = False
        self.up_move = False
        self.down_move = False

    def output(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.right_move and (self.rect.right < self.screen_rect.right):
            self.rect.centerx += 1
        if self.left_move and (self.rect.left > 0):
            self.rect.centerx -= 1
        if self.up_move and (self.rect.top > 0):
            self.rect.centery -= 1
        if self.down_move and (self.rect.bottom < self.screen_rect.bottom):
            self.rect.centery += 1