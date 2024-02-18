import pygame


def draw_text(instance, text, x, y, center=False):
    white = (255, 255, 255)
    blue = (0, 0, 255)
    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(text, True, white, blue)
    text_rect = text.get_rect()
    if not center:
        text_rect.topleft = (x, y)
    else:
        text_rect.center = (x, y)
    instance.display_surf.blit(text, text_rect)
