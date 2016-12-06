import pygame
from moved.entity.Hero import Hero
from moved.entity.block import Block
from moved.entity.platform import Platform
from view.camera import Camera
from view.menu import Menu
from moved.logic.controlGame import Control
from conroler.createFileLevel import NewFile
from view.workWithFile import File
from moved.logic.renderingLevel import renderLevel

SIZE = (800,600)
alllevel = ['level1.bat', 'level2.bat', 'level3.bat', 'level4.bat', 'level5.bat',
         'level6.bat', 'level7.bat', 'level8.bat', 'level9.bat', 'level10.bat']
index = 0

#Создаем окно
window = pygame.display.set_mode(SIZE)
#Создаем рабочую поверхность (игровой экран)
screen = pygame.Surface(SIZE)

#Создание героя
hero = Hero(55, 55)

#Создание шрифта
pygame.font.init()
font_point = pygame.font.SysFont('System',30,True,True)

#Создаем уровень
NewFile.createLevel()
level = File.readOfFileByte('fileLevel\level1.bat')
sprite_group, platforms , kill_group = renderLevel(level, hero)

#Создаем меню
punkts = [(260,140,u'Game',(200,200,200),(0,250,0),0),
          (265, 250, u'Quit',(200, 200, 200),(0, 250, 0),1)]
game = Menu(punkts)
game.mainMeny(screen, window, hero)

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

total_level_wigth = len(level[0]) * 40 +5000
total_level_heigth = len(level) * 40

camera = Camera(camera_funk, total_level_wigth, total_level_heigth)

done = True
timer = pygame.time.Clock()

while done:
    #Убираем значек мышки
    pygame.mouse.set_visible(False)

    #Блок управления событиями
    Control.contolGame(hero,game,window, screen)

    #Закрашивание поверхнсти
    screen.fill((10,120,10))

    #Отображение холста
    screen.blit(font_point.render(u'Point: ' + str(int(hero.points)),1,(210,120,200)),(640,25))
    screen.blit(font_point.render(str((alllevel[index])), 1, (210, 120, 200)), (140, 25))
    #Переход на новый уровень
    if  hero.live == False:
        level = File.readOfFileByte('fileLevel\level1.bat')
        sprite_group, platforms, kill_group = renderLevel(level,hero)
        hero.live = True
        index = 0
    elif (hero.rect.x >= 3900 and alllevel[index] == 'level1.bat'):
        level = File.readOfFileByte('fileLevel\level2.bat')
        sprite_group, platforms, kill_group = renderLevel(level,hero)
        hero.rect.x = 55
        index += 1
        hero.xSpeed -=0.2
    elif hero.rect.x >= 4400 and alllevel[index] == 'level2.bat':
        level = File.readOfFileByte('fileLevel\level3.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        hero.xSpeed -= 0.2
    elif hero.rect.x >= 4900 and alllevel[index] == 'level3.bat':
        level = File.readOfFileByte('fileLevel\level4.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        hero.xSpeed -=0.2
    elif hero.rect.x >= 5400 and alllevel[index] == 'level4.bat':
        level = File.readOfFileByte('fileLevel\level5.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
    elif hero.rect.x >= 5900 and alllevel[index] == 'level5.bat':
        level = File.readOfFileByte('fileLevel\level6.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
    elif hero.rect.x >= 6400 and alllevel[index] == 'level6.bat':
        level = File.readOfFileByte('fileLevel\level7.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
    elif hero.rect.x >= 6900 and alllevel[index] == 'level7.bat':
        level = File.readOfFileByte('fileLevel\level8.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
    elif hero.rect.x >= 7400 and alllevel[index] == 'level8.bat':
        level = File.readOfFileByte('fileLevel\level9.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
    elif hero.rect.x >= 7900 and alllevel[index] == 'level9.bat':
        level = File.readOfFileByte('fileLevel\level10.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
    #Отоброжение героя
    hero.update( platforms, kill_group)
    camera.update(hero)
    for e in sprite_group:
        screen.blit(e.image, camera.apply(e))


    #Отображаем рабочию поверхность в окне
    window.blit(screen,(0,0))

    #Обновляем окно
    pygame.display.flip()

    #Скорость игры
    timer.tick(45)