import pygame

pygame.init()

screen = pygame.display.set_mode((640, 240))

r = pygame.Rect(0, 0, 20, 20)

while True:
    pygame.draw.rect(screen, (255,0,0), r)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


# class Card:
#     def __init__(self, suit, rank, x, y) -> None:
        
