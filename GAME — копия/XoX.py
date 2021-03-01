import os
import sys
import pygame  # Импортируем нужные библиотеки
import time

pygame.init()


# Функция для загрузки изображения с компьютера
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим и пишем, что такого файла нет
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


# Размеры нашего окна
WIDTH = 800
HEIGHT = 650


# Класс объекта с которым будет взаимодействие
class StaticSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Boat.jpg')  # Загружем изображение
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 6,
                         self.image.get_height() // 6))  # Размеры
        self.image.set_colorkey()
        self.rect.x = WIDTH - 200  # Расположение
        self.rect.y = HEIGHT - 90
        keys = pygame.key.get_pressed()
        if keys == pygame.KEYUP:
            pos = pygame.mouse.get_pos()
            print(pos)


# Еще один класс объекта с которым будет взаимодействие
class StaticSprite1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Book.jpg')  # Его картинка
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(
            self.image, (self.image.get_width() // 6,  # Размеры
                         self.image.get_height() // 6))
        self.image.set_colorkey()
        self.rect.x = WIDTH - 500  # Расположение
        self.rect.y = HEIGHT - 450
        keys = pygame.key.get_pressed()
        if keys == pygame.KEYUP:
            pos = pygame.mouse.get_pos()
            print(pos)


# Класс 1-го игрока
class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player.png')  # Картинка
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.centerx = WIDTH / 2  # Расположение
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0  # Параметр скорости

    # Движение 1-го игрока
    def update(self):
        self.speedx = 1
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:  # Влево
            self.rect.x -= self.speedx
        if keystate[pygame.K_RIGHT]:  # Вправо
            self.rect.x += self.speedx
        if keystate[pygame.K_UP]:  # Вверх
            self.rect.y -= self.speedx
        if keystate[pygame.K_DOWN]:  # Вниз
            self.rect.y += self.speedx
        if self.rect.right > WIDTH:  # Далее не даем нашему герою выйти за рамки окна
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.y > HEIGHT - 100:
            self.rect.y = HEIGHT - 100
        if self.rect.y < 0:
            self.rect.y = 0


# Класс 2-го игрока
class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player2.jpg')  # Картинка
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.centerx = WIDTH / 3  # Расположение
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0  # Параметр скорости


# Класс 2-го игрока
class Player3(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100, 100))
        self.image = load_image('Player3.jpg')  # Картинка
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))
        self.rect.centerx = WIDTH / 6  # Расположение
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0  # Параметр скорости


def main():
    lvl = 0
    size = 800, 650  # Размеры окна
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('GameOfTheYear')
    all_sprites = pygame.sprite.Group()  # Создаем группы спрайтов
    sound_sprites = pygame.sprite.Group()
    hero_sprites = pygame.sprite.Group()
    mouse_sprites = pygame.sprite.Group()
    static_sprites = pygame.sprite.Group()
    static_sprites1 = pygame.sprite.Group()

    playb = pygame.sprite.Sprite()  # Делаем спрайт, загружаем картинку, ставим расположение, добавляем в нужную группу спрайтов
    playb.image = load_image("Меню.png")
    playb.rect = playb.image.get_rect()
    playb.rect.topleft = (287, 205)
    all_sprites.add(playb)

    sound = pygame.sprite.Sprite()  # Делаем спрайт, загружаем картинку, ставим расположение, добавляем в нужную группу спрайтов
    sound.image = load_image("Динамик.png")
    sound.rect = sound.image.get_rect()
    sound.rect.topleft = (733, 583)
    sound100 = True
    sound_sprites.add(sound)

    sound1 = pygame.sprite.Sprite()  # Делаем спрайт, загружаем картинку, ставим расположение, добавляем в нужную группу спрайтов
    sound1.image = load_image("стрелочки.png")
    sound1.rect = sound1.image.get_rect()
    sound1.rect.topleft = (10000, 10000)
    sound_sprites.add(sound1)

    sound2 = pygame.sprite.Sprite()  # Делаем спрайт, загружаем картинку, ставим расположение, добавляем в нужную группу спрайтов
    sound2.image = load_image("5.png")
    p = 5
    sound2.rect = sound2.image.get_rect()
    sound2.rect.topleft = (10000, 10000)
    sound_sprites.add(sound2)

    pygame.mixer.music.load(
        'C:\\Users\\IRINA\\PycharmProjects\\untitled2\\123\\GameOfTheYear-main\\GAME — копия\\data\\AntonioVivaldi.mp3')  # Загружаем музыку
    pygame.mixer.music.play()  # Проигрываем ее
    pygame.mixer.music.set_volume(1)

    pers = pygame.sprite.Sprite()  # Делаем спрайт, загружаем картинку, ставим расположение, добавляем в нужную группу спрайтов
    pers.image = load_image("ГП.png")
    pers.rect = pers.image.get_rect()
    pers.rect.topleft = (10000, 10000)
    hero_sprites.add(pers)

    cursor_image = load_image("arrow.png")  # Загружем картинку курсора
    cursor = pygame.sprite.Sprite(mouse_sprites)  # Определяем в группу спрайтов мышки
    cursor.image = cursor_image  # Устанавливаем картинку
    cursor.rect = cursor.image.get_rect()
    cursor_image2 = load_image("58170b7223cb51581a04b5e3.jvxDD.png")  # Загружем картинку курсора
    cursor2 = pygame.sprite.Sprite(mouse_sprites)  # Определяем в группу спрайтов мышки
    cursor2.image = cursor_image2  # Устанавливаем картинку
    cursor2.rect = cursor2.image.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    background = load_image('Scream.jpg')  # Ставим картинку на задний фон
    player = Player1()  # Создаю отдельные группы спрайтов
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
    now = time.time()  # Задаемм время
    future = now + 45

    while running:
        if lvl == 1:  # Первый лвл нашей игры
            if dc == 0:
                pygame.mixer.music.load(
                    'C:\\Users\\IRINA\\PycharmProjects\\untitled2\\123\\GameOfTheYear-main\\GAME — копия\\data\\DialogK1.mp3')  # Монолог автора
                pygame.mixer.music.play()
                dc = 1
                if time.time() > future:
                    pygame.mixer.music.load(
                        'C:\\Users\\IRINA\\PycharmProjects\\untitled2\\123\\GameOfTheYear-main\\GAME — копия\\data\\DialogO1.mp3')  # Монолог одного из персонажей
                    pygame.mixer.music.play()
            background = load_image('main.jpg')  # Меняем картинку заднего фона
            hero_sprites.update()
        elif lvl == 2:  # Второй лвл нашей игры
            background = load_image('Room.jpg')  # Меняем картинку заднего фона
            hero_sprites.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Если выходим, то игра закрывается
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:  # Если нажимается ЛКМ, то
                x, y = event.pos  # Считываем позицию курсора
                if (x in range(287, 513)) and (
                        y in range(365, 446)) and lvl == 0:  # Если мышка в этом диапозоне по х и у, то
                    pygame.quit()  # Выходим из игры
                    sys.exit()
                elif (x in range(287, 513)) and (
                        y in range(205, 285)) and lvl == 0:  # Если мышка в этом диапозоне по х и у, то
                    for item in all_sprites:  # Перебираем элементы all_sprites
                        item.kill()  # И удаляем их
                    lvl = 1
                elif (x in range(287, 513)) and (
                        y in range(285, 366)) and lvl == 0:  # Если мышка в этом диапозоне по х и у, то
                    print('Сохраняю....')
                    pygame.time.wait(2000)  # Тут без комментариев :3
                    print('Сохранение завершено!')
                elif (x in range(550, 650)) and (
                        y in range(520, 610)) and lvl == 1:  # Если мышка в этом диапозоне по х и у, то
                    for item in all_sprites:  # Перебираем элементы all_sprites
                        item.kill()  # И удаляем их
                    lvl = 2
                elif (x in range(300, 400)) and (
                        y in range(200, 300)) and lvl == 2:  # Если мышка в этом диапозоне по х и у, то
                    for item in all_sprites:  # Перебираем элементы all_sprites
                        item.kill()  # И удаляем их
                    lvl = 3

                elif (x in range(733, 800)) and (
                        y in range(583, 650)) and sound100 == True:  # Если мышка в этом диапозоне по х и у, то
                    sound.rect.topleft = (10000, 10000)  # Меняем картинки звука
                    sound1.rect.topleft = (657, 578)
                    sound2.rect.topleft = (657, 618)
                    sound100 = False
                elif (x in range(657, 729)) and (
                        y in range(578, 618)) and sound100 == False:  # Если мышка в этом диапозоне по х и у, то
                    if p == 5:
                        sound2.image = load_image("4.png")  # Меняем картинку
                        pygame.mixer.music.set_volume(0.75)  # Уменьшаем звук
                        p = 4
                    elif p == 4:
                        sound2.image = load_image("3.png")  # Меняем картинку
                        p = 3
                        pygame.mixer.music.set_volume(0.5)  # Уменьшаем звук
                    elif p == 3:
                        sound2.image = load_image("2.png")  # Меняем картинку
                        p = 2
                        pygame.mixer.music.set_volume(0.25)  # Уменьшаем звук
                    elif p == 2:
                        sound2.image = load_image("1.png")  # Меняем картинку
                        p = 1
                        pygame.mixer.music.set_volume(0)  # Уменьшаем звук
                    else:
                        pass
                elif (x in range(729, 800)) and (
                        y in range(578, 618)) and sound100 == False:  # Если мышка в этом диапозоне по х и у, то
                    if p == 5:
                        pass
                    elif p == 4:
                        sound2.image = load_image("5.png")  # Меняем картинку
                        p = 5
                        pygame.mixer.music.set_volume(1)  # Увеличиваем звук
                    elif p == 3:
                        sound2.image = load_image("4.png")  # Меняем картинку
                        pygame.mixer.music.set_volume(0.75)  # Увеличиваем звук
                        p = 4
                    elif p == 2:
                        sound2.image = load_image("3.png")  # Меняем картинку
                        pygame.mixer.music.set_volume(0.5)  # Увеличиваем звук
                        p = 3
                    elif p == 1:
                        pygame.mixer.music.set_volume(0.25)  # Увеличиваем звук
                        sound2.image = load_image("2.png")  # Меняем картинку
                        p = 2
                else:
                    sound.rect.topleft = (733, 583)  # Убираем ненужные картинки
                    sound1.rect.topleft = (10000, 10000)
                    sound2.rect.topleft = (10000, 10000)
                    sound100 = True

            if event.type == pygame.MOUSEMOTION:  # Если мышка двигается, то
                x, y = event.pos  # Считываем позицию мышки
                if (x in range(287, 513)) and (
                        y in range(205, 285)) and lvl == 0:  # Если мышка в этом диапозоне по х и у, то
                    cursor2.rect.topleft = event.pos  # Меняем курсор
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(287, 513)) and (
                        y in range(285, 366)) and lvl == 0:  # Если мышка в этом диапозоне по х и у, то
                    cursor2.rect.topleft = event.pos  # Меняем курсор
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(287, 513)) and (
                        y in range(365, 446)) and lvl == 0:  # Если мышка в этом диапозоне по х и у, то
                    cursor2.rect.topleft = event.pos  # Меняем курсор
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(733, 800)) and (
                        y in range(583, 650)) and sound100 == True:  # Если мышка в этом диапозоне по х и у, то
                    cursor2.rect.topleft = event.pos  # Меняем курсор
                    cursor.rect.topleft = (10000, 10000)
                elif (x in range(657, 800)) and (
                        y in range(578, 618)) and sound100 == False:  # Если мышка в этом диапозоне по х и у, то
                    cursor2.rect.topleft = event.pos  # Меняем курсор
                    cursor.rect.topleft = (10000, 10000)
                else:
                    cursor.rect.topleft = event.pos  # Меняем курсор
                    cursor2.rect.topleft = (10000, 10000)
        # Отрисовка заднего фона
        background = pygame.transform.scale(background, (800, 650))
        background_rect = background.get_rect()

        screen.blit(background, background_rect)

        if pygame.mouse.get_focused() and lvl == 0:  # В зависимости от уровня, отображаем определенные спрайты
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

    pygame.quit()  # Если цикл завершен, выходим


if __name__ == "__main__":
    main()
