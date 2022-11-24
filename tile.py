import pygame
import pascal 
import time

TRIANGLE_SIZE = 69

triangle_rows = pascal.Pascal(TRIANGLE_SIZE).getTriangle()

HEIGHT, WIDTH = 600, 800
FPS = 20
surface = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("pascal")

def draw():
    y = 12
    for row in triangle_rows:
        x = 12
        for tile in row:
            # print(x, y)
            # print(tile.drawTile(), end = ', ')
            actual_val_color = tile.drawTile()

            r, g, b = 0, 0, 0

            rectangle = pygame.Rect(x, y, 10, 10)
            pygame.draw.rect(surface, tile.drawTile(), rectangle)
            rectangle.move(x + 69, y + 69)
            x += 12
        # print()
        y += 12 

    pygame.display.update()

clock = pygame.time.Clock()
run = True
while True:
    
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if not run:
        pygame.quit()
        quit()

