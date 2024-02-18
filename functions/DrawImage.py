import pygame
import os


def draw_player(instance):
    game_folder = os.path.dirname(__file__)
    assets_folder = os.path.join(game_folder, '../assets')
    img = pygame.image.load(os.path.join(assets_folder, 'RanRan.png')).convert_alpha()
    img_rect = img.get_rect()
    img_rect.center = instance.game_player.get_pos()
    instance.display_surf.blit(img, img_rect, )


def draw_sambucca(instance):
    game_folder = os.path.dirname(__file__)
    assets_folder = os.path.join(game_folder, '../assets')
    img = pygame.image.load(os.path.join(assets_folder, 'Sambucca.png')).convert_alpha()
    for key in instance.sambuccas:
        img_rect = img.get_rect()
        img_rect.center = instance.sambuccas[key].pos
        instance.display_surf.blit(img, img_rect, )


def draw_stagg(instance):
    game_folder = os.path.dirname(__file__)
    assets_folder = os.path.join(game_folder, '../assets')
    img = pygame.image.load(os.path.join(assets_folder, 'Stagg.png')).convert_alpha()
    for key in instance.staggs:
        img_rect = img.get_rect()
        img_rect.center = instance.staggs[key].pos
        instance.display_surf.blit(img, img_rect, )
