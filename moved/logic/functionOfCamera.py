import pygame

def camera_funk(camera, target_rect):
    SIZE = (800, 600)
    l = -target_rect.x + SIZE[0]/2
    t = -target_rect.y + SIZE[1]/2
    w,h = camera.width, camera.height

    l = min(0, l)
    l = max(-(camera.width - SIZE[0]), l)
    t = min(0, t)
    t = max(-(camera.height - SIZE[1]), t)
    return pygame.Rect(l, t, w, h)