import pygame
import os


class Player:
    def __init__(self):
        self.position = None
        self.sprite = pygame.sprite.Sprite()
        self.all_sprites = pygame.sprite.Group()
        # filename = os.path.join('data', 'hero.jpg')
        self.sprite.image = pygame.image.load('data/cool_man.png')
        self.sprite.image = pygame.transform.scale(self.sprite.image, (100, 100))
        self.all_sprites.add(self.all_sprites)
        # self.sprite.rect = self.sprite.image.get_rect()
        #  загрузка изображения героя, определение позиции героя
        self.power = None
        #  энергия героя, если энергия равна 0 то игрок пригрывает

    def level_determination(self):
        pass
        #   при помощи позиции определяем уровень
