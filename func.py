import pygame, sys
from city_center import City_center

def events(screen, settlers, citieses):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                cities = City_center(screen, event.pos[0], event.pos[1], settlers)
                citieses.append(cities)
            if event.button == 3:
                citieses[0].spawn = True

                
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3:
                citieses[0].spawn = False


def move(setl):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_a:
                setl.left_move = True
            if event.key == pygame.K_d:
                setl.right_move = True
            if event.key == pygame.K_w:
                setl.up_move = True
            if event.key == pygame.K_s:
                setl.down_move = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                setl.left_move = False
            if event.key == pygame.K_d:
                setl.right_move = False
            if event.key == pygame.K_w:
                setl.up_move = False
            if event.key == pygame.K_s:
                setl.down_move = False

def select(self):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                right = self.rect.right
                left = self.rect.left
                up = self.rect.top
                down = self.rect.bottom
                if (right < event.pos[0] < left) and (down < event.pos[1] < up):
                    select_object = self
                    return select_object