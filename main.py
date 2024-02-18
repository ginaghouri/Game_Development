import os
import pygame
import uuid
import math
from enums.GameState import GameState
from classes.Player import Player
from classes.Timer import Timer
from classes.Collectable import Collectable
from functions.renders.Main import render_main
from functions.renders.Play import render_play
from functions.DrawText import draw_text
from functions.DrawGamePad import draw_game_pad
from functions.Controls import controls
from functions.RandomSpawn import random_spawn
from functions.Collect import collect_collectable

class App:
    def __init__(self):
        # Game Runner
        self.running = True
        self.game_state = GameState.MAIN
        # Main Window Stuff
        pygame.mixer.init()
        game_folder = os.path.dirname(__file__)
        assets_folder = os.path.join(game_folder, 'assets')
        self.bgm = pygame.mixer.Sound(os.path.join(assets_folder, 'Stagg.ogg'))
        self.display_surf = None
        self._size = self.width, self.height = 600, 800
        self._window_name = "Stagg: Prepare to Ranno Edition"
        # Time Stuff
        self.clock = Timer()
        self._last_time = 0
        self.game_time = 0
        # Player Stuff
        self.game_player = Player()
        self.staggs = {}
        self.sambuccas = {}
        # Debug Stuff
        self.debug_string = ''
        self.debug_string_2 = ''

    def on_init(self):
        pygame.init()
        pygame.display.set_caption(self._window_name)
        self.display_surf = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.running = True
        self.bgm.set_volume(0.5)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        controls(self, event)

    def on_loop(self):
        if self.game_state == GameState.PLAY:
            if pygame.mixer.get_busy() == False:
                self.bgm.play()
            self.clock.increase_timer(30)
            self.game_time = self.clock.get_time()
            if int(self.game_time) != int(self._last_time) and self.game_player.get_energy() > 0:
                self._last_time = self.game_time
                self.game_player.alter_energy(-1)
                if int(self.game_time) % 3 == 0:
                    # Spawn Sambucca
                    sp = random_spawn()
                    self.sambuccas[uuid.uuid4()] = Collectable('Sambucca', -10, sp)
                    # self.debug_string_2 = f'Sambucca = {sp}'
                if int(self.game_time) % 5 == 0:
                    # Spawn Stagg
                    sp = random_spawn()
                    self.staggs[uuid.uuid4()] = Collectable('Stagg', 5, sp)
                    # self.debug_string_2 = f'Stagg = {sp}'
            collect_collectable(self)


    def on_render(self):
        render_main(self)
        render_play(self)
        draw_game_pad(self)
        draw_text(self, f'DEBUG:{self.debug_string}', 10, 780)
        draw_text(self, f'DEBUG:{self.debug_string_2}', 10, 760)

    @staticmethod
    def on_cleanup():
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self.running = False
        while self.running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            pygame.display.update()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
