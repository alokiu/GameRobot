import pygame
import Level
from camera import Camera
from Hero import Hero
from platform import Platform
from block import Block


SIZE = (800,600)
monitor = [4000,600]

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
#Камера
def camera_funk(camera, target_rect):
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.y + SIZE[1]/2
    w,h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - SIZE[0]), l)
    t = min(0, t)
    t = max(-(camera.height - SIZE[1]), t)
    return pygame.Rect(l, t, w, h)

total_level_wigth = len(level[0]) * 40
total_level_heigth = len(level) * 40

camera = Camera(camera_funk, total_level_wigth, total_level_heigth)

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
            if e.key == pygame.K_SPACE:
                space = True
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_UP:
                up = False
                hero.xSpeed += 0.2


    #Закрашивание поверхнсти
    screen.fill((10,120,10))


    #Отоброжение героя
    hero.update(up, platforms, kill_group)
    camera.update(hero)
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))
    #sprite_group.draw(screen)
    #Отображаем рабочию поверхность в окне
    window.blit(screen,(0,0))

    #Обновляем окно
    pygame.display.flip()

    timer.tick(60)