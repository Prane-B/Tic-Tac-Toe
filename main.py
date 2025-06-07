import pygame
from pygame import mouse

display = pygame.display.set_mode((800, 800))

RUN = True
while RUN:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
    print(mouse.get_pos())
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 255, 255), (305, 130, 5, 550))
    pygame.draw.rect(display, (255, 255, 255), (505, 130, 5, 550))
    pygame.draw.rect(display, (255, 255, 255), (135, 300, 550, 5))
    pygame.draw.rect(display, (255, 255, 255), (135, 500, 550, 5))
    pygame.display.flip()