import pygame
import sys

pygame.init()

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.position = (100, 100)
        self.velocity = 1
        self.image = pygame.image.load("mario-project/sprite/stop1.png")
        self.rect = self.image.get_rect() # Permet de stocker des coordonnées rectangulaires
        self.player = pygame.transform.scale(self.image, (40, 50))

    def update(self):
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_UP]:
        #     self.rect.y -= self.velocity
        # if keys[pygame.K_DOWN]:
        #     self.rect.y += self.velocity

    # def draw(self, surface):
    #     pygame.draw.circle(surface, (255, 0, 0), self.position, 10)

    def move_left(self):
        self.velocity = (-1, self.velocity[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        self.image = pygame.image.load("mario-project/sprite/walkL1.png")
        self.image = pygame.image.load("mario-project/sprite/walkL2.png")
        self.image = pygame.image.load("mario-project/sprite/walkL3.png")
        self.image = pygame.image.load("mario-project/sprite/walkL4.png")

    def move_right(self):
        self.velocity = (1, self.velocity[1])
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity
        self.image = pygame.image.load("mario-project/sprite/walkR1.png")
        self.image = pygame.image.load("mario-project/sprite/walkR2.png")
        self.image = pygame.image.load("mario-project/sprite/walkR3.png")
        self.image = pygame.image.load("mario-project/sprite/walkR4.png")

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width ,screen_height))

ciel = pygame.image.load("mario-project/template/background.jpg")
platform = pygame.image.load("mario-project/template/texture/ground9.png")

running = True
while running:
    screen.blit(ciel, (0, 0))
    screen.blit(platform, (0, 698))
    player = Player()
    screen.blit(player.player, player.position)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()