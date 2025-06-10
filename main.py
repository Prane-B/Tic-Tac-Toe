import pygame
from pygame import mouse

display = pygame.display.set_mode((800, 800))
O_uncrop = pygame.image.load('Assets/O.png')
X_uncrop = pygame.image.load('Assets/X.png')
O = pygame.transform.scale(O_uncrop, (150, 150))
X = pygame.transform.scale(X_uncrop, (150, 150))
row1 = ["x","x","x"]
row2 = ["x","x","x"]
row3 = ["x","x","x"]
turn = 0
x,y = 1000,1000
RUN = True
while RUN:
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 255, 255), (305, 130, 5, 520))
    pygame.draw.rect(display, (255, 255, 255), (480, 130, 5, 520))
    pygame.draw.rect(display, (255, 255, 255), (135, 300, 520, 5))
    pygame.draw.rect(display, (255, 255, 255), (135, 475, 520, 5))

    for i in row1:
        if i == "0l":
            display.blit(O, (145,140))
        if i == "1l":
            display.blit(X, (145,140))
        if i == "0m":
            display.blit(O, (320,140))
        if i == "1m":
            display.blit(X, (320,140))
        if i == "0r":
            display.blit(O, (495,140))
        if i == "1r":
            display.blit(X, (495,140))
    i = 0
    for j in row2:
        if j == "0l":
            display.blit(O, (145,315))
        if j == "1l":
            display.blit(X, (145,315))
        if j == "0m":
            display.blit(O, (320,315))
        if j == "1m":
            display.blit(X, (320,315))
        if j == "0r":
            display.blit(O, (495,315))
        if j == "1r":
            display.blit(X, (495,315))
    for k in row3:
        if k == "0l":
            display.blit(O, (145,490))
        if k == "1l":
            display.blit(X, (145,490))
        if k == "0m":
            display.blit(O, (320,490))
        if k == "1m":
            display.blit(X, (320,490))
        if k == "0r":
            display.blit(O, (495,490))
        if k == "1r":
            display.blit(X, (495,490))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = mouse.get_pos()

            #ROW 1
            if x in range(135,310) and y in range(130,305):
                if turn == 0 and row1[0] == "x":
                    turn = 1
                    row1[0] = "0l"
                elif turn == 1 and row1[0] == "x":
                    turn = 0
                    row1[0] = "1l"
            if x in range(310,485) and y in range(130,305):
                if turn == 0 and row1[1] == "x":
                    turn = 1
                    row1[1] = "0m"
                elif turn == 1 and row1[1] == "x":
                    turn = 0
                    row1[1] = "1m"
            if x in range(485,655) and y in range(130,305):
                if turn == 0 and row1[2] == "x":
                    turn = 1
                    row1[2] = "0r"
                elif turn == 1 and row1[2] == "x":
                    turn = 0
                    row1[2] = "1r"

            #ROW 2
            if x in range(135,310) and y in range(305,480):
                if turn == 0 and row2[0] == "x":
                    turn = 1
                    row2[0] = "0l"
                elif turn == 1 and row2[0] == "x":
                    turn = 0
                    row2[0] = "1l"
            if x in range(310,485) and y in range(305,480):
                if turn == 0 and row2[1] == "x":
                    turn = 1
                    row2[1] = "0m"
                elif turn == 1 and row2[1] == "x":
                    turn = 0
                    row2[1] = "1m"
            if x in range(485,655) and y in range(305,480):
                if turn == 0 and row2[2] == "x":
                    turn = 1
                    row2[2] = "0r"
                elif turn == 1 and row2[2] == "x":
                    turn = 0
                    row2[2] = "1r"

            #ROW 3
            if x in range(135,310) and y in range(480,655):
                if turn == 0 and row3[0] == "x":
                    turn = 1
                    row3[0] = "0l"
                elif turn == 1 and row3[0] == "x":
                    turn = 0
                    row3[0] = "1l"
            if x in range(310,485) and y in range(480,655):
                if turn == 0 and row3[1] == "x":
                    turn = 1
                    row3[1] = "0m"
                elif turn == 1 and row3[1] == "x":
                    turn = 0
                    row3[1] = "1m"
            if x in range(485,655) and y in range(480,655):
                if turn == 0 and row3[2] == "x":
                    turn = 1
                    row3[2] = "0r"
                elif turn == 1 and row3[2] == "x":
                    turn = 0
                    row3[2] = "1r"
    pygame.display.flip()