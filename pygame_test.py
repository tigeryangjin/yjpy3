import sys

import pygame

pygame.init()
surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('杨进的游戏')
surface.fill((255, 255, 255))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
