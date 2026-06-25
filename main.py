import pygame

WIDTH = 400
HEIGHT = 200

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

screen.fill((200, 200, 200))

while True:
    clock.tick(60)
    
    pygame.display.update()