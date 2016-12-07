import pygame

from conroler.createFileLevel import NewFile
from moved.entity.Hero import Hero
from moved.logic.controlGame import Control
from moved.logic.functionOfCamera import camera_funk
from moved.logic.renderingLevel import renderLevel
from view.camera import Camera
from view.menu import Menu
from view.nexrLevel import NextLevel
from view.workWithFile import File

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
font_point = pygame.font.SysFont('System',40,True,True)

#Создаем уровень
NewFile.createLevel()
level = File.readOfFileByte('fileLevel\level1.bat')
sprite_group, platforms , kill_group = renderLevel(level, hero)

#Создаем меню
punkts = [(260,100,u'Game',(200,200,200),(0,250,0),0),
          (275,190,u'Help',(200,200,200),(0,250,0),1),
          (265, 290, u'Quit',(200, 200, 200),(0, 250, 0),2)]
game = Menu(punkts)
game.mainMeny(screen, window, hero)

#Камера

total_level_wigth = len(level[0]) * 40 +5000
total_level_heigth = len(level) * 40
camera = Camera(camera_funk, total_level_wigth, total_level_heigth, SIZE)

done = True
timer = pygame.time.Clock()

while done:
    #Убираем значек мышки
    pygame.mouse.set_visible(False)

    #Блок управления событиями
    Control.contolGame(hero,game,window, screen)

    #Закрашивание поверхнсти
    screen.fill((0,210,255))

    #Отображение холста
    screen.blit(font_point.render(u'Point: ' + str(int(hero.points)),1,(250,00,0)),(600,25))
    screen.blit(font_point.render(str((alllevel[index].split('.')[0])), 1, (250, 0, 0)), (30, 25))
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
        NextLevel.informationAboutNextLevel(screen, window, hero)
    elif hero.rect.x >= 4400 and alllevel[index] == 'level2.bat':
        level = File.readOfFileByte('fileLevel\level3.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        hero.xSpeed -= 0.2
        NextLevel.informationAboutNextLevel(screen, window, hero)
    elif hero.rect.x >= 4900 and alllevel[index] == 'level3.bat':
        level = File.readOfFileByte('fileLevel\level4.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        hero.xSpeed -=0.2
        NextLevel.informationAboutNextLevel(screen, window, hero)
    elif hero.rect.x >= 5400 and alllevel[index] == 'level4.bat':
        level = File.readOfFileByte('fileLevel\level5.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        NextLevel.informationAboutNextLevel(screen, window)
    elif hero.rect.x >= 5900 and alllevel[index] == 'level5.bat':
        level = File.readOfFileByte('fileLevel\level6.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        NextLevel.informationAboutNextLevel(screen, window, hero)
    elif hero.rect.x >= 6400 and alllevel[index] == 'level6.bat':
        level = File.readOfFileByte('fileLevel\level7.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        NextLevel.informationAboutNextLevel(screen, window, hero)
    elif hero.rect.x >= 6900 and alllevel[index] == 'level7.bat':
        level = File.readOfFileByte('fileLevel\level8.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        NextLevel.informationAboutNextLevel(screen, window)
    elif hero.rect.x >= 7400 and alllevel[index] == 'level8.bat':
        level = File.readOfFileByte('fileLevel\level9.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        index += 1
        NextLevel.informationAboutNextLevel(screen, window, hero)
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
    timer.tick(40)