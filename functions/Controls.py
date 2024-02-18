import pygame
from enums.GameState import GameState
from classes.Timer import Timer
from enums.ButtonPositions import ButtonPositions
from functions.DrawGamePad import button_clicked


def controls(instance, event):
    # instance.debug_string = f'Ranno Position: {instance.game_player.get_pos()}'
    # MOUSE
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        if instance.game_state == GameState.PLAY:
            if button_clicked(ButtonPositions.UP, pos):
                instance.game_player.move(0, -5)
            if button_clicked(ButtonPositions.DOWN, pos):
                instance.game_player.move(0, 5)
            if button_clicked(ButtonPositions.LEFT, pos):
                instance.game_player.move(-5, 0)
            if button_clicked(ButtonPositions.RIGHT, pos):
                instance.game_player.move(5, 0)
        if instance.game_state == GameState.MAIN:
            if button_clicked(ButtonPositions.BAR, pos):
                instance.clock = Timer()
                instance.bgm.play()
                instance.game_state = GameState.PLAY

    # KEYBOARD
    if event.type == pygame.KEYDOWN:
        if instance.game_state == GameState.MAIN:
            if event.key == pygame.K_SPACE:
                instance.clock = Timer()
                instance.game_state = GameState.PLAY
        if instance.game_state == GameState.PLAY:
            # Directional Controls
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                instance.game_player.move(0, 5)
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                instance.game_player.move(0, -5)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                instance.game_player.move(-5, 0)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                instance.game_player.move(5, 0)

            # Exit Game
            if event.key == pygame.K_ESCAPE:
                instance.bgm.stop()
                instance.running = False
