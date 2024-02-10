import pygame

# class Card:
#     def __init__(self, suit, rank, x, y) -> None:
#         self.suit = suit
#         self.rank = rank
#         self.x = x
#         self.y = y
#         self.rect = pygame.Rect(self.x, self.y, 50, 70)
#         self.num_font = pygame.font.SysFont('arial', 20)
#         self.num = self.num_font.render(str(rank), True, (0, 255, 0))

#         self.surface = pygame.Surface((50, 70))

#     def draw(self) -> None:
#         self.surface.fill((255, 255, 255))
#         self.surface.blit(self.num, (0,0))


pygame.init()



screen = pygame.display.set_mode((800, 600))

surface = pygame.Surface((50, 70))
num_font = pygame.font.SysFont('arial', 20)
num = num_font.render("8", True, (0, 0, 0))

x = 0

while True:
    surface.fill((255,255,255))
    surface.blit(num, (0,0))
    screen.blit(surface, (x, 0))
    x = 100
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

