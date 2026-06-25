import pygame
import sys

WIDTH = 600
HEIGHT = 200

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TRY TO DENY")
clock = pygame.time.Clock()

screen.fill((255, 255, 255))

def render_form():
    font = pygame.font.Font(None, 30)
    surface = pygame.Surface((600, 400), pygame.SRCALPHA)

    form_text = font.render("Do you want to close this window?", True, (0, 0, 0))
    reopen_button_text = font.render("YES", True, (255, 255, 255))

    rect_form_text = form_text.get_rect(center=surface.get_rect().center, top=20)
    surface.blit(form_text, rect_form_text)

    reopen_button_rect = pygame.Rect(175, 100, 100, 50)

    pygame.draw.rect(surface, (0, 150, 0), reopen_button_rect)
    pygame.draw.rect(surface, (0, 0, 0), reopen_button_rect, 3)

    reopen_button_text_rect = reopen_button_text.get_rect(center=reopen_button_rect.center)
    surface.blit(reopen_button_text, reopen_button_text_rect)

    surface_rect = surface.get_rect(center=surface.get_rect().center)
    screen.blit(surface, surface_rect)

while True:
    clock.tick(60)

    render_form()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pass

    pygame.display.update()