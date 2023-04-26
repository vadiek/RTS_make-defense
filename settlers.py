import pygame

class Settlers():

    def __init__(self, screen, centerx, centery):

        self.screen = screen
        self.image = pygame.image.load('image/setler.png')
        self.rect = self.image.get_rect() #определяем прямоугольник объекта
        self.screen_rect = screen.get_rect() #определяем прямоугольник окна
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.movement = True # определяем способность объекта к движению
        self.right_move = False
        self.left_move = False
        self.up_move = False
        self.down_move = False
        self.selected = False
# у каждого объекта есть свой определенный прямоугольник, который имеет свои размеры, значит нажатие должно происходить в диапазоне
# значений, рассмотрим ось x берем координату центра по оси и диапазон будет неаходиться в промежутке от координата - половина размера
# до координата + половина размера
        self.sizex = self.rect.size[0]
        self.sizey = self.rect.size[1]
        self.grani = ((self.rect.centerx - (self.sizex/2)), (self.rect.centerx + (self.sizex/2)), (self.rect.centery - (self.sizey/2)), (self.rect.centery + (self.sizey/2)))
    def output(self):
        self.screen.blit(self.image, self.rect)


    def update(self):
        if self.selected:
            if self.right_move and (self.rect.right < self.screen_rect.right):
                self.rect.centerx += 2
            if self.left_move and (self.rect.left > 0):
                self.rect.centerx -= 2
            if self.up_move and (self.rect.top > 0):
                self.rect.centery -= 2
            if self.down_move and (self.rect.bottom < self.screen_rect.bottom):
                self.rect.centery += 2

    def select(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print('proverka')
            if self.grani[0] < event.pos[0] < self.grani[1] and self.grani[2] < event.pos[1] < self.grani[3]:
                self.selected = True
                self.image = pygame.image.load('image/setler_selected.png')
            else:
                self.selected = False
                self.image = pygame.image.load('image/setler.png')