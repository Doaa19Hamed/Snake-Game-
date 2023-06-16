from snake import *
from os import environ
def screen(surface):
    surface.fill(SURFACE_CLR)
def drawgrid(surface):
    Z = 0
    F = 0
    for r in range(ROWS):
        Z = Z + SQUARE_SIZE
        F = F + SQUARE_SIZE
        pygame.draw.line(surface, GRID_CLR, (Z, 0), (Z, HEIGHT))
        pygame.draw.line(surface, GRID_CLR, (0, F), (WIDTH, F))
def Playgame():
    pygame.init()
    environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.display.set_caption("SNAKE")
    game_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake(game_surface)
    loop = True
    while loop:
        screen(game_surface)
        drawgrid(game_surface)
        snake.update()
        clock.tick(FRAMES)
        pygame.display.update()
if _name_ == '_main_':
    Playgame()