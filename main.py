import select

import pygame.transform

from modules import *
from player import Player
from background import Background
pygame.init()


class Main:
    def __init__(self):
        self.SCREEN = pygame.display.set_mode((640, 480))
        self.screen_for_player = pygame.display.set_mode((640, 480))
        self.play_button = pygame.image.load('data/play_button.png')
        self.x_pos, self.y_pos = 0, 0
        self.weigh, self.height = 20, 2
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.right_move = False
        self.left_move = True
        self.pizza_image = pygame.image.load('data/pizzza.png').convert()
        self.pizza_image = pygame.transform.scale(self.pizza_image, (100, 100))
        self.fon_music = pygame.mixer.Sound('data/muzika_na_zadnij_fon_-_bez_nazvanija_(z2.fm).mp3')
        self.fall_sound = pygame.mixer.Sound('data/multyashnyiy-zvuk-padeniya.mp3')
        self.start()

    def start(self):  # начальное окно старта
        self.fon_music.play()
        self.SCREEN.fill((255, 255, 255))
        self.SCREEN.blit(self.play_button, (180, 292))
        run = True
        while run:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if i.pos[0] >= 214 and i.pos[0] <= 430 and i.pos[1] >= 335 and i.pos[1] <= 420:
                        run = False
            pygame.time.delay(12)
            pygame.display.update()
        self.fon_music.stop()
        self.create()
        self.move()

    def game_over(self):  # окно при проигрыше
        self.fon_music.play()
        run = True
        self.SCREEN.fill((0, 0, 0))
        over_photo = pygame.image.load('data/game_over.png')
        self.SCREEN.blit(over_photo, (120, 150))
        retry_photo = pygame.image.load('data/retry_ar.png')
        self.SCREEN.blit(retry_photo, (0, 0))
        while run:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if i.pos[0] >= 2 and i.pos[0] <= 150 and i.pos[1] >= 1 and i.pos[1] <= 80:
                        self.fon_music.stop()
                        self.create()
                        self.move()
            pygame.display.flip()

    def create(self):  # создание предметов для сбора энергии
        self.SCREEN.fill((255, 255, 255))
        for i in range(5):
            self.SCREEN.blit(self.pizza_image, (random.randint(20, 480), random.randint(10, 480)))
        pygame.display.update()

    def move(self):  # движение
        moving = True
        while moving:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1 and self.left_move is True:
                        self.y_pos -= 60
                        self.x_pos += 25
                    if i.button == 1 and self.right_move is True:
                        self.y_pos -= 60
                        self.x_pos -= 25
            if self.y_pos == 390:
                self.x_pos = 0
                self.y_pos = 0
                self.game_over()
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
            self.SCREEN.fill((255, 255, 255))

            self.SCREEN.blit(self.player.sprite.image, (self.x_pos, self.y_pos))
            pygame.time.delay(12)
            pygame.display.update()
            pygame.display.flip()

    # def checkCollision(self):
    #     col = pygame.sprite.collide_rect(self.sprite.pizza, self.player.sprite.rect)
    #     if col == True:
    #         print('collision')


if __name__ == '__main__':
    Main()
