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
        select_obj = 0
        clock.tick(config.FPS)

#------------------------------------------------------------ отдел обработки событий
        func.events(screen, setlers, citieses)
        for i in citieses:
            i.spawn_setl()
        for i in setlers:
            i.select()
        all_object = setlers + citieses

        func.move(select_obj)

#------------------------------------------------------------- отдел рендеринга
        screen.fill(config.bg_color)
        for i in all_object:
            i.output()
        pygame.display.flip()
