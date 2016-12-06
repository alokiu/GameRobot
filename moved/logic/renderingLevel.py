from moved.entity.platform import Platform
from moved.entity.block import Block
import pygame


def renderLevel(level,  hero):
    sprite_group = pygame.sprite.Group()
    sprite_group.add(hero)
    platforms = []
    kill_group = []
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == '*':
                pl = Platform(x, y)
                sprite_group.add(pl)
                platforms.append(pl)
            if col == "|":
                if y == 320:
                    y += 10
                else:
                    y += 5
                pl = Block(x, y)
                sprite_group.add(pl)
                platforms.append(pl)
                kill_group.append(pl)
                if y == 330:
                    y -= 10
                else:
                    y -= 5
            x += 40
        y += 40
        x = 0
    return sprite_group,platforms,kill_group