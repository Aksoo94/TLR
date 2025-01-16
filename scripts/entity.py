import pygame

class Entity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size

        self.img_scale = 2
        self.speed = 3
        
        self.anim_offset = (-21 * self.img_scale, -23 * self.img_scale)

        self.action = ''
        self.direction = 'down'
        self.set_action('idle', self.direction)

    
    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
    
    def set_action(self, action, direction):
        if action != self.action or direction != self.direction:
            self.direction = direction
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action + '/' + self.direction].copy()
    
    def update(self, movement=(0,0)):
        speed = self.speed
        if movement[0] != 0 and movement[1] != 0:
            speed *= 0.7071
        self.pos[0] += int(movement[0] * speed)
        self.pos[1] += int(movement[1] * speed)

        if movement[0] > 0:
            if movement[1] > 0:
                self.set_action('walk', 'rightdown')
            elif movement[1] < 0:
                self.set_action('walk', 'rightup')
            else:
                self.set_action('walk', self.direction)
        elif movement[0] < 0:
            if movement[1] > 0:
                self.set_action('walk', 'leftdown')
            elif movement[1] < 0:
                self.set_action('walk', 'leftup')
            else:
                self.set_action('walk', self.direction)
        elif movement[1] > 0:
            self.set_action('walk', 'down')
        elif movement[1] < 0:
            self.set_action('walk', 'up')
        else:
            self.set_action('idle', self.direction)
        
        self.animation.update()

    def render(self, surf, offset=(0,0)):
        surf.blit(pygame.transform.scale_by(self.animation.img(), self.img_scale), (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))

class Player(Entity):
    def __init__(self, game, pos, size):
        super().__init__(game, 'player', pos, size)

