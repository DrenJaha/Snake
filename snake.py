import pygame
import random

class Snake(): #creating the snake itself
    def __init__(self): #attributes
        self.length = 3
        self.position = [(WIDTH // 2, HEIGHT // 2), (WIDTH // 2, HEIGHT // 2 + gridsize), (WIDTH // 2, HEIGHT // 2 + 2 * gridsize)]
        self.colour = (0, 128, 0)
        self.direction = up
        self.score = 0

    def drawSnake(self, window):
        for block in self.position:
            pygame.draw.rect(window, self.colour, (block[0], block[1], gridsize, gridsize))

    def movement(self): #movement of the snake
        head = self.position[0]
        x, y = self.direction
        next = ((head[0] + x * gridsize) % WIDTH, (head[1] + y * gridsize) % HEIGHT)
        self.position.insert(0, next)
        self.position.pop()

    def check_end_game(self, window):
        if self.position[0] in self.position[1:]:
            global highscore
            highscore = self.score if self.score > highscore else highscore
            myfont = pygame.font.SysFont('Courier New', 25)
            text = myfont.render("Game Over", True, (0, 0, 0))
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 20))
            myfont2 = pygame.font.SysFont('Courier New', 10)
            text2 = myfont.render("Get Ready!", True, (0, 0, 0))
            text2_rect = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            window.blit(text, text_rect)
            window.blit(text2, text2_rect)
            pygame.display.update()
            pygame.time.delay(5000)
            self.__init__()

    def change_direction(self): #changing the direction of the snake
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not self.direction == down:
                        self.direction = up
                elif event.key == pygame.K_DOWN:
                    if not self.direction == up:
                        self.direction = down
                elif event.key == pygame.K_LEFT:
                    if not self.direction == right:
                        self.direction = left
                elif event.key == pygame.K_RIGHT:
                    if not self.direction == left:
                        self.direction = right

class Apple():
    def __init__(self):
        self.position = (random.randint(0, WIDTH) // grids * grids, random.randint(0, WIDTH) // grids * grids)
        self.colour = (255, 0, 0)

    def draw_apple(self, window):
        pygame.draw.rect(window, self.colour, (self.position[0], self.position[1], gridsize, gridsize))


WIDTH = 400
HEIGHT = 400

grids = 20
gridsize = WIDTH // grids

#directions initialized
up = (0, -1)
down = (0, 1)
right = (1, 0)
left = (-1, 0)

highscore = 0

def setBackground(window):
    window.fill((255, 255, 255))

def main():
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    setBackground(window)

    snake = Snake()
    apple = Apple()
    myfont = pygame.font.SysFont('Courier New', 20)

    while True:
        clock.tick(15)
        snake.movement()
        setBackground(window)
        snake.drawSnake(window)
        apple.draw_apple(window)
        snake.check_end_game(window)
        snake.check_end_game(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if not snake.direction == down:
                        snake.direction = up

                elif event.key == pygame.K_DOWN:
                    if not snake.direction == up:
                        snake.direction = down

                elif event.key == pygame.K_LEFT:
                    if not snake.direction == right:
                        snake.direction = left

                elif event.key == pygame.K_RIGHT:
                    if not snake.direction == left:
                        snake.direction = right

        if apple.position == snake.position[0]:
            snake.length += 1
            snake.score += 1
            snake.position.append((2 * snake.position[-1][0] - snake.position[-2][0], 2 * snake.position[-1][1] - snake.position[-2][1]))
            apple.__init__()

        text = myfont.render('Score: {}'.format(snake.score), True, (0, 0, 0))
        text2 = myfont.render('HighScore: {}'.format(highscore), True, (0, 0, 0))
        window.blit(text, (0, 0))
        window.blit(text2, (0, 20))
        pygame.display.update()

    return

main()
