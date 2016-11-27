import pygame
from Hero import Hero
from platform import Platform
from block import Block

import Level

SIZE = (800,600)
monitor = [800,600]


#Создаем окно
window = pygame.display.set_mode(SIZE)
#Создаем рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)

#Создание героя
hero = Hero(55, 55)
up = False
level = Level.Level.generationLevel(1,monitor)

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
            if y == 320 :
                y += 10
            else :
                y += 5
            pl = Block(x,y)
            sprite_group.add(pl)
            platforms.append(pl)
            kill_group.append(pl)
            if y == 330:
                y -= 10
            else:
                y -=5
        x += 40
    y += 40
    x = 0


done = True
timer = pygame.time.Clock()
while done:
    #Блок управления событиями
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                up = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                up = False


    #Закрашивание поверхнсти
    screen.fill((10,120,10))


    #Отоброжение героя
    hero.update(up, platforms)
    sprite_group.draw(screen)
    #Отображаем рабочию поверхность в окне
    window.blit(screen,(0,0))

    #Обновляем окно
    pygame.display.flip()

    timer.tick(60)