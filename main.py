# import pygame.display

from modules import *
from player import Player
from background import Background
from button import Button
pygame.init()


class Main:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode((640, 480))
        self.x_pos, self.y_pos = 0, 0
        self.weigh, self.height = 20, 20
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.right_move = False
        self.left_move = True
        self.coin_image_path = os.path.join('data', 'money.jpg')
        self.coin_image = pygame.image.load(self.coin_image_path)
        self.coin_image = pygame.transform.scale(self.coin_image, (100, 100))
        self.fall_sound_path = os.path.join('data', 'multyashnyiy-zvuk-padeniya.mp3')
        self.fall_sound = pygame.mixer.Sound(self.fall_sound_path)
        self.create()
        self.move()

    def create(self):  # создание монет
        self.SCREEN.fill((255, 255, 255))
        for i in range(5):
            self.SCREEN.blit(self.coin_image, (random.randint(20, 480), random.randint(10, 480)))
        pygame.display.update()
        pygame.display.flip()

    def move(self):  # движение
        moving = True
        while moving:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    moving = False
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1 and self.left_move is True:
                        self.y_pos -= 50
                        self.x_pos += 25
                    if i.button == 1 and self.right_move is True:
                        self.y_pos -= 50
                        self.x_pos -= 25
            if self.y_pos == 390:
                print('game over!')
            else:
                if self.x_pos <= 540 and self.right_move is False:
                    if self.x_pos == 540:
                        self.right_move = True
                        self.left_move = False
                    self.x_pos += 1
                    self.y_pos += 2
                if self.x_pos >= 1 and self.left_move is False:
                    if self.x_pos == 0:
                        self.left_move = True
                        self.right_move = False
                    self.x_pos -= 1
                    self.y_pos += 2
                if self.x_pos <= 1 and self.left_move is False:
                    self.x_pos += 1
                    self.y_pos += 2
                    self.left_move = True
                    self.right_move = False
                if self.x_pos > 540 and self.right_move is False:
                    self.x_pos -= 1
                    self.y_pos += 2
                    self.right_move = True
                    self.left_move = False
            self.SCREEN.blit(self.player.sprite.image, (self.x_pos, self.y_pos))
            self.clock.tick(60) / 1000.0
            pygame.display.update()
            pygame.display.flip()


if __name__ == '__main__':
    Main()
