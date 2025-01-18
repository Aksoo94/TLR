import pygame
import os

BASE_IMG_PATH = "assets/"

def load_image(path, scale=1):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    img = pygame.transform.scale_by(img, scale)
    return img

def load_sprite_sheet(img_path, size=(48,64), scale=1):
    img = load_image(img_path, scale)
    sheet = []
    for x in range(img.get_width() // size[0]):
        sheet.append(pygame.transform.scale(img.subsurface((x*size[0], 0, size[0], size[1])), (size[0]*scale, size[1]*scale)))
    return sheet

class Animation:
    def __init__(self, images, img_dur=12, loop=True):
        self.images = images
        self.img_duration = img_dur
        self.loop = loop
        self.frame = 0
        self.done = False
    
    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)
    
    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
            if self.frame >= self.img_duration * len(self.images) - 1:
                self.done = True
    
    def img(self):
        return self.images[int(self.frame / self.img_duration)]
