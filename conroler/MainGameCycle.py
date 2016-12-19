import pygame

from conroler.createFileLevel import NewFile
from moved.entity.Hero import Hero
from moved.entity.camera import Camera
from moved.logic.controlGame import Control
from moved.logic.functionOfCamera import camera_funk
from moved.logic.renderingLevel import renderLevel
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

    if (len(level[0])-10)*40 <= hero.rect.x :
        index += 1
        level = File.readOfFileByte('fileLevel/' + str((alllevel[index])))
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.rect.x = 55
        hero.xSpeed -= 0.1
        NextLevel.informationAboutNextLevel(screen, window, hero)
    elif hero.live == False:
        level = File.readOfFileByte('fileLevel\level1.bat')
        sprite_group, platforms, kill_group = renderLevel(level, hero)
        hero.live = True
        index = 0
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