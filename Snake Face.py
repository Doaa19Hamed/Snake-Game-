WIDTH = 600                   #putting the width
HEIGHT = 600                   #putting the hight
ROWS = 21
SQUARE_SIZE = WIDTH // ROWS
GAP_SIZE = 2                    #adjacent squares
SURFACE_CLR = "#000000"         #putting colors for (surface,head,Aplle,grid)using color codes
SNAKE_CLR = "#550A35"
APPLE_CLR = "#E799A3"
HEAD_CLR = "#F67280"
GRID_CLR = "#550A35"
VIRTUAL_SNAKE_CLR = "#944B03"
FRAMES = 14                          # FPS= SPEED
INITIAL_SNAKE_LENGTH = 2             #THE LENGTH OF FIRST SNAKE APPEAR IN GAME IS 2
AFTER_WIN = 20                      #PUTTING SECONDS BEFORE RESTARTING AGAIN
MAX_MOVES_WITHOUT_EATING = ROWS * ROWS * ROWS * 2
SNAKE_MAX_LENGTH = ROWS * ROWS - INITIAL_SNAKE_LENGTH
GRID = [[i, j] for i in range(ROWS) for j in range(ROWS)]                    #  VARIABLES USED IN BFS ALGORITHM

def distance(pos1, pos2):
    Z1, Z2 = pos1[0], pos2[0]
    F1, F2 = pos1[1], pos2[1]
    return abs(Z2 - Z1) + abs(F2 - F1)

def get_neighbors(position):
    neighbors = [[position[0] + 1, position[1]], [position[0] - 1, position[1]], [position[0], position[1] + 1], [position[0], position[1] - 1]]
    in_grid_neighbors = []
    for pos in neighbors:
        if pos in GRID:
            in_grid_neighbors.append(pos)
    return in_grid_neighbors
ADJACENCY_DICT = {tuple(pos): get_neighbors(pos) for pos in GRID}