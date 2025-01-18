import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

all_sprites = pygame.sprite.Group()


class Bomb(pygame.sprite.Sprite):
    image = pygame.image.load('bomb2.png').convert_alpha()
    BOMB_WIDTH = image.get_width()
    BOMB_HEIGHT = image.get_height()

    def __init__(self, x1, y1):
        super().__init__(all_sprites)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x1, y1)
        self.mask = pygame.mask.from_surface(self.image)


class Boom(pygame.sprite.Sprite):
    image = pygame.image.load('boom.png').convert_alpha()
    BOOM_WIDTH = image.get_width()
    BOOM_HEIGHT = image.get_height()

    def __init__(self, x1, y1):
        super().__init__(all_sprites)
        self.image = Boom.image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x1, y1)


for _ in range(10):
    while True:
        x = random.randint(0, SCREEN_WIDTH - Bomb.BOMB_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT - Bomb.BOMB_HEIGHT)
        new_bomb = Bomb(x, y)

        collision = False

        for sprite in all_sprites:
            if sprite != new_bomb:
                if new_bomb.rect.colliderect(sprite.rect):
                    if pygame.sprite.collide_mask(new_bomb, sprite):
                        collision = True
                        break
        if not collision:
            break
        else:
            new_bomb.kill()

clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bomb in all_sprites:
                if bomb.rect.collidepoint(event.pos):
                    x, y = bomb.rect.x, bomb.rect.y
                    bomb.kill()
                    boom = Boom(x, y)

    all_sprites.update()
    screen.fill('white')

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
