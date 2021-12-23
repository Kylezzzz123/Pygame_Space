# sprite    # sprite is use to show pictures of items
import pygame
FPS = 60
WHITE = (255,255,255)
GREEN = (0,255,0)

WIDTH = 500
HEIGHT = 600

# Game initial 
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('SpaceGame by Kyle')
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 200
        
all_sprite = pygame.sprite.Group()
player = Player()
all_sprite.add(player)

        
        
# Game cycle
running = True
while running: 
    clock.tick(10)  # execute at most 10 times in one second
    # input
    for event in pygame.event.get():    #return all events to list
        if event.type == pygame.QUIT:
            running = False
        
    # update game

    # show screen
    screen.fill((WHITE))
    all_sprite.draw(screen)    # draw 
    pygame.display.update() 

pygame.quit()
