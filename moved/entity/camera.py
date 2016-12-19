from pygame import Rect

class Camera:
    def __init__(self, camera_funk, width, height, size):
        self.camera_func = camera_funk
        self.state = Rect(0,0,width,height)
        self.size = size

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

