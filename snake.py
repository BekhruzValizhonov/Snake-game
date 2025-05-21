import pygame

UP = 119
DOWN = 115
LEFT = 97
RIGHT = 100


class Snake:
  def __init__(self):
    # Snake positions
    self.snake = [(200, 200), (210, 200), (220, 200), (230, 200), (240, 200)]
    # Head
    self.head = pygame.Surface((10, 10))
    self.head.fill((200, 200, 200))
    # Body
    self.skin = pygame.Surface((10, 10))
    self.skin.fill((255, 255, 255))
    self.direction = RIGHT

  def craw(self):
    if self.direction == RIGHT:
      self.snake.append((self.snake[len(self.snake) - 1][0] + 10, self.snake[len(self.snake) - 1][1]))
    elif self.direction == UP:
      self.snake.append((self.snake[len(self.snake) - 1][0], self.snake[len(self.snake) - 1][1] - 10))
    elif self.direction == DOWN:
      self.snake.append((self.snake[len(self.snake) - 1][0], self.snake[len(self.snake) - 1][1] + 10))
    elif self.direction == LEFT:
      self.snake.append((self.snake[len(self.snake) - 1][0] - 10, self.snake[len(self.snake) - 1][1]))

    self.snake.pop(0)

  def snake_eat_apple(self, apple_pos):
    return self.snake[-1] == apple_pos

  def snake_bigger(self):
    self.snake.insert(0, (self.snake[0]))

  def self_collision(self):
    return self.snake[-1] in self.snake[0:-1]

  def wall_collision(self):
    return self.snake[len(self.snake) - 1][0] >= 400 or self.snake[len(self.snake) - 1][0] < 0 or \
      self.snake[len(self.snake) - 1][1] >= 400 or self.snake[len(self.snake) - 1][1] < 0
