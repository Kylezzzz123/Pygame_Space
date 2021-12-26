# sprite    # sprite is use to show pictures of items  # how to control objects
import pygame
import random

FPS = 60

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255, 0, 0)
YELLOW = (255,255,0)
BLACK = (0, 0, 0)

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
        self.rect.centerx = WIDTH/2        # set the object (Space) to middle x
        self.rect.bottom = HEIGHT - 10     # set the object (Space) to bottom 
        self.speedx = 8                    # set the object (Space) movement to speed 8

    def update(self):  
        key_pressed = pygame.key.get_pressed()   # return boolean value, 
        if key_pressed[pygame.K_RIGHT]:         # press right to go right
            self.rect.x += self.speedx          # speedx = 8
        if key_pressed[pygame.K_LEFT]:          # press left to go left
            self.rect.x -= self.speedx        
        if self.rect.right > WIDTH:             # set the x limit to boudary 
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
       
class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))      # Width and height
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)        # set the object (Space) from random 0 to width of screen - width of rock
        self.rect.y = random.randrange(-100, -40)  # set the object from random -100 to -40 
        self.speedy = random.randrange(2,10)                   # set the object (Rock) movement to speed 2
        self.speedx = random.randrange(-3,3)
    def update(self):  
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)        # set the object (ROCK) from random 0 to width of screen - width of rock
            self.rect.y = random.randrange(-100, -40)  # set the object from random -100 to -40 
            self.speedy = random.randrange(2,10)                   # set the object (Rock) movement y speed from 2 to 10
            self.speedx = random.randrange(-3,3)                   # set the object (Rock) movement x speed from -3 to 3

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10,20))      # Width and height
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y 
        self.speedy = -10       # bullet launches from bottom to top, so the speedy is -10 (negative)
        
    def update(self):  
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()             # kill is from the function of Sprites


all_sprites = pygame.sprite.Group() 
rocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player() 
all_sprites.add(player)
for i in range(8):   # creates 8 rocks
    r = Rock() 
    all_sprites.add(r)
    rocks.add(r)

        
    # Game cycle
running = True
while running: 
    clock.tick(FPS)  # execute at most 10 times in one second
    # input
    for event in pygame.event.get():    #return all events to list
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

        
    # update game
    all_sprites.update() # execute every single item in all_sprites group
    hits = pygame.sprite.groupcollide(bullets, rocks, True, True)    # boolean is to determine if the objects needed to be removed
    for hit in hits:   # after bullets hit rock, use for loop to keep updating the rocks
        r = Rock()
        all_sprites.add(r)
        rocks.add(r)

    hits = pygame.sprite.spritecollide(player, rocks, False)
    if hits:
        running = False

    # show screen
    screen.fill((BLACK))
    all_sprites.draw(screen)    # draw 
    pygame.display.update() 

pygame.quit()
