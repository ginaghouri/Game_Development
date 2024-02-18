import pygame
from enums.GameState import GameState
from functions.DrawText import draw_text
from functions.DrawImage import draw_player, draw_stagg, draw_sambucca


def render_play(instance):
    if instance.game_state == GameState.PLAY:
        instance.display_surf.fill(pygame.Color('black'))
        if instance.game_player.get_energy() <= 0:
            draw_text(instance, 'YOU DEAD', 300, 300, True)
        else:
            draw_player(instance)
        draw_text(instance, f'Time Alive = {int(instance.game_time)}', 10, 10)
        draw_text(instance,
                  f'Energy = {int(instance.game_player.get_energy())} / {int(instance.game_player.get_max_energy())}',
                  10,
                  30)
        draw_stagg(instance)
        draw_sambucca(instance)
