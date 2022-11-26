import pygame
import pascal 
import time

TRIANGLE_SIZE = 600

GRANULARITY = 3

triangle_rows = pascal.Pascal(TRIANGLE_SIZE).getTriangle()

HEIGHT, WIDTH = 600, 600
FPS = 20
surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pascal")

def draw(GRANULARITY):
    y = GRANULARITY
    for row in triangle_rows:
        x = GRANULARITY
        for tile in row:
            # print(x, y)
            # print(tile.drawTile(), end = ', ')
            actual_val_color = tile.drawTile()

            r, g, b = 0, 0, 0

            rectangle = pygame.Rect(x, y, GRANULARITY, GRANULARITY)
            # rectangle_inv = pygame.Rect(600-x, 600-y, 1, 1)
            pygame.draw.rect(surface, tile.drawTile(), rectangle)
            # pygame.draw.rect(surface, tile.drawTile(), rectangle_inv)
            # rectangle.move(x + 69, y + 69)
            x += GRANULARITY
        # print()
        y += GRANULARITY

    pygame.display.update()

clock = pygame.time.Clock()
run = True
while True:
    
    clock.tick(FPS)
    draw(GRANULARITY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not run:
        pygame.quit()
        quit()

