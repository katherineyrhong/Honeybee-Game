import os
import pygame
from pygame.locals import *
import time
import random

SIZE = 40
WIDTH = 800
HEIGHT = 600
white = (255, 255, 255)
bee = pygame.image.load(os.path.join("Assets", "bee.png"))
honey = pygame.image.load(os.path.join("Assets", "honey.png"))


class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.bee = pygame.transform.flip(pygame.transform.scale(bee, (40, 40)), True, False)
        self.direction = 'down'

        self.length = length
        self.x = [SIZE] * length
        self.y = [SIZE] * length

    # increase every time a collision happens between bee and honey
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.bee, (self.x[i], self.y[i]))

    def move_up(self):
        self.direction = "up"

    def move_down(self):
        self.direction = "down"

    def move_left(self):
        self.direction = "left"

    def move_right(self):
        self.direction = "right"

    def auto_move(self):
        # moving snake body with head
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]

        # moving snake head
        if self.direction == "up":
            self.y[0] -= SIZE
        if self.direction == "down":
            self.y[0] += SIZE
        if self.direction == "left":
            self.x[0] -= SIZE
        if self.direction == "right":
            self.x[0] += SIZE

        self.draw()


class Snack:
    def __init__(self, parent_screen):
        self.snack = pygame.transform.flip(pygame.transform.scale(
            honey, (40, 40)), True, False)

        self.parent_screen = parent_screen
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.snack, (self.x, self.y))

    # randomly choose where honey will appear next
    def spawn(self):
        self.x = random.randint(1, 19) * SIZE
        self.y = random.randint(1, 14) * SIZE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Honeybee Game")
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))

        self.snake = Snake(self.surface, 1)
        self.snake.draw()

        self.snack = Snack(self.surface)
        self.snack.draw()

    def collision(self, x1, y1, x2, y2):
        if y1 == y2:
            if x1 == x2:
                return True
        return False

    def render_background(self):
        # background scaled to match game window
        bg = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", "sky.jpg")), (WIDTH, HEIGHT))
        self.surface.blit(bg, (0, 0))

    def play(self):
        self.render_background()
        self.snake.auto_move()
        self.snack.draw()
        self.score()
        pygame.display.flip()

        # snake colliding with snack which increases score
        if self.collision(self.snake.x[0], self.snake.y[0], self.snack.x, self.snack.y):
            sound = pygame.mixer.Sound("assets/bubble.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.snack.spawn()

        # snake colliding with itself and game ends
        for i in range(2, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                collide = pygame.mixer.Sound("assets/collide.mp3")
                pygame.mixer.Sound.play(collide)
                raise "GAME OVER"

        # snake colliding with the walls of the window and game ends
        if not (0 <= self.snake.x[0] <= WIDTH and 0 <= self.snake.y[0] <= HEIGHT):
            collide = pygame.mixer.Sound("assets/collide.mp3")
            pygame.mixer.Sound.play(collide)
            raise "GAME OVER"

    def score(self):
        # score needs to begin at 0
        font = pygame.font.SysFont("FreeSansBold.ttf", 50)
        score = font.render(f"Honey collected: {self.snake.length - 1}", True, white)
        self.surface.blit(score, (450, 20))

    def game_over(self):
        self.render_background()

        # prompt user for enter or esc
        font = pygame.font.SysFont("FreeSansBold.ttf", 45)
        line1 = font.render(f"Final score: {self.snake.length - 1}", True, white)
        self.surface.blit(line1, (100, 330))

        line2 = font.render("Press ENTER to play again!", True, white)
        self.surface.blit(line2, (100, 390))
        pygame.display.flip()

        line3 = font.render("Press ESC to exit.", True, white)
        self.surface.blit(line3, (100, 430))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.surface, 1)
        self.snack = Snack(self.surface)

    def run(self):
        # pause prevents user from pressing keys when game is not running
        running = True
        pause = False

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_RETURN:
                        pause = False
                    # only one key press at a time is allowed
                    if not pause:
                        if event.key == pygame.K_UP:
                            self.snake.move_up()
                        if event.key == pygame.K_DOWN:
                            self.snake.move_down()
                        if event.key == pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key == pygame.K_RIGHT:
                            self.snake.move_right()

                elif event.type == pygame.QUIT:
                    running = False

            # exceptions in game_over function
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()

            # determines bee speed
            time.sleep(0.125)


if __name__ == '__main__':
    game = Game()
    game.run()
