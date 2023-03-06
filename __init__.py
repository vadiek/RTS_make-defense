import pygame
import func
import config
from settlers import Settlers
from city_center import City_center

def run():
    pygame.init()
    screen = pygame.display.set_mode(config.scren_size)
    pygame.display.set_caption(config.game_name)
    clock = pygame.time.Clock()
    setlers = []
    citieses = []


    while True:
        clock.tick(config.FPS)
        func.events(screen, setlers, citieses)
        for i in citieses:
            i.spawn_setl()
        screen.fill(config.bg_color)
        for i in citieses:
            i.upload()
        for i in setlers:
            i.output()
        pygame.display.flip()
