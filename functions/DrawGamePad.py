import pygame
from enums.ButtonPositions import ButtonPositions

background_color = (100, 100, 100)
background_border_color = (80, 80, 80)
button_color = (170, 170, 170)
white = (255, 255, 255)


def draw_game_pad(instance):
    # Button Font
    button_font = pygame.font.SysFont('arial', 35)

    pygame.draw.rect(instance.display_surf, background_color, [0, 600, 600, 300])
    pygame.draw.rect(instance.display_surf, background_border_color, [0, 600, 600, 20])

    # Arrow Keys
    pygame.draw.rect(instance.display_surf, button_color, ButtonPositions.UP.value)
    up_text = button_font.render(f'↑', True, white)
    instance.display_surf.blit(up_text, ButtonPositions.UP.value)

    pygame.draw.rect(instance.display_surf, button_color, ButtonPositions.DOWN.value)
    down_text = button_font.render(f'↓', True, white)
    instance.display_surf.blit(down_text, ButtonPositions.DOWN.value)

    pygame.draw.rect(instance.display_surf, button_color, ButtonPositions.LEFT.value)
    left_text = button_font.render(f'←', True, white)
    instance.display_surf.blit(left_text, ButtonPositions.LEFT.value)

    pygame.draw.rect(instance.display_surf, button_color, ButtonPositions.RIGHT.value)
    right_text = button_font.render(f'→', True, white)
    instance.display_surf.blit(right_text, ButtonPositions.RIGHT.value)

    # Go Button
    pygame.draw.rect(instance.display_surf, button_color, ButtonPositions.BAR.value)
    bar_text = button_font.render(f'BAR', True, white)
    instance.display_surf.blit(bar_text, ButtonPositions.BAR.value)


def button_clicked(buttonPosition, pos):
    if (pos[0] > buttonPosition.value[0] and pos[0] < (buttonPosition.value[0] + buttonPosition.value[2]) and
            (pos[1] > buttonPosition.value[1] and pos[1] < (buttonPosition.value[1] + buttonPosition.value[3]))):
        return True

