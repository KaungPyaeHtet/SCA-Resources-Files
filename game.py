import pygame

WIDTH, HEIGHT = 800, 400

pygame.init()
pygame.display.set_caption("Runner")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill('Red')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.blit(test_surface, (0, 0))
    clock.tick(60)
    pygame.display.update()