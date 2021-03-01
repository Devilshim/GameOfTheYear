import os
import sys

import pygame
import time
pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


WIDTH = 800
HEIGHT = 650


class StaticSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Boat.jpg')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 6,
                       self.image.get_height() // 6))
        self.image.set_colorkey()
        self.rect.x = WIDTH - 200
        self.rect.y = HEIGHT - 90
        keys = pygame.key.get_pressed()
        if keys == pygame.KEYUP:
            pos = pygame.mouse.get_pos()
            print(pos)


class StaticSprite1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Book.jpg')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 6,
                       self.image.get_height() // 6))
        self.image.set_colorkey()
        self.rect.x = WIDTH - 500
        self.rect.y = HEIGHT - 450
        keys = pygame.key.get_pressed()
        if keys == pygame.KEYUP:
            pos = pygame.mouse.get_pos()
            print(pos)

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player.png')
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0


    def update(self):
        self.speedx = 1
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
        if self.rect.y > HEIGHT - 100:
            self.rect.y = HEIGHT - 100
        if self.rect.y < 0:
            self.rect.y = 0


class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player2.jpg')
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.centerx = WIDTH / 3
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0




class Player3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player3.jpg')
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.centerx = WIDTH / 6
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0





def main():
    lvl = 0
    size = 800, 650
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('GameOfTheYear')
    all_sprites = pygame.sprite.Group()
    sound_sprites = pygame.sprite.Group()
    hero_sprites = pygame.sprite.Group()
    mouse_sprites = pygame.sprite.Group()
    static_sprites = pygame.sprite.Group()
    static_sprites1 = pygame.sprite.Group()

    playb = pygame.sprite.Sprite()
    playb.image = load_image("Меню.png")
    playb.rect = playb.image.get_rect()
    playb.rect.topleft = (287, 205)
    all_sprites.add(playb)

    sound = pygame.sprite.Sprite()
    sound.image = load_image("Динамик.png")
    sound.rect = sound.image.get_rect()
    sound.rect.topleft = (733, 583)
    sound100 = True
    sound_sprites.add(sound)

    sound1 = pygame.sprite.Sprite()
    sound1.image = load_image("стрелочки.png")
    sound1.rect = sound1.image.get_rect()
    sound1.rect.topleft = (10000, 10000)
    sound_sprites.add(sound1)

    sound2 = pygame.sprite.Sprite()
    sound2.image = load_image("5.png")
    p = 5
    sound2.rect = sound2.image.get_rect()
    sound2.rect.topleft = (10000, 10000)
    sound_sprites.add(sound2)

    pygame.mixer.music.load('E:\YANDEX\GAME\data\AntonioVivaldi.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(1)


    pers = pygame.sprite.Sprite()
    pers.image = load_image("ГП.png")
    pers.rect = pers.image.get_rect()
    pers.rect.topleft = (10000, 10000)
    hero_sprites.add(pers)

    cursor_image = load_image("arrow.png")
    cursor = pygame.sprite.Sprite(mouse_sprites)
    cursor.image = cursor_image
    cursor.rect = cursor.image.get_rect()
    cursor_image2 = load_image("58170b7223cb51581a04b5e3.jvxDD.png")
    cursor2 = pygame.sprite.Sprite(mouse_sprites)
    cursor2.image = cursor_image2
    cursor2.rect = cursor2.image.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    background = load_image('Scream.jpg')
    player = Player1()
    hero_sprites.add(player)
    player1 = Player2()
    hero_sprites.add(player1)
    player2 = Player3()
    hero_sprites.add(player2)
    boat = StaticSprite()
    static_sprites.add(boat)
    book = StaticSprite1()
    static_sprites1.add(book)
    dc = 0
    now = time.time()
    future = now + 45

    while running:
        if lvl == 1:
            if dc == 0:
                pygame.mixer.music.load('E:\YANDEX\GAME\data\DialogK1.mp3')
                pygame.mixer.music.play()
                dc = 1
                if time.time() > future:
                    pygame.mixer.music.load('E:\YANDEX\GAME\data\DialogO1.mp3')
                    pygame.mixer.music.play()
            background = load_image('main.jpg')
            hero_sprites.update()
        elif lvl == 2:
            background = load_image('Room.jpg')
            hero_sprites.update()




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x in range(287, 513)) and (y in range(365, 446)) and lvl == 0:
                    pygame.quit()
                    sys.exit()
                elif (x in range(287, 513)) and (y in range(205, 285)) and lvl == 0:
                    for item in all_sprites:
                        item.kill()
                    lvl = 1
                    print(1)
                elif (x in range(550, 650)) and (y in range(520, 610)) and lvl == 1:
                    for item in all_sprites:
                        item.kill()
                    lvl = 2
                    print(2)
                elif (x in range(300, 400)) and (y in range(200, 300)) and lvl == 2:
                    for item in all_sprites:
                        item.kill()
                    lvl = 3
                    print(3)

                elif (x in range(733, 800)) and (y in range(583, 650)) and sound100 == True:
                    sound.rect.topleft = (10000, 10000)
                    sound1.rect.topleft = (657, 578)
                    sound2.rect.topleft = (657, 618)
                    sound100 = False
                elif (x in range(657, 729)) and (y in range(578, 618)) and sound100 == False:
                    if p == 5:
                        sound2.image = load_image("4.png")
                        pygame.mixer.music.set_volume(0.75)
                        p = 4
                    elif p == 4:
                        sound2.image = load_image("3.png")
                        p = 3
                        pygame.mixer.music.set_volume(0.5)
                    elif p == 3:
                        sound2.image = load_image("2.png")
                        p = 2
                        pygame.mixer.music.set_volume(0.25)
                    elif p == 2:
                        sound2.image = load_image("1.png")
                        p = 1
                        pygame.mixer.music.set_volume(0)
                    else:
                        pass
                elif (x in range(729, 800)) and (y in range(578, 618)) and sound100 == False:
                    if p == 5:
                        pass
                    elif p == 4:
                        sound2.image = load_image("5.png")
                        p = 5
                        pygame.mixer.music.set_volume(1)
                    elif p == 3:
                        sound2.image = load_image("4.png")
                        pygame.mixer.music.set_volume(0.75)
                        p = 4
                    elif p == 2:
                        sound2.image = load_image("3.png")
                        pygame.mixer.music.set_volume(0.5)
                        p = 3
                    elif p == 1:
                        pygame.mixer.music.set_volume(0.25)
                        sound2.image = load_image("2.png")
                        p = 2
                else:
                    sound.rect.topleft = (733, 583)
                    sound1.rect.topleft = (10000, 10000)
                    sound2.rect.topleft = (10000, 10000)
                    sound100 = True

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                if (x in range(287, 513)) and (y in range(205, 285)) and lvl == 0:
                    cursor2.rect.topleft = event.pos
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(287, 513)) and (y in range(285, 366)) and lvl == 0:
                    cursor2.rect.topleft = event.pos
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(287, 513)) and (y in range(365, 446)) and lvl == 0:
                    cursor2.rect.topleft = event.pos
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(733, 800)) and (y in range(583, 650)) and sound100 == True:
                    cursor2.rect.topleft = event.pos
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(657, 800)) and (y in range(578, 618)) and sound100 == False:
                    cursor2.rect.topleft = event.pos
                    cursor.rect.topleft = (10000, 10000)
                else:
                    cursor.rect.topleft = event.pos
                    cursor2.rect.topleft = (10000, 10000)

        background = pygame.transform.scale(background, (800, 650))
        background_rect = background.get_rect()

        screen.blit(background, background_rect)

        if pygame.mouse.get_focused() and lvl == 0:
            all_sprites.draw(screen)
            sound_sprites.draw(screen)
            mouse_sprites.draw(screen)
        elif pygame.mouse.get_focused() and lvl == 1:
            hero_sprites.draw(screen)
            sound_sprites.draw(screen)
            mouse_sprites.draw(screen)
            static_sprites.draw(screen)
        elif pygame.mouse.get_focused() and lvl == 2:
            hero_sprites.draw(screen)
            sound_sprites.draw(screen)
            mouse_sprites.draw(screen)
            static_sprites1.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
