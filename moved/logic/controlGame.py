import pygame, sys
from view.pause import Pause

class Control():
    @staticmethod
    def contolGame(hero, game, window, screen):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    hero.up = True
                if e.key == pygame.K_ESCAPE:
                    game.mainMeny(screen, window, hero)
                if e.key == pygame.K_p:
                    Pause.pauseOfGame(screen, window)


            if e.type == pygame.KEYUP:
                if e.key == pygame.K_SPACE:
                    hero.up = False
                    hero.xSpeed += 0.2
        if hero.live == False:
            game.mainMeny(screen, window, hero)

