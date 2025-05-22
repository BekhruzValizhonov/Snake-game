from pygame import KEYDOWN

from apple import Apple
from snake import *


# TODO so that he could go beyond the limit and come back out from the opposite side of the wall -> Done
# TODO show Score -> Done
# TODO pause game 'p' button

def main():
  SPEED = 15
  score = 0
  pygame.init()
  screen = pygame.display.set_mode((400, 400))
  snake = Snake()
  apple = Apple()
  apple.set_random_position()
  clock = pygame.time.Clock()

  run = True
  while run:
    clock.tick(SPEED)
    snake.craw()
    snake.snake_portal()

    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        run = False

      if e.type == KEYDOWN:
        if e.key == UP and snake.direction != DOWN:
          snake.direction = UP

        elif e.key == LEFT and snake.direction != RIGHT:
          snake.direction = LEFT

        elif e.key == DOWN and snake.direction != UP:
          snake.direction = DOWN

        elif e.key == RIGHT and snake.direction != LEFT:
          snake.direction = RIGHT

    if snake.snake_eat_apple(apple.position):
      apple.set_random_position()
      snake.snake_bigger()
      SPEED += 1
      score += 10

    if snake.self_collision():
      run = False

    screen.fill((0, 0, 0))

    for snake_pos in snake.snake[0:-1]:
      screen.blit(snake.skin, snake_pos)

    screen.blit(snake.head, snake.snake[-1])
    screen.blit(apple.apple, apple.position)
    screen.blit(snake.snake_score(score), (5, 5))
    pygame.display.update()

  pygame.quit()


if __name__ == '__main__':
  main()
