import pygame


class Timer:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self._time_elapsed = 0

    def get_time(self):
        return self._time_elapsed

    def increase_timer(self, fps):
        self._clock.tick(fps)
        self._time_elapsed += (self._clock.get_time() / 1000)
