import pygame
from scripts.utils import load_image, load_sprite_sheet, Animation
from scripts.entity import Entity, Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.movement = [False, False, False, False]

        self.assets = {
            'player/idle/down': Animation(load_sprite_sheet('player/Idle/Idle_Down.png')), 
            'player/idle/up': Animation(load_sprite_sheet('player/Idle/Idle_Up.png')),
            'player/idle/leftdown': Animation(load_sprite_sheet('player/Idle/Idle_Left_Down.png')),
            'player/idle/leftup': Animation(load_sprite_sheet('player/Idle/Idle_Left_Up.png')),
            'player/idle/rightdown': Animation(load_sprite_sheet('player/Idle/Idle_Right_Down.png')),
            'player/idle/rightup': Animation(load_sprite_sheet('player/Idle/Idle_Right_Up.png')),
            'player/walk/down': Animation(load_sprite_sheet('player/Walk/walk_Down.png'), img_dur=6),
            'player/walk/leftup': Animation(load_sprite_sheet('player/Walk/walk_Left_Up.png'), img_dur=6),
            'player/walk/leftdown': Animation(load_sprite_sheet('player/Walk/walk_Left_Down.png'), img_dur=6),
            'player/walk/rightup': Animation(load_sprite_sheet('player/Walk/walk_Right_Up.png'), img_dur=6),
            'player/walk/rightdown': Animation(load_sprite_sheet('player/Walk/walk_Right_Down.png'), img_dur=6),
            'player/walk/up': Animation(load_sprite_sheet('player/Walk/walk_Up.png'), img_dur=6),
        }

        self.player = Player(self, (400,300), (10,20))
        
        self.scroll = [0,0]

    def update(self):
        while self.running:
            self.screen.fill((50,50,50))

            self.scroll[0] += (self.player.rect().centerx - self.screen.get_width()/2 - self.scroll[0])
            self.scroll[1] += (self.player.rect().centery - self.screen.get_height()/2 - self.scroll[1])
            #render_scroll = (int(self.scroll[0]), int(self.scroll[1])) # uncomment this if you want to center the player
            render_scroll = (0,0) # comment this out if you want to center the player

            self.player.update((self.movement[1] - self.movement[0], self.movement[3] - self.movement[2]))
            self.player.render(self.screen, render_scroll)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        self.movement[0] = False
                    if event.key == pygame.K_d:
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
            
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    Game().update()