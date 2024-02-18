from enums.GameState import GameState
from functions.DrawText import draw_text


def render_main(instance):
    if instance.game_state == GameState.MAIN:
        draw_text(instance, 'STAGG', 300, 30, True)
        draw_text(instance, 'We all seek the Double G', 300, 50, True)
        draw_text(instance, 'Rules:', 300, 100, True)
        draw_text(instance, 'Ranno is growing tired. Collect the chilli to keep him lively,', 300, 120, True)
        draw_text(instance, "look out for the Sambuca though! We think he's had enough.", 300, 140, True)
        draw_text(instance, 'Press BAR to start', 300, 350, True)
