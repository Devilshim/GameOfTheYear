import pygame
import random
import numpy as np
import os
import sys

WIDTH = 1000
HEIGHT = 1000
FPS = 60


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image




# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game!")
clock = pygame.time.Clock()


class StaticSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Book.jpg')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 6,
                       self.image.get_height() // 6))
        self.image.set_colorkey((255, 255, 255))
        self.rect.x = WIDTH - 120
        self.rect.y = HEIGHT - 90
        keys = pygame.key.get_pressed()
        if keys == pygame.KEYUP:
            pos = pygame.mouse.get_pos()
            print(pos)






class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player.png')
        self.rect = self.image.get_rect()
        self.image.set_colorkey('white')
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0


    def update(self):
        self.speedx = 8
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.rect.x -= self.speedx
        if keystate[pygame.K_RIGHT]:
            self.rect.x += self.speedx
        if keystate[pygame.K_UP]:
            self.rect.y -= self.speedx
        if keystate[pygame.K_DOWN]:
            self.rect.y += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y > HEIGHT - 150:
            self.rect.y = HEIGHT - 150
        if self.rect.y < 0:
            self.rect.y = 0


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
ssp = StaticSprite()
all_sprites.add(ssp)

# Цикл игры
running = True
while running:
    picture_counter = 0
    background = load_image('Scream.jpg')
    background = pygame.transform.scale(background, (1000, 1000))
    background_rect = background.get_rect()
    clock.tick(FPS)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()


    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
