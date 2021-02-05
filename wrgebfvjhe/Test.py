import os
import sys

import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image

def main():
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Свой курсор')
    all_sprites = pygame.sprite.Group()

    cursor_image = load_image("Arrow.png")
    cursor = pygame.sprite.Sprite(all_sprites)
    game = pygame.transform.scale(cursor, (200, 200))
    cursor.rect = cursor.game.get_rect()
    pygame.mouse.set_visible(False)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                cursor.rect.topleft = event.pos
        screen.fill(pygame.Color("black"))
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()